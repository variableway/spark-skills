#!/usr/bin/env bash
# Unified skill installer - supports system-level and project-level installation.
# Can select specific folders (like dev/) to install.
#
# Usage: ./install.sh [OPTIONS] [SKILL_NAMES...]
#
# Options:
#   --system              Install to system directories
#   --project             Install to current project directory
#   --folder <name>       Install from specific folder (e.g., dev, frontend)
#   --agent <name>        Target specific agent (claude-code, kimi, codex, opencode)
#   --all                 Install all skills found
#   --list                List available skills
#   --list-folders        List available skill folders
#   -h, --help            Show this help message
#
# Examples:
#   ./install.sh --system --all                      # Install all skills to system
#   ./install.sh --system --folder dev --all         # Install all dev/ skills to system
#   ./install.sh --project github-task-workflow      # Install specific skill to project
#   ./install.sh --system --agent kimi --all         # Install to kimi directory only

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_MODE=""         # system or project
TARGET_FOLDER=""        # specific folder or empty for root
TARGET_AGENT=""         # specific agent or empty for all
INSTALL_ALL=false
LIST_SKILLS=false
LIST_FOLDERS=false
SKILLS_TO_INSTALL=()

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
            --folder)
                TARGET_FOLDER="$2"
                shift 2
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
            --list-folders)
                LIST_FOLDERS=true
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

# Get list of available skill folders
get_available_folders() {
    local folders=()
    for dir in "$SCRIPT_DIR"/*/; do
        if [[ -d "$dir" ]] && [[ -d "$dir"/*/ ]]; then
            # Check if subdirectory contains SKILL.md
            for subdir in "$dir"*/; do
                if [[ -f "$subdir/SKILL.md" ]]; then
                    folders+=("$(basename "$dir")")
                    break
                fi
            done
        fi
    done
    echo "${folders[@]}"
}

# Get list of available skills
# If TARGET_FOLDER is set, only look in that folder
get_available_skills() {
    local skills=()
    local search_dir="$SCRIPT_DIR"

    if [[ -n "$TARGET_FOLDER" ]]; then
        search_dir="$SCRIPT_DIR/$TARGET_FOLDER"
        if [[ ! -d "$search_dir" ]]; then
            echo -e "${RED}Error: Folder not found: $TARGET_FOLDER${NC}" >&2
            exit 1
        fi
    fi

    # Search in target directory
    for dir in "$search_dir"/*/; do
        if [[ -d "$dir" ]] && [[ -f "$dir/SKILL.md" ]]; then
            local skill_name
            if [[ -n "$TARGET_FOLDER" ]]; then
                skill_name="$TARGET_FOLDER/$(basename "$dir")"
            else
                skill_name="$(basename "$dir")"
            fi
            skills+=("$skill_name")
        fi
    done

    echo "${skills[@]}"
}

# List available folders
list_folders() {
    echo -e "${BLUE}Available skill folders:${NC}"
    local folders=($(get_available_folders))
    if [[ ${#folders[@]} -eq 0 ]]; then
        echo "  (none - all skills are in root directory)"
    else
        for folder in "${folders[@]}"; do
            local count=$(find "$SCRIPT_DIR/$folder" -name "SKILL.md" | wc -l)
            echo "  📁 $folder ($count skills)"
        done
    fi
    echo ""
    echo -e "${BLUE}Root directory skills:${NC}"
    local root_skills=()
    for dir in "$SCRIPT_DIR"/*/; do
        if [[ -f "$dir/SKILL.md" ]]; then
            root_skills+=("$(basename "$dir")")
        fi
    done
    if [[ ${#root_skills[@]} -eq 0 ]]; then
        echo "  (none)"
    else
        for skill in "${root_skills[@]}"; do
            echo "  📄 $skill"
        done
    fi
}

# List available skills
list_skills() {
    local skills=($(get_available_skills))

    if [[ -n "$TARGET_FOLDER" ]]; then
        echo -e "${BLUE}Available skills in '$TARGET_FOLDER':${NC}"
    else
        echo -e "${BLUE}Available skills:${NC}"
    fi

    if [[ ${#skills[@]} -eq 0 ]]; then
        echo "  (none found)"
    else
        for skill in "${skills[@]}"; do
            # Get description from SKILL.md
            local skill_path="$SCRIPT_DIR/$skill"
            local desc=$(grep "^description:" "$skill_path/SKILL.md" 2>/dev/null | head -1 | cut -d':' -f2- | cut -c1-50)
            if [[ -n "$desc" ]]; then
                echo "  📄 $skill -$desc..."
            else
                echo "  📄 $skill"
            fi
        done
    fi
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
    dirs+=("./.agents/skills")
    dirs+=("./.kimi/skills")
    dirs+=("./.claude/skills")
    echo "${dirs[@]}"
}

# Get skill source path
get_skill_source() {
    local skill_name="$1"

    # If skill_name contains '/', it's a folder/skill path
    if [[ "$skill_name" == */* ]]; then
        echo "$SCRIPT_DIR/$skill_name"
    else
        # Check in target folder first if specified
        if [[ -n "$TARGET_FOLDER" ]]; then
            if [[ -d "$SCRIPT_DIR/$TARGET_FOLDER/$skill_name" ]] && [[ -f "$SCRIPT_DIR/$TARGET_FOLDER/$skill_name/SKILL.md" ]]; then
                echo "$SCRIPT_DIR/$TARGET_FOLDER/$skill_name"
                return
            fi
        fi
        # Check in root
        if [[ -d "$SCRIPT_DIR/$skill_name" ]] && [[ -f "$SCRIPT_DIR/$skill_name/SKILL.md" ]]; then
            echo "$SCRIPT_DIR/$skill_name"
            return
        fi
        echo ""
    fi
}

# Get skill display name (basename only)
get_skill_display_name() {
    local skill_name="$1"
    basename "$skill_name"
}

# Install skill to target directory
install_skill_to_dir() {
    local skill_name="$1"
    local skill_src="$2"
    local target_dir="$3"
    local display_name=$(get_skill_display_name "$skill_name")
    local link_path="$target_dir/$display_name"

    mkdir -p "$target_dir"

    if [[ -e "$link_path" ]] || [[ -L "$link_path" ]]; then
        echo -e "${YELLOW}  [SKIP]${NC} $display_name already exists"
        return 1
    fi

    ln -s "$skill_src" "$link_path"
    echo -e "${GREEN}  [OK]${NC}   $display_name"
    return 0
}

# System-level installation
install_system() {
    echo -e "${BLUE}Installing skills to system directories...${NC}"

    if [[ -n "$TARGET_FOLDER" ]]; then
        echo -e "${BLUE}Source folder: $TARGET_FOLDER${NC}"
    fi

    local target_dirs=($(get_system_target_dirs))
    local installed_count=0
    local skipped_count=0

    for skill_name in "${SKILLS_TO_INSTALL[@]}"; do
        local skill_src=$(get_skill_source "$skill_name")
        if [[ -z "$skill_src" ]]; then
            echo -e "${RED}  [ERROR] Skill not found: $skill_name${NC}"
            continue
        fi

        local display_name=$(get_skill_display_name "$skill_name")
        echo ""
        echo "Installing: $display_name"

        local skill_installed=false
        for target_dir in "${target_dirs[@]}"; do
            if install_skill_to_dir "$skill_name" "$skill_src" "$target_dir"; then
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

    if [[ -n "$TARGET_FOLDER" ]]; then
        echo -e "${BLUE}Source folder: $TARGET_FOLDER${NC}"
    fi

    # Check if we're in a git repository
    if [[ ! -d ".git" ]]; then
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
        local skill_src=$(get_skill_source "$skill_name")
        if [[ -z "$skill_src" ]]; then
            echo -e "${RED}  [ERROR] Skill not found: $skill_name${NC}"
            continue
        fi

        local display_name=$(get_skill_display_name "$skill_name")
        echo ""
        echo "Installing: $display_name"

        local skill_installed=false
        for target_dir in "${target_dirs[@]}"; do
            if install_skill_to_dir "$skill_name" "$skill_src" "$target_dir"; then
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
    if [[ ! -f ".kimi/KIMI.md" ]]; then
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
    if [[ ! -d "tasks" ]]; then
        mkdir -p tasks
        echo -e "${GREEN}  [OK]${NC}   Created: tasks/"
    else
        echo -e "${YELLOW}  [SKIP]${NC} tasks/ already exists"
    fi
}

# Main function
main() {
    parse_args "$@"

    # List folders if requested
    if $LIST_FOLDERS; then
        list_folders
        exit 0
    fi

    # List skills if requested
    if $LIST_SKILLS; then
        list_skills
        exit 0
    fi

    # Validate install mode
    if [[ -z "$INSTALL_MODE" ]]; then
        echo -e "${RED}Error: Must specify --system or --project${NC}" >&2
        usage
        exit 1
    fi

    # Get skills to install
    if $INSTALL_ALL; then
        SKILLS_TO_INSTALL=($(get_available_skills))
        if [[ ${#SKILLS_TO_INSTALL[@]} -eq 0 ]]; then
            echo -e "${RED}Error: No skills found${NC}" >&2
            exit 1
        fi
    elif [[ ${#SKILLS_TO_INSTALL[@]} -eq 0 ]]; then
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
        echo "  - $(get_skill_display_name "$skill")"
    done
}

main "$@"
