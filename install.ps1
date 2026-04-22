#Requires -Version 5.1
<#
.SYNOPSIS
    Universal skill installer for Windows - supports both system-level and project-level installation.

.DESCRIPTION
    This script installs AI Agent skills to system or project directories.
    It creates symbolic links (or junctions if symlinks require elevation) from
    skill directories to agent configuration directories.

.PARAMETER System
    Install to system directories (default: ~/.config/agents/skills/)

.PARAMETER Project
    Install to current project directory (./.agents/skills/)

.PARAMETER Agent
    Target specific agent (claude-code, kimi, codex, opencode)

.PARAMETER All
    Install all skills found in this directory

.PARAMETER List
    List available skills

.PARAMETER Skills
    Names of specific skills to install

.EXAMPLE
    .\install.ps1 -System -All
    Install all skills to system directories

.EXAMPLE
    .\install.ps1 -System -Skills "github-task-workflow","local-workflow"
    Install specific skills to system

.EXAMPLE
    .\install.ps1 -Project -All
    Install all skills to current project

.EXAMPLE
    .\install.ps1 -System -Agent kimi -All
    Install to kimi directory only

.EXAMPLE
    .\install.ps1 -System -Folder fe-skills -All
    Install all skills from fe-skills folder to system

.EXAMPLE
    .\install.ps1 -List
    List available skills
#>

param(
    [switch]$System,
    [switch]$Project,
    [string]$Agent = "",
    [string]$Folder = "",
    [switch]$All,
    [switch]$List,
    [switch]$ListFolders,
    [string[]]$Skills
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Colors for output
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Success { param([string]$Message) Write-ColorOutput $Message "Green" }
function Write-Warning { param([string]$Message) Write-ColorOutput $Message "Yellow" }
function Write-Error { param([string]$Message) Write-ColorOutput $Message "Red" }
function Write-Info { param([string]$Message) Write-ColorOutput $Message "Cyan" }

# Get list of available skill folders
function Get-AvailableFolders {
    $folders = @()
    Get-ChildItem -Path $ScriptDir -Directory | ForEach-Object {
        $dir = $_.FullName
        $hasSkill = $false
        Get-ChildItem -Path $dir -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            $skillMdPath = Join-Path $_.FullName "SKILL.md"
            if (Test-Path $skillMdPath) {
                $hasSkill = $true
            }
        }
        if ($hasSkill) {
            $folders += $_.Name
        }
    }
    return $folders
}

# Get list of available skills
function Get-AvailableSkills {
    param([string]$TargetFolder = "")

    $skills = @()
    $searchDir = $ScriptDir

    if ($TargetFolder -ne "") {
        $searchDir = Join-Path $ScriptDir $TargetFolder
        if (-not (Test-Path $searchDir)) {
            Write-Error "Error: Folder not found: $TargetFolder"
            exit 1
        }
    }

    Get-ChildItem -Path $searchDir -Directory | ForEach-Object {
        $skillMdPath = Join-Path $_.FullName "SKILL.md"
        if (Test-Path $skillMdPath) {
            if ($TargetFolder -ne "") {
                $skills += "$TargetFolder/$($_.Name)"
            } else {
                $skills += $_.Name
            }
        }
    }
    return $skills
}

# List available folders
function Show-Folders {
    Write-Info "Available skill folders:"
    $folders = Get-AvailableFolders
    if ($folders.Count -eq 0) {
        Write-Host "  (none - all skills are in root directory)"
    } else {
        foreach ($folder in $folders) {
            $count = (Get-ChildItem -Path (Join-Path $ScriptDir $folder) -Recurse -Filter "SKILL.md" | Measure-Object).Count
            Write-Host "  📁 $folder ($count skills)"
        }
    }

    Write-Host ""
    Write-Info "Root directory skills:"
    $rootSkills = @()
    Get-ChildItem -Path $ScriptDir -Directory | ForEach-Object {
        $skillMdPath = Join-Path $_.FullName "SKILL.md"
        if (Test-Path $skillMdPath) {
            $rootSkills += $_.Name
        }
    }
    if ($rootSkills.Count -eq 0) {
        Write-Host "  (none)"
    } else {
        foreach ($skill in $rootSkills) {
            Write-Host "  📄 $skill"
        }
    }
}

# List available skills
function Show-Skills {
    param([string]$TargetFolder = "")

    if ($TargetFolder -ne "") {
        Write-Info "Available skills in '$TargetFolder':"
    } else {
        Write-Info "Available skills:"
    }

    $skills = Get-AvailableSkills -TargetFolder $TargetFolder
    if ($skills.Count -eq 0) {
        Write-Host "  (none found)"
    } else {
        foreach ($skill in $skills) {
            $skillPath = Join-Path $ScriptDir $skill
            $desc = ""
            $skillMdPath = Join-Path $skillPath "SKILL.md"
            if (Test-Path $skillMdPath) {
                $line = Get-Content $skillMdPath | Select-Object -First 1
                if ($line -match "^description:\s*(.+)$") {
                    $desc = $matches[1].Substring(0, [Math]::Min(50, $matches[1].Length))
                }
            }
            if ($desc -ne "") {
                Write-Host "  📄 $skill - $desc..."
            } else {
                Write-Host "  📄 $skill"
            }
        }
    }
}

# Get system target directories based on agent
function Get-SystemTargetDirs {
    param([string]$TargetAgent)

    $dirs = @()
    $homePath = $env:USERPROFILE

    switch ($TargetAgent) {
        "" {
            # All supported agents
            $dirs += Join-Path $homePath ".config\agents\skills"
            $dirs += Join-Path $homePath ".claude\skills"
            $dirs += Join-Path $homePath ".kimi\skills"
            $dirs += Join-Path $homePath ".codex\skills"
            $dirs += Join-Path $homePath ".opencode\skills"
        }
        "claude-code" {
            $dirs += Join-Path $homePath ".claude\skills"
        }
        "kimi" {
            $dirs += Join-Path $homePath ".kimi\skills"
            $dirs += Join-Path $homePath ".config\agents\skills"
        }
        "codex" {
            $dirs += Join-Path $homePath ".codex\skills"
        }
        "opencode" {
            $dirs += Join-Path $homePath ".opencode\skills"
        }
        default {
            Write-Error "Error: Unknown agent '$TargetAgent'"
            Write-Host "Supported agents: claude-code, kimi, codex, opencode"
            exit 1
        }
    }
    return $dirs
}

# Get project target directories
function Get-ProjectTargetDirs {
    $dirs = @()
    $dirs += Join-Path $PWD ".agents\skills"
    $dirs += Join-Path $PWD ".kimi\skills"
    $dirs += Join-Path $PWD ".claude\skills"
    return $dirs
}

# Check if we can create symbolic links (requires admin on older Windows)
function Test-SymlinkCapability {
    $testPath = Join-Path $env:TEMP "symlink_test_$(Get-Random)"
    $testTarget = Join-Path $env:TEMP "symlink_test_target_$(Get-Random)"

    try {
        New-Item -ItemType Directory -Path $testTarget -Force | Out-Null
        New-Item -ItemType SymbolicLink -Path $testPath -Target $testTarget -Force | Out-Null
        Remove-Item $testPath -Force
        Remove-Item $testTarget -Force
        return $true
    }
    catch {
        return $false
    }
}

# Create link (symlink or junction)
function New-SkillLink {
    param(
        [string]$SourcePath,
        [string]$LinkPath
    )

    if ((Test-Path $LinkPath) -or (Get-Item $LinkPath -ErrorAction SilentlyContinue)) {
        Write-Warning "  [SKIP] Skill already exists at $LinkPath"
        return $false
    }

    $parentDir = Split-Path -Parent $LinkPath
    if (-not (Test-Path $parentDir)) {
        New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    }

    # Try symbolic link first, fall back to junction
    if (Test-SymlinkCapability) {
        try {
            New-Item -ItemType SymbolicLink -Path $LinkPath -Target $SourcePath -Force | Out-Null
            Write-Success "  [OK]   $(Split-Path -Leaf $SourcePath) -> $LinkPath"
            return $true
        }
        catch {
            # Fall through to junction
        }
    }

    # Use junction as fallback (doesn't require admin)
    try {
        New-Item -ItemType Junction -Path $LinkPath -Target $SourcePath -Force | Out-Null
        Write-Success "  [OK]   $(Split-Path -Leaf $SourcePath) -> $LinkPath (junction)"
        return $true
    }
    catch {
        Write-Error "  [ERROR] Failed to create link: $_"
        return $false
    }
}

# Get skill source path
function Get-SkillSource {
    param([string]$SkillName)

    if ($SkillName -match "/") {
        return Join-Path $ScriptDir $SkillName
    } else {
        if ($Folder -ne "") {
            $folderPath = Join-Path $ScriptDir $Folder $SkillName
            $folderSkillMd = Join-Path $folderPath "SKILL.md"
            if ((Test-Path $folderPath) -and (Test-Path $folderSkillMd)) {
                return $folderPath
            }
        }
        $rootPath = Join-Path $ScriptDir $SkillName
        $rootSkillMd = Join-Path $rootPath "SKILL.md"
        if ((Test-Path $rootPath) -and (Test-Path $rootSkillMd)) {
            return $rootPath
        }
        return $null
    }
}

# Get skill display name
function Get-SkillDisplayName {
    param([string]$SkillName)
    return Split-Path -Leaf $SkillName
}

# Install skill to target directory
function Install-SkillToDir {
    param(
        [string]$SkillName,
        [string]$SkillSrc,
        [string]$TargetDir
    )

    $displayName = Get-SkillDisplayName $SkillName
    $linkPath = Join-Path $TargetDir $displayName

    return New-SkillLink -SourcePath $SkillSrc -LinkPath $linkPath
}

# System-level installation
function Install-System {
    param([string[]]$SkillsToInstall)

    Write-Info "Installing skills to system directories..."

    if ($Folder -ne "") {
        Write-Info "Source folder: $Folder"
    }

    $targetDirs = Get-SystemTargetDirs -TargetAgent $Agent
    $installedCount = 0
    $skippedCount = 0

    foreach ($skillName in $SkillsToInstall) {
        Write-Host ""
        Write-Host "Installing: $skillName"

        $skillSrc = Get-SkillSource $skillName
        if ($null -eq $skillSrc) {
            Write-Error "  [ERROR] Skill not found: $skillName"
            continue
        }

        $displayName = Get-SkillDisplayName $skillName
        $skillInstalled = $false
        foreach ($targetDir in $targetDirs) {
            $result = Install-SkillToDir -SkillName $skillName -SkillSrc $skillSrc -TargetDir $targetDir
            if ($result) {
                $skillInstalled = $true
            }
            else {
                $skippedCount++
            }
        }

        if ($skillInstalled) {
            $installedCount++
        }
    }

    Write-Host ""
    Write-Success "System installation complete."
    Write-Host "  Installed: $installedCount skill(s)"
    Write-Host "  Skipped: $skippedCount existing link(s)"
}

# Project-level installation
function Install-Project {
    param([string[]]$SkillsToInstall)

    Write-Info "Installing skills to project directories..."

    if ($Folder -ne "") {
        Write-Info "Source folder: $Folder"
    }

    # Check if we're in a git repository
    if (-not (Test-Path ".git")) {
        Write-Warning "Warning: Current directory is not a git repository."
        $response = Read-Host "Continue anyway? (y/N)"
        if ($response -notmatch "^[Yy]$") {
            exit 1
        }
    }

    $targetDirs = Get-ProjectTargetDirs
    $installedCount = 0
    $skippedCount = 0

    foreach ($skillName in $SkillsToInstall) {
        Write-Host ""
        Write-Host "Installing: $skillName"

        $skillSrc = Get-SkillSource $skillName
        if ($null -eq $skillSrc) {
            Write-Error "  [ERROR] Skill not found: $skillName"
            continue
        }

        $displayName = Get-SkillDisplayName $skillName
        $skillInstalled = $false
        foreach ($targetDir in $targetDirs) {
            $result = Install-SkillToDir -SkillName $skillName -SkillSrc $skillSrc -TargetDir $targetDir
            if ($result) {
                $skillInstalled = $true
            }
            else {
                $skippedCount++
            }
        }

        if ($skillInstalled) {
            $installedCount++
        }
    }

    # Setup project configuration
    Set-ProjectConfig

    Write-Host ""
    Write-Success "Project installation complete."
    Write-Host "  Installed: $installedCount skill(s)"
    Write-Host "  Skipped: $skippedCount existing link(s)"
}

# Setup project-level configuration
function Set-ProjectConfig {
    Write-Host ""
    Write-Info "Setting up project configuration..."

    # Create .kimi/KIMI.md if not exists
    $kimiMdPath = Join-Path $PWD ".kimi\KIMI.md"
    if (-not (Test-Path $kimiMdPath)) {
        $kimiDir = Split-Path -Parent $kimiMdPath
        if (-not (Test-Path $kimiDir)) {
            New-Item -ItemType Directory -Path $kimiDir -Force | Out-Null
        }

        $kimiContent = @"
# Kimi CLI - Project Instructions

This project uses GitHub Task Workflow for task execution.

## Auto-Workflow Trigger

When the user asks you to "execute", "run", "implement", or "work on" a task file (e.g., ``tasks/*.md``), you **MUST** follow the **GitHub Task Workflow** defined in ``.agents/skills/github-task-workflow/SKILL.md``.

### Workflow Steps

1. **READ**: Read the task file
2. **CREATE ISSUE**: Run ``python .agents/skills/github-task-workflow/scripts/orchestrate.py init <task-file>``
3. **IMPLEMENT**: Execute the task
4. **UPDATE ISSUE**: Run ``python .agents/skills/github-task-workflow/scripts/orchestrate.py finish``

## Task File Format

Task files are markdown files in ``tasks/`` directory:
- First line (without ``# ``) = Issue title
- Full content = Issue body
"@
        Set-Content -Path $kimiMdPath -Value $kimiContent -Encoding UTF8
        Write-Success "  [OK]   Created: .kimi/KIMI.md"
    }
    else {
        Write-Warning "  [SKIP] .kimi/KIMI.md already exists"
    }

    # Create tasks directory
    $tasksDir = Join-Path $PWD "tasks"
    if (-not (Test-Path $tasksDir)) {
        New-Item -ItemType Directory -Path $tasksDir -Force | Out-Null
        Write-Success "  [OK]   Created: tasks/"
    }
    else {
        Write-Warning "  [SKIP] tasks/ already exists"
    }
}

# Main function
function Main {
    # List folders if requested
    if ($ListFolders) {
        Show-Folders
        exit 0
    }

    # List skills if requested
    if ($List) {
        Show-Skills -TargetFolder $Folder
        exit 0
    }

    # Validate install mode
    if (-not $System -and -not $Project) {
        Write-Error "Error: Must specify -System or -Project"
        Write-Host ""
        Write-Host "Usage:"
        Write-Host "  .\install.ps1 -System -All                    # Install all skills to system"
        Write-Host "  .\install.ps1 -System -Skills 'skill1','skill2'  # Install specific skills"
        Write-Host "  .\install.ps1 -Project -All                   # Install all skills to project"
        Write-Host "  .\install.ps1 -List                           # List available skills"
        exit 1
    }

    # Get skills to install
    $skillsToInstall = @()
    if ($All) {
        $skillsToInstall = Get-AvailableSkills -TargetFolder $Folder
        if ($skillsToInstall.Count -eq 0) {
            Write-Error "Error: No skills found"
            exit 1
        }
    }
    elseif ($Skills.Count -gt 0) {
        $skillsToInstall = $Skills
    }
    else {
        Write-Error "Error: No skills specified. Use -All or specify skill names with -Skills."
        Write-Host ""
        Write-Host "Usage:"
        Write-Host "  .\install.ps1 -System -All                    # Install all skills to system"
        Write-Host "  .\install.ps1 -System -Folder fe-skills -All  # Install all fe-skills to system"
        Write-Host "  .\install.ps1 -System -Skills 'skill1','skill2'  # Install specific skills"
        Write-Host "  .\install.ps1 -Project -All                   # Install all skills to current project"
        exit 1
    }

    # Perform installation
    if ($System) {
        Install-System -SkillsToInstall $skillsToInstall
    }
    elseif ($Project) {
        Install-Project -SkillsToInstall $skillsToInstall
    }

    Write-Host ""
    Write-Host "Installed skills:"
    foreach ($skill in $skillsToInstall) {
        Write-Host "  - $(Get-SkillDisplayName $skill)"
    }
}

# Run main function
Main
