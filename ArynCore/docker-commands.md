# ArynCore Docker Stack – Usage Cheat Sheet

This stack contains multiple AI and automation tools running locally via Docker. Use this reference to interact with each service.

---

## Container Overview

| Tool              | Port             | Interface         | Description                        |
|------------------|------------------|-------------------|------------------------------------|
| Ollama           | 11434            | REST API / CLI    | Run local LLMs (e.g. LLaMA 3)      |
| Stable Diffusion | 7860             | Web UI            | Generate art using prompts         |
| Tortoise TTS     | 5005 (default)   | CLI / REST        | Text-to-speech with cloned voices |
| Whisper          | -                | CLI               | Audio-to-text transcription        |
| n8n              | 5678 (default)   | Web UI            | Automation workflows               |
| pgAdmin          | 5050             | Web UI            | Manage PostgreSQL visually         |
| PostgreSQL       | 5432             | -                 | Used by n8n and pgAdmin            |

---

## Ollama (Local LLMs)

List installed models:
```bash
docker exec -it docker-ollama-1 ollama list
```

Run a model:
```bash
docker exec -it docker-ollama-1 ollama run llama3
```

Use curl to send a prompt:
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Write a bedtime story about Ember and a dragon."
}'
```

---

## Stable Diffusion (AUTOMATIC1111)

Open the Web UI:
http://localhost:7860

View container logs:
```bash
docker logs -f docker-stable-diffusion-1
```

---

## Tortoise TTS

Shell into container:
```bash
docker exec -it docker-tortoise-tts-1 /bin/bash
```

Example TTS command:
```bash
python3 tortoise/do_tts.py --text "Hello Ember" --voice yourvoice
```

You must prepare your voices and scripts ahead of time. Set up the `/data` folder on the host at `../docker/tortoise`.

---

## Whisper (Audio Transcription)

Place audio files in:
```
../docker/audio/
```

Run transcription:
```bash
docker exec -it docker-whisper-1 bash
whisper /audio/yourfile.wav --model base
```

---

## n8n (No-Code Automation)

Open Web UI:
http://localhost:5678

Use it to:
- Build automations
- Connect APIs (Ollama, Whisper, SD, etc.)
- Schedule tasks
- Store results in PostgreSQL

---

## pgAdmin (PostgreSQL)

Open Web UI:
http://localhost:5050

Login:
- Email: admin@foundry.local
- Password: admin123

Connect to:
- Host: postgres
- Database: n8n_db
- User: n8n_user
- Password: strongpassword

---

## Helpful Docker Commands

List running containers:
```bash
docker ps
```

Restart a specific service:
```bash
docker restart docker-ollama-1
```

View logs:
```bash
docker logs -f docker-n8n-1
```

Enter a container shell:
```bash
docker exec -it <container-name> /bin/bash
```

---

## Volumes and Host Paths

Make sure these directories exist on the host:

- `../docker/audio` for Whisper input files
- `../docker/tortoise` for TTS models and output
- `../docker/sd` for Stable Diffusion images
- `../docker/ollama` for Ollama model storage

---

## To-Do

- [ ] Automate startup scripts
- [ ] Add a simple dashboard to switch between tools
- [ ] Schedule PostgreSQL backups
- [ ] Create example n8n workflows for automation

---

Note: `version: "3.8"` is deprecated in Docker Compose. You may remove or ignore that line in `docker-compose.yml`.
