cat <<EOF > pull-ollama-models.sh
#!/bin/bash
models=(
  "mistral"
  "codellama:7b"
  "gemma:2b"
  "llama2:7b"
  "orca-mini"
  "phi"
)

for model in "\${models[@]}"; do
  echo "[+] Pulling \$model"
  ollama pull "\$model"
done
EOF

chmod +x pull-ollama-models.sh
./pull-ollama-models.sh
