#!/bin/bash -e
# Build script for LSCode.me web version

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$SCRIPT_DIR"

echo "🔨 Building HTML site..."

# Setup virtual environment if needed
if [ ! -d "$ROOT_DIR/.venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$ROOT_DIR/.venv"
fi

# Activate venv
source "$ROOT_DIR/.venv/bin/activate"

# Check for Python dependencies
if ! "$ROOT_DIR/.venv/bin/python3" -c "import markdown" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    "$ROOT_DIR/.venv/bin/pip" install markdown jinja2
fi

# Run the converter
"$ROOT_DIR/.venv/bin/python3" converter.py

echo "✅ HTML build complete!"
