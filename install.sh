#!/bin/bash

echo "------------------------------------------------"
echo "  TAMO INTELLIGENCE SQUAD - INSTALLER v1.0.0"
echo "------------------------------------------------"

# 1. Environment Setup
echo "> Initializing TAMO Kernel..."
python3 -m venv .venv
source .venv/bin/activate
pip install rich requests exa-py firecrawl-py python-dotenv --quiet

# 2. Alias Configuration
echo "> Injecting TAMO Alias..."
if [[ "$SHELL" == */zsh ]]; then
    PROFILE="$HOME/.zshrc"
elif [[ "$SHELL" == */bash ]]; then
    PROFILE="$HOME/.bash_profile"
else
    PROFILE="$HOME/.profile"
fi

TAMO_PATH=$(pwd)
echo "alias tamo='python3 $TAMO_PATH/kernel/cli.py'" >> "$PROFILE"

# 3. Finalizing
echo "------------------------------------------------"
echo "  INSTALLATION COMPLETE"
echo "  Type 'tamo' to start the engine."
echo "------------------------------------------------"
