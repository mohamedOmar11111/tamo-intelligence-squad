#!/bin/bash

echo "------------------------------------------------"
echo "  ONYX INTELLIGENCE SQUAD - INSTALLER v1.0.0"
echo "------------------------------------------------"

# 1. Environment Setup
echo "> Initializing Onyx Kernel..."
python3 -m venv .venv
source .venv/bin/activate
pip install rich requests exa-py firecrawl-py --quiet

# 2. Alias Configuration
echo "> Injecting Onyx Alias..."
if [[ "$SHELL" == */zsh ]]; then
    PROFILE="$HOME/.zshrc"
elif [[ "$SHELL" == */bash ]]; then
    PROFILE="$HOME/.bash_profile"
else
    PROFILE="$HOME/.profile"
fi

ONYX_PATH=$(pwd)
echo "alias onyx='python3 $ONYX_PATH/kernel/cli.py'" >> "$PROFILE"

# 3. Finalizing
echo "------------------------------------------------"
echo "  INSTALLATION COMPLETE"
echo "  Type 'onyx' to start the engine."
echo "------------------------------------------------"
