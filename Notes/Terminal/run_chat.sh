#!/bin/bash

MODEL="mistral"
SYSTEM_FILE="instructions/system.txt"
CHATLOG_FILE="memory/chatlog.txt"
INPUT_FILE="prompts/input.txt"

# Read system prompt
system_prompt=$(<"$SYSTEM_FILE")

# Grab the last 20 lines of chatlog as context
memory_context=$(tail -n 20 "$CHATLOG_FILE")

# Read user input
user_input=$(<"$INPUT_FILE")

# Construct full prompt
full_prompt="$system_prompt\n\nPrevious conversation:\n$memory_context\n\nLorelei: $user_input\nAssistant:"

# Send request to Ollama and parse response
response=$(curl -s http://localhost:11434/api/generate \
  -d "$(jq -n \
    --arg model "$MODEL" \
    --arg prompt "$full_prompt" \
    --argjson stream false \
    '{model: $model, prompt: $prompt, stream: $stream}')" \
)

reply=$(echo "$response" | jq -r .response)

# Output to terminal
echo -e "\nAssistant: $reply\n"

# Append to memory log
{
  echo -e "Lorelei: $user_input"
  echo -e "Assistant: $reply"
  echo ""
} >> "$CHATLOG_FILE"