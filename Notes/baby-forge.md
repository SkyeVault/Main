Thank you for your patience — here is the correct markdown, with all code blocks properly closed using triple backticks. This version is fully copy-pasteable into a .md file or GitHub and will render without errors.

⸻

BabyForge — Open Source Mad Talking Baby Pipeline

Turn your art, photos, or AI portraits into talking baby videos — locally, privately, and with your own creative direction.

100% free, offline-capable, and powered by Stable Diffusion, SadTalker, Tortoise TTS, and n8n.

⸻

Folder Structure

babyforge/
├── docker-compose.yml               # Full local AI pipeline
├── n8n_workflows/
│   └── babyforge_pipeline.json      # n8n flow to control the process
├── scripts/                         # Executable helper scripts
│   ├── generate_baby_image.sh       # Runs SD with baby LoRA or prompt
│   ├── generate_voice_tortoise.sh   # Generates .wav using Tortoise TTS
│   ├── animate_talker.sh            # Runs SadTalker
│   └── render_final_video.sh        # Uses ffmpeg to merge everything
├── output/
│   ├── baby.png                     # Output image
│   ├── voice.wav                    # Generated voice
│   ├── anim.mp4                     # Talking baby video
│   └── final.mp4                    # Final merged video
└── models/
    └── sd-lora-baby-style/          # LoRA trained on baby aesthetic


⸻

Required Docker Services
	•	stable-diffusion-webui (AUTOMATIC1111)
	•	sadtalker (face animation)
	•	tortoise-tts (voice synthesis)
	•	n8n (automation trigger)
	•	optional: ffmpeg (can be host-based)

⸻

Scripts Overview

generate_baby_image.sh

#!/bin/bash
# Generates a baby-style image from a text prompt

PROMPT="baby version of a stained glass artist in cathedral"
curl -X POST http://localhost:7860/sdapi/v1/txt2img \
  -H 'Content-Type: application/json' \
  -d "{
        \"prompt\": \"${PROMPT}, toddler, photorealistic, 9:16, studio lighting\",
        \"steps\": 25,
        \"width\": 512,
        \"height\": 912,
        \"sampler_index\": \"Euler a\"
      }" | jq -r '.images[0]' | base64 -d > output/baby.png


⸻

generate_voice_tortoise.sh

#!/bin/bash
# Requires Tortoise TTS installed locally

python3 tortoise/do_tts.py \
  --text "Welcome to my magical stained glass tutorial!" \
  --voice "baby" \
  --output_path output/voice.wav


⸻

animate_talker.sh

#!/bin/bash
# Uses SadTalker to animate a still image using the generated voice

python3 sadtalker/inference.py \
  --driven_audio output/voice.wav \
  --source_image output/baby.png \
  --result_dir output/anim \
  --enhancer gfpgan \
  --still_mode \
  --preprocess full


⸻

render_final_video.sh

#!/bin/bash
# Uses ffmpeg to merge the animation with the voice audio

ffmpeg -i output/anim/result.mp4 -i output/voice.wav \
  -c:v copy -c:a aac -shortest output/final.mp4


⸻

n8n Integration

Flow: babyforge_pipeline.json

Steps:
	1.	Webhook Trigger: Starts with a prompt or upload
	2.	Execute Command Node: Runs generate_baby_image.sh
	3.	Execute Command Node: Runs generate_voice_tortoise.sh
	4.	Execute Command Node: Runs animate_talker.sh
	5.	Execute Command Node: Runs render_final_video.sh
	6.	(Optional): Upload to IPFS, YouTube, or notify via Telegram

⸻

Let me know if you want this bundled into a GitHub repo template or ready-to-run Docker image next.