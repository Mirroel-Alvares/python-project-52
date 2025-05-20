#!/usr/bin/env bash
set -e

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH for the current session
export PATH="$HOME/.local/bin:$PATH"

# Verify uv is available
which uv

# Create virtual environment
uv venv -p python3.11
source .venv/bin/activate

# Now run make commands with uv in PATH
make install && make collectstatic && make migrate
