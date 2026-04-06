#!/usr/bin/env bash
# Universal skill installer - supports both system-level and project-level installation.
# Usage: ./install-v2.sh [OPTIONS] [SKILL_NAMES...]
#
# Options:
#   --system        Install to system directories (default: ~/.config/agents/skills/)
#   --project       Install to current project directory (./.agents/skills/)
#   --agent <name>  Target specific agent (claude-code, kimi, codex, opencode)
#   --all           Install all skills found in this directory
#   --list          List available skills
#   -h, --help      Show this help message
#
# Examples:
#   ./install-v2.sh --system --all                    # Install all skills to system
#   ./install-v2.sh --system github-task-workflow     # Install specific skill to system
#   ./install-v2.sh --project --all                   # Install all skills to current project
#   ./install-v2.sh --system --agent kimi --all       # Install to kimi directory only

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_MODE=""      # system or project
TARGET_AGENT=""      # specific agent or empty for all
INSTALL_ALL=false
SKILLS_TO_INSTALL=()
LIST_SKILLS=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print usage
usage() {
    sed -n '/^# Usage:/,/^$/p' "$0" | sed 's/^# //'
}

# Parse arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --system)
                INSTALL_MODE="system"
                shift
                ;;
            --project)
                INSTALL_MODE="project"
                shift
                ;;
            --agent)
                TARGET_AGENT="$2"
                shift 2
                ;;
            --all)
                INSTALL_ALL=true
                shift
                ;;
            --list)
                LIST_SKILLS=true
                shift
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            -*)
                echo -e "${RED}Error: Unknown option $1${NC}" >&2
                usage
                exit 1
                ;;
            *)
                SKILLS_TO_INSTALL+=("$1")
                shift
                ;;
        esac
    done
}

# Get list of available skills
get_available_skills() {
    local skills=()
    for dir in "$SCRIPT_DIR"/*/; do
        if [ -d "$dir" ] && [ -f "$dir/SKILL.md" ]; then
            skills+=("$(basename "$dir")")
        fi
    done
    echo "${skills[@]}"
}

# List available skills
list_skills() {
    echo -e "${BLUE}Available skills:${NC}"
    for skill in $(get_available_skills); do
        echo "  - $skill"
    done
}

# Get target directories based on agent
get_system_target_dirs() {
    local dirs=()
    case "$TARGET_AGENT" in
        "")
            # All supported agents
            dirs+=("$HOME/.config/agents/skills")
            dirs+=("$HOME/.claude/skills")
            dirs+=("$HOME/.kimi/skills")
            dirs+=("$HOME/.codex/skills")
            dirs+=("$HOME/.opencode/skills")
            ;;
        claude-code)
            dirs+=("$HOME/.claude/skills")
            ;;
        kimi)
            dirs+=("$HOME/.kimi/skills")
            dirs+=("$HOME/.config/agents/skills")
            ;;
        codex)
            dirs+=("$HOME/.codex/skills")
            ;;
        opencode)
            dirs+=("$HOME/.opencode/skills")
            ;;
        *)
            echo -e "${RED}Error: Unknown agent '$TARGET_AGENT'${NC}" >&2
            echo "Supported agents: claude-code, kimi, codex, opencode" >&2
            exit 1
            ;;
    esac
    echo "${dirs[@]}"
}

# Get project target directories
get_project_target_dirs() {
    local dirs=()
    # Project-level skill directories
    dirs+=("./.agents/skills")
    dirs+=("./.kimi/skills")
    dirs+=("./.claude/skills")
    echo "${dirs[@]}"
}

# Install skill to target directory
install_skill_to_dir() {
    local skill_name="$1"
    local skill_src="$SCRIPT_DIR/$skill_name"
    local target_dir="$2"
    local link_path="$target_dir/$skill_name"
    
    mkdir -p "$target_dir"
    
    if [ -e "$link_path" ] || [ -L "$link_path" ]; then
        echo -e "${YELLOW}  [SKIP]${NC} $skill_name already exists at $link_path"
        return 1
    fi
    
    ln -s "$skill_src" "$link_path"
    echo -e "${GREEN}  [OK]${NC}   $skill_name -> $link_path"
    return 0
}

# System-level installation
install_system() {
    echo -e "${BLUE}Installing skills to system directories...${NC}"
    
    local target_dirs=($(get_system_target_dirs))
    local installed_count=0
    local skipped_count=0
    
    for skill_name in "${SKILLS_TO_INSTALL[@]}"; do
        echo ""
        echo "Installing: $skill_name"
        
        local skill_src="$SCRIPT_DIR/$skill_name"
        if [ ! -d "$skill_src" ] || [ ! -f "$skill_src/SKILL.md" ]; then
            echo -e "${RED}  [ERROR] Skill not found: $skill_name${NC}"
            continue
        fi
        
        local skill_installed=false
        for target_dir in "${target_dirs[@]}"; do
            if install_skill_to_dir "$skill_name" "$target_dir"; then
                skill_installed=true
            else
                ((skipped_count++)) || true
            fi
        done
        
        if $skill_installed; then
            ((installed_count++)) || true
        fi
    done
    
    echo ""
    echo -e "${GREEN}System installation complete.${NC}"
    echo "  Installed: $installed_count skill(s)"
    echo "  Skipped: $skipped_count existing link(s)"
}

# Project-level installation
install_project() {
    echo -e "${BLUE}Installing skills to project directories...${NC}"
    
    # Check if we're in a git repository
    if [ ! -d ".git" ]; then
        echo -e "${YELLOW}Warning: Current directory is not a git repository.${NC}"
        read -p "Continue anyway? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
    
    local target_dirs=($(get_project_target_dirs))
    local installed_count=0
    local skipped_count=0
    
    for skill_name in "${SKILLS_TO_INSTALL[@]}"; do
        echo ""
        echo "Installing: $skill_name"
        
        local skill_src="$SCRIPT_DIR/$skill_name"
        if [ ! -d "$skill_src" ] || [ ! -f "$skill_src/SKILL.md" ]; then
            echo -e "${RED}  [ERROR] Skill not found: $skill_name${NC}"
            continue
        fi
        
        local skill_installed=false
        for target_dir in "${target_dirs[@]}"; do
            if install_skill_to_dir "$skill_name" "$target_dir"; then
                skill_installed=true
            else
                ((skipped_count++)) || true
            fi
        done
        
        if $skill_installed; then
            ((installed_count++)) || true
        fi
    done
    
    # Also copy agent config files if they exist
    setup_project_config
    
    echo ""
    echo -e "${GREEN}Project installation complete.${NC}"
    echo "  Installed: $installed_count skill(s)"
    echo "  Skipped: $skipped_count existing link(s)"
}

# Setup project-level configuration
setup_project_config() {
    echo ""
    echo -e "${BLUE}Setting up project configuration...${NC}"
    
    # Create .kimi/KIMI.md if not exists
    if [ ! -f ".kimi/KIMI.md" ]; then
        mkdir -p .kimi
        cat > .kimi/KIMI.md <<'EOF'
# Kimi CLI - Project Instructions

This project uses GitHub Task Workflow for task execution.

## Auto-Workflow Trigger

When the user asks you to "execute", "run", "implement", or "work on" a task file (e.g., `tasks/*.md`), you **MUST** follow the **GitHub Task Workflow** defined in `.agents/skills/github-task-workflow/SKILL.md`.

### Workflow Steps

1. **READ**: Read the task file
2. **CREATE ISSUE**: Run `python .agents/skills/github-task-workflow/scripts/orchestrate.py init <task-file>`
3. **IMPLEMENT**: Execute the task
4. **UPDATE ISSUE**: Run `python .agents/skills/github-task-workflow/scripts/orchestrate.py finish`

## Task File Format

Task files are markdown files in `tasks/` directory:
- First line (without `# `) = Issue title
- Full content = Issue body
EOF
        echo -e "${GREEN}  [OK]${NC}   Created: .kimi/KIMI.md"
    else
        echo -e "${YELLOW}  [SKIP]${NC} .kimi/KIMI.md already exists"
    fi
    
    # Create tasks directory
    if [ ! -d "tasks" ]; then
        mkdir -p tasks
        echo -e "${GREEN}  [OK]${NC}   Created: tasks/"
    else
        echo -e "${YELLOW}  [SKIP]${NC} tasks/ already exists"
    fi
}

# Main function
main() {
    parse_args "$@"
    
    # List skills if requested
    if $LIST_SKILLS; then
        list_skills
        exit 0
    fi
    
    # Validate install mode
    if [ -z "$INSTALL_MODE" ]; then
        echo -e "${RED}Error: Must specify --system or --project${NC}" >&2
        usage
        exit 1
    fi
    
    # Get skills to install
    if $INSTALL_ALL; then
        SKILLS_TO_INSTALL=($(get_available_skills))
        if [ ${#SKILLS_TO_INSTALL[@]} -eq 0 ]; then
            echo -e "${RED}Error: No skills found in $SCRIPT_DIR${NC}" >&2
            exit 1
        fi
    elif [ ${#SKILLS_TO_INSTALL[@]} -eq 0 ]; then
        echo -e "${RED}Error: No skills specified. Use --all or specify skill names.${NC}" >&2
        usage
        exit 1
    fi
    
    # Perform installation
    case "$INSTALL_MODE" in
        system)
            install_system
            ;;
        project)
            install_project
            ;;
    esac
    
    echo ""
    echo "Installed skills:"
    for skill in "${SKILLS_TO_INSTALL[@]}"; do
        echo "  - $skill"
    done
}

main "$@"
