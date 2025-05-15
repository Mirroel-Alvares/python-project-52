#!/usr/bin/env bash
set -e

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
#export PATH="$HOME/.local/bin:$PATH"


make install && make collectstatic && make migrate
