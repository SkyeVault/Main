#!/bin/bash

# Absolute base path
BASE_DIR="$HOME/dev/main/.local-chatbot"

SYSTEM_FILE="$BASE_DIR/instructions/system.txt"
CHATLOG_FILE="$BASE_DIR/memory/chatlog.txt"
INPUT_FILE="$BASE_DIR/prompts/input.txt"

# Check if files exist
if [[ ! -f "$SYSTEM_FILE" ]]; then
  echo "Missing: $SYSTEM_FILE"
  exit 1
fi

if [[ ! -f "$CHATLOG_FILE" ]]; then
  echo "Missing: $CHATLOG_FILE"
  exit 1
fi

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "Missing: $INPUT_FILE"
  exit 1
fi

# Show session start
echo "Assistant:"
echo "-----------"

# Display the latest context
tail -n 10 "$CHATLOG_FILE"

# Read prompt
echo ""
echo "You: "
cat "$INPUT_FILE"

# Append interaction to chatlog (simulated assistant response)
echo "" >> "$CHATLOG_FILE"
echo "You: $(cat "$INPUT_FILE")" >> "$CHATLOG_FILE"
echo "Assistant: (responds here)" >> "$CHATLOG_FILE"
