
#!/bin/bash

echo "[+] Upgrading to top-tier Ollama models..."

models=(
  # Meta's best
  "llama3:8b-instruct-q4_0"           # Best general-purpose model
  "llama3:8b-q4_0"                    # Base model, quantized

  # Mistral (light + powerful)
  "mistral:7b-instruct-q4_0"

  # Phi-3 (128k context, newer than phi:latest)
  "phi3:mini-128k-instruct-q4_0"

  # Code
  "codellama:7b-instruct-q4_0"

  # Gemma, quantized
  "gemma:2b-instruct-q4_0"

  # Ultra-fast fallback
  "tinyllama:1.1b-chat"
)

for model in "${models[@]}"; do
  echo "[>] Pulling $model"
  ollama pull "$model"
done

echo "[✓] Model upgrade complete."
