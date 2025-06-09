#!/bin/bash
source "$(dirname "$0")/config.sh"

function query_llm() {
  local prompt="$1"

  curl -s http://localhost:11434/api/generate \
    -d "$(jq -n \
      --arg model "$MODEL" \
      --arg prompt "$prompt" \
      --argjson stream false \
      '{model: $model, prompt: $prompt, stream: $stream}')" \
    | jq -r '.response'
}
