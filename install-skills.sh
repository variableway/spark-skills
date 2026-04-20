#!/usr/bin/env bash
# Install project skills to the user's agents skills directory.
# Usage: ./scripts/install-skills.sh [source-dir] [target-dir]
# Default source: .agents/skills/ or .claude/skills/
# Default target: ~/.config/agents/skills/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SOURCE_DIR="${1:-}"
TARGET_DIR="${2:-$HOME/.config/agents/skills}"

# Auto-detect source directory if not provided
if [[ -z "$SOURCE_DIR" ]]; then
    if [[ -d "$PROJECT_ROOT/.agents/skills" ]]; then
        SOURCE_DIR="$PROJECT_ROOT/.agents/skills"
    elif [[ -d "$PROJECT_ROOT/.claude/skills" ]]; then
        SOURCE_DIR="$PROJECT_ROOT/.claude/skills"
    else
        echo "Error: No skills directory found. Expected .agents/skills/ or .claude/skills/" >&2
        exit 1
    fi
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
    echo "Error: Source directory not found: $SOURCE_DIR" >&2
    exit 1
fi

# Create target directory if needed
mkdir -p "$TARGET_DIR"

echo "Installing skills from $SOURCE_DIR to $TARGET_DIR"

# Install each skill directory
installed_count=0
for skill_path in "$SOURCE_DIR"/*/; do
    # Skip if not a directory
    [[ -d "$skill_path" ]] || continue

    skill_name="$(basename "$skill_path")"
    target_skill_path="$TARGET_DIR/$skill_name"

    # Check if it's a valid skill (has SKILL.md)
    if [[ ! -f "$skill_path/SKILL.md" ]]; then
        echo "  ⚠️  Skipping '$skill_name' (no SKILL.md)"
        continue
    fi

    if [[ -d "$target_skill_path" ]]; then
        echo "  🔄 Updating '$skill_name'"
        rm -rf "$target_skill_path"
    else
        echo "  📦 Installing '$skill_name'"
    fi

    cp -r "$skill_path" "$target_skill_path"
    ((installed_count++)) || true
done

echo ""
echo "Done. $installed_count skill(s) installed to $TARGET_DIR"
