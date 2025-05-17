# FoundryForge Sovereign Video Stack

This stack gives you a full, self-hosted video creation pipeline using open-source tools. It includes Stable Diffusion for image generation, AnimateDiff and ComfyUI for animation, Whisper for transcription, and n8n for workflow automation.

---

## Stack Overview

### Core Services (via Docker Compose)

- **Stable Diffusion WebUI**: Image generation from prompts
- **AnimateDiff**: Animation of images into short motion clips
- **ComfyUI**: Modular AI workflow builder for video/image pipelines
- **Ollama**: Local LLM engine for scripting and assistance
- **Whisper**: Transcription (OpenAI voice-to-text)
- **n8n**: Workflow automation for controlling everything
- **PostgreSQL + PGAdmin**: Data storage + web interface for managing it

---

## Directory Layout

```
foundryforge-stack/
├── docker-compose.yml               # Launches entire stack
├── generate_image.sh                # Generates image from prompt
├── animate_image.sh                 # Animates image into short video
├── output/
│   ├── generated.png                # Result from image script
│   └── animation/                   # Result from AnimateDiff
├── n8n_workflow_animate_image.json # Import into n8n to automate the pipeline
```

---

## Setup Instructions

### 1. Install Docker & Docker Compose

```bash
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
```

Log out and back in.

---

### 2. Start the Stack

```bash
cd foundryforge-stack
docker compose up -d
```

---

### 3. Make Scripts Executable

```bash
chmod +x generate_image.sh
chmod +x animate_image.sh
```

---

### 4. Run Manually (Test Flow)

```bash
./generate_image.sh
./animate_image.sh
```

---

### 5. Automate with n8n

1. Open n8n at [http://localhost:5678](http://localhost:5678)
2. Log in with:
   - User: `forge`
   - Pass: `forge123`
3. Import `n8n_workflow_animate_image.json`
4. Activate the workflow
5. Use webhook to trigger:
```bash
curl -X POST http://localhost:5678/webhook/generate-and-animate
```

---

## Coming Next (Optional Enhancements)

- Accept dynamic prompts via webhook form
- Auto-post animations to Telegram or email
- Tag and store animation metadata in PostgreSQL
- Sync assets to IPFS

---

## Notes

This stack assumes all services are running locally and accessible via their default ports. You can update ports in `docker-compose.yml` if needed.

When your Forge machine is back online, you'll be able to run this stack fully, locally, with GPU acceleration and sovereign storage.

