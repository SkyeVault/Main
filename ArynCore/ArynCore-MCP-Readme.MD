# ArynCore MCP – Modular Control Platform

ArynCore is a modular, sovereign compute and automation framework. It transforms any Linux server or local machine into a secure, intelligent control hub for large language models (LLMs), workflow automations, real-time messaging, GPU/CPU monitoring, and encrypted communication using NKN.

The system supports both centralized web-scale deployment and isolated private edge nodes (HIPAA-ready).

## Overview

ArynCore MCP (Modular Control Platform) is the core of the Arynwood infrastructure project. It connects a network of local and remote machines under one secure control dashboard, powered by:

- Local and remote LLMs (Ollama, Whisper, SDXL)
- Workflow automation via `n8n`
- End-to-end encrypted communication via NKN mesh
- Full HTTPS routing via NGINX reverse proxy
- Real-time monitoring, uptime control, and service restarts
- Clickable GUI desktop interface (planned via Tauri)

## Modes of Operation

ArynCore runs in one of two core modes.

### Doctor.mode — Local Node Setup (HIPAA-Safe)

Doctor.mode deploys the MCP onto a completely private workstation, ideal for medical professionals, researchers, and privacy-critical operators.

#### Features

- No internet required after installation
- Encrypted local storage
- NKN peer-to-peer messaging (optional)
- Auto-installation of:
  - Ollama (Mistral, LLaMA2, etc.)
  - Whisper and Whisper.cpp
  - Stable Diffusion (CPU fallback or GPU)
  - n8n automation workflows
  - Required Python/PIP packages, `apt` libs, and dependencies

#### Security

- Logs are stored locally
- No cloud API calls or telemetry
- Encrypted disk storage (optional LUKS/FUSE layer)

#### Installation

The node installer runs shell-based setup scripts that:
- Detect system architecture
- Install required toolchains
- Configure service ports and permissions
- Add `/usr/bin/aryncore` as a system control tool

### Public.mode — Multi-User Platform and Portal

Public.mode turns your Arynwood-hosted server into a branded platform for AI tools, live dashboards, and multi-user workflows.

#### Structure
```
https://server.arynwood.com       → MCP GUI Dashboard
https://n8n.arynwood.com          → Workflow automation editor
https://ollama.arynwood.com       → API inference access
https://monitor.arynwood.com      → Uptime and system status
https://bots.arynwood.com         → Future GUI for chat and agents
```
#### Role-Based Access

| Role   | Description |
|--------|-------------|
| Admin  | Full access to workflows, system config, secret keys, deployment tools |
| User   | Run pre-built workflows such as sending prompts or transcriptions |
| Guest  | Browse public tools, chat with AI, explore documentation |

#### Use Cases

- AI platform for small teams
- Research and educational hub for automation workflows
- Web-scale orchestration backend for model-driven services

## Core Technologies

| Component      | Stack                                      |
|----------------|--------------------------------------------|
| Automation     | n8n (self-hosted)                          |
| Inference      | Ollama, Whisper, Stable Diffusion XL       |
| Proxy/Routing  | NGINX and Certbot TLS                      |
| Communication  | NKN peer-to-peer mesh                      |
| Monitoring     | Netdata or Uptime Kuma                     |
| GUI            | HTML/JavaScript (Web) and Tauri (Desktop)  |

## Example Workflow

User clicks "Transcribe Audio" in the GUI. This triggers an n8n workflow that processes the file with Whisper, returns the transcript to the interface, and optionally summarizes it using Mistral.

## Directories

| Path                           | Purpose                                  |
|--------------------------------|------------------------------------------|
| `/var/www/html/index.html`     | Web dashboard homepage                   |
| `~/nkn/listener.js`            | NKN listener and node identity           |
| `~/.n8n`                        | Persistent automation workflows          |
| `/etc/nginx/sites-available`   | Reverse proxy domain configurations      |
| `~/doctor-mode/setup.sh`       | One-click HIPAA-safe local installer     |

## Privacy and Security

- All components can run air-gapped
- Secure WebSocket and HTTPS routing
- System designed to be owned and operated solely by the user
- Communication between nodes is encrypted using the NKN tunnel

## Future Plans

- Tauri desktop client with drag-and-run dashboard
- LLM chatbot router with memory and history
- Autonomous agents for workflow generation
- Real-time model benchmarking and evaluation
- Plugin system for GUI integration
- Git-integrated workflow deployment and change tracking

## Project Role

This project is developed and maintained by Lorelei Noble as part of the Arynwood Sovereign Systems Initiative. The mission is to empower artists, engineers, and independent thinkers to reclaim compute power, personal AI, and automation.

## License

This repository and infrastructure design is © Lorelei Noble, licensed under the MIT License unless otherwise stated for included model files or subcomponents.

## Contact

For questions, consulting, or future collaborations, visit [https://server.arynwood.com](https://server.arynwood.com) or use the Arynwood-linked communication channels.