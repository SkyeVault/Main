# BabyForge — Sovereign AI Pipeline for Prompt-to-Video Creation

**BabyForge** is a fully local, open-source creative pipeline for turning art, prompts, or photos into animated, voiced, and published video clips — without using any cloud-based tools or subscriptions. It's designed to support your own art style, narration, and music, with complete control.

---

## Features

- Generate baby-styled or fantasy-style images with **Stable Diffusion**
- Animate them using **AnimateDiff** and **SadTalker**
- Create expressive voiceovers with **Tortoise TTS**
- Merge visuals and audio using **ffmpeg**
- Automate everything using **n8n**
- Track metadata and CID links using **PostgreSQL**
- Mint on Web3 or upload to IPFS using CLI tools

---

## Folder Structure

```bash
babyforge/
├── babyforge_stack.yml               # Docker Compose file
├── scripts/
│   ├── generate_baby_image.sh        # Run SD with LoRA for baby art
│   ├── generate_voice_tortoise.sh    # Generate .wav from script
│   ├── animate_talker.sh             # Use SadTalker to animate face
│   └── render_final_video.sh         # Combine audio + video
├── output/
│   ├── baby.png                      # Output image
│   ├── voice.wav                     # Generated voice
│   ├── anim.mp4                      # Animated face
│   └── final.mp4                     # Final merged video
├── models/
│   └── sd-lora-baby-style/           # LoRA-trained models
└── n8n_workflows/
    └── babyforge_pipeline.json       # n8n automation workflow
```

---

## Getting Started

### 1. Clone and Enter the Project

```bash
git clone https://your-repo-url/babyforge.git
cd babyforge
```

### 2. Launch the Stack

```bash
docker compose -f babyforge_stack.yml up -d
```

---

## Script: Image Generation

```bash
#!/bin/bash
# generate_baby_image.sh

PROMPT="baby version of a stained glass artist in a cathedral"
curl -X POST http://localhost:7860/sdapi/v1/txt2img   -H 'Content-Type: application/json'   -d "{
        \"prompt\": \"${PROMPT}, photorealistic, toddler, cinematic lighting, 9:16\",
        \"steps\": 25,
        \"width\": 512,
        \"height\": 912,
        \"sampler_index\": \"Euler a\"
      }" | jq -r '.images[0]' | base64 -d > output/baby.png
```

---

## Script: Voice Generation with Tortoise TTS

```bash
#!/bin/bash
# generate_voice_tortoise.sh

python3 tortoise/do_tts.py \
  --text "Welcome to my magical stained glass tutorial!" \
  --voice "baby" \
  --output_path output/voice.wav
```

---

## Script: Animate Face with SadTalker

```bash
#!/bin/bash
# animate_talker.sh

python3 sadtalker/inference.py \
  --driven_audio output/voice.wav \
  --source_image output/baby.png \
  --result_dir output/anim \
  --enhancer gfpgan \
  --still_mode \
  --preprocess full
```

---

## Script: Final Merge with FFmpeg

```bash
#!/bin/bash
# render_final_video.sh

ffmpeg -i output/anim/result.mp4 -i output/voice.wav \
  -c:v copy -c:a aac -shortest output/final.mp4
```

---

## Automation (n8n)

Import `babyforge_pipeline.json` in your n8n dashboard:

- **Trigger:** Webhook or schedule
- **Steps:** Each script in order
- **Extras:** Add Telegram alert or upload to IPFS automatically

---

## Roadmap

- Add Ollama + Claude-style prompt agent
- Support custom script generation from LLM
- Support real-time user input from terminal or chat
- Auto-mint final output as NFT or gallery listing

---