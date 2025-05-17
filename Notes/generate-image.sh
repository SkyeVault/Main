#!/bin/bash

# Prompt and output setup
PROMPT="a futuristic stained glass forest cathedral, cinematic lighting, 4k"
OUTPUT="output/generated.png"

# Stable Diffusion API endpoint (via webui)
curl -X POST http://localhost:7860/sdapi/v1/txt2img \
  -H 'Content-Type: application/json' \
  -d "{
        \"prompt\": \"${PROMPT}\",
        \"steps\": 25,
        \"cfg_scale\": 7,
        \"width\": 512,
        \"height\": 512,
        \"sampler_index\": \"Euler\"
      }" | jq -r '.images[0]' | base64 -d > "${OUTPUT}"

echo "Image saved to ${OUTPUT}"