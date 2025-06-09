#!/bin/bash

source "$(dirname "$0")/config.sh"
source "$(dirname "$0")/engine.sh"
source "$(dirname "$0")/ui.sh"

[[ -f "$SYSTEM_FILE" ]] || { echo "Missing system file."; exit 1; }
[[ -f "$INPUT_FILE" ]] || { echo "Missing input file."; exit 1; }
[[ -f "$CHATLOG_FILE" ]] || touch "$CHATLOG_FILE"

show_header
show_last_turns

USER_INPUT=$(<"$INPUT_FILE")
SYSTEM_PROMPT=$(<"$SYSTEM_FILE")
FULL_PROMPT="$SYSTEM_PROMPT\n\n$USER_INPUT"

RESPONSE=$(query_llm "$FULL_PROMPT")

echo "Assistant: $RESPONSE"
echo "" >> "$CHATLOG_FILE"
echo "You: $USER_INPUT" >> "$CHATLOG_FILE"
echo "Assistant: $RESPONSE" >> "$CHATLOG_FILE"
