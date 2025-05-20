#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv venv -p python3.11
source .venv/bin/activate
source $HOME/.local/bin/env

make install && make migrations && make migrate
