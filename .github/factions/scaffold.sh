#!/bin/bash

# Scaffold script for creating necessary directories and files for Skyrim Campaign Vault

mkdir -p modules factions state npcs

echo "{}" > clocks.json
mkdir -p state
echo "{"campaign_state": {}}" > state/campaign_state.json

echo "Setup scaffold completed."