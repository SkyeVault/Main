# The “Impenetrable VPS”  A Step-by-Step Markdown Guide

**Impenetrable VPS Case Study**: hardened Ubuntu server, IPv6, Caddy TLS, Ollama (LLMs), n8n (automations), and Prometheus/Grafana (observability). Optional: self-hosted email.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [VPS Bootstrap & Hardening](#2-vps-bootstrap--hardening)
3. [DNS & TLS](#3-dns--tls)
4. [Core Stack (Caddy + Ollama + n8n + Prometheus/Grafana)](#4-core-stack-caddy--ollama--n8n--prometheusgrafana)

   * [Compose files](#compose-files)
   * [Bring it up](#bring-it-up)
5. [Email (Optional, with Mailu)](#5-email-optional-with-mailu)
6. [Your Demo Automation (End-to-End)](#6-your-demo-automation-end-to-end)
7. [Portfolio Landing Page](#7-portfolio-landing-page)
8. [Final Checks (The Proof)](#8-final-checks-the-proof)
9. [Common Gotchas & Quick Fixes](#9-common-gotchas--quick-fixes)
10. [Deliverables to Showcase](#10-deliverables-to-showcase)

---

## 1) Prerequisites

* **Provider**: Hetzner / DigitalOcean / Linode.

  * OS: Ubuntu 22.04 or 24.04
  * Size: 2 vCPU, 4–8 GB RAM
* **Domain**: register a clean dev domain (e.g., `yourbrand.dev`).
* **Email path** (choose one):

  * **Mailu** (Docker; fast and repeatable) — covered below
  * **Postfix + Dovecot** (manual; more craft, more time)

---

## 2) VPS Bootstrap & Hardening

SSH to the VPS with your provider’s default user or root, then:

```bash
# Create admin and lock down SSH
adduser admin && usermod -aG sudo admin
mkdir -p /home/admin/.ssh && chmod 700 /home/admin/.ssh
echo "<YOUR_SSH_PUBLIC_KEY>" >> /home/admin/.ssh/authorized_keys
chmod 600 /home/admin/.ssh/authorized_keys && chown -R admin:admin /home/admin/.ssh

# Harden sshd: no root login, no passwords
sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart ssh

# Base secure packages & Docker
apt update && apt -y upgrade
apt install -y ufw fail2ban unattended-upgrades curl git docker.io docker-compose-plugin ca-certificates gnupg

# Firewall
ufw default deny incoming && ufw default allow outgoing
ufw allow OpenSSH
ufw allow 80,443/tcp
ufw enable

# Auto security updates
dpkg-reconfigure --priority=low unattended-upgrades
```

> Optional: configure Fail2ban (`/etc/fail2ban/jail.local`) and enable with `systemctl enable --now fail2ban`.

---

## 3) DNS & TLS

At your domain registrar, create these **DNS** records (replace `yourdomain.tld`):

| Type | Host      | Value                                           |
| ---- | --------- | ----------------------------------------------- |
| A    | `@`       | VPS IPv4                                        |
| AAAA | `@`       | VPS IPv6                                        |
| A    | `ollama`  | VPS IPv4                                        |
| AAAA | `ollama`  | VPS IPv6                                        |
| A    | `n8n`     | VPS IPv4                                        |
| AAAA | `n8n`     | VPS IPv6                                        |
| A    | `grafana` | VPS IPv4                                        |
| AAAA | `grafana` | VPS IPv6                                        |
| MX   | `@`       | `10 mail.yourdomain.tld` (if self-hosting mail) |
| TXT  | `@`       | `v=spf1 mx a ~all` (tune later)                 |

**TLS** will be handled automatically by **Caddy** via Let’s Encrypt.

---

## 4) Core Stack (Caddy + Ollama + n8n + Prometheus/Grafana)

Create a project directory:

```bash
sudo mkdir -p /opt/forge && sudo chown -R admin:admin /opt/forge
cd /opt/forge
```

### Compose files

**`docker-compose.yml`**

```yaml
version: "3.9"

networks:
  web:

volumes:
  caddy_data:
  caddy_config:
  ollama_models:
  n8n_data:
  grafana_data:
  prometheus_data:

services:
  caddy:
    image: caddy:2
    restart: unless-stopped
    networks: [web]
    ports: ["80:80", "443:443"]
    volumes:
      - caddy_data:/data
      - caddy_config:/config
      - ./Caddyfile:/etc/caddy/Caddyfile:ro

  ollama:
    image: ollama/ollama:latest
    restart: unless-stopped
    networks: [web]
    environment:
      - OLLAMA_HOST=0.0.0.0
    volumes:
      - ollama_models:/root/.ollama

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    networks: [web]
    environment:
      - N8N_HOST=n8n.yourdomain.tld
      - N8N_PROTOCOL=https
      - N8N_PORT=443
      - GENERIC_TIMEZONE=UTC
    volumes:
      - n8n_data:/home/node/.n8n

  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    networks: [web]
    command: ["--config.file=/etc/prometheus/prometheus.yml"]
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus

  node_exporter:
    image: prom/node-exporter:latest
    restart: unless-stopped
    networks: [web]

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    restart: unless-stopped
    networks: [web]
    privileged: true
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro

  grafana:
    image: grafana/grafana-oss:latest
    restart: unless-stopped
    networks: [web]
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=change-me
    volumes:
      - grafana_data:/var/lib/grafana
```

**`Caddyfile`**

```
# Root site (portfolio)
yourdomain.tld {
  root * /opt/forge/site
  file_server
}

# OLLAMA
ollama.yourdomain.tld {
  reverse_proxy ollama:11434
}

# n8n
n8n.yourdomain.tld {
  reverse_proxy n8n:5678
}

# grafana
grafana.yourdomain.tld {
  reverse_proxy grafana:3000
}
```

**`prometheus.yml`**

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['node_exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
```

### Bring it up

```bash
docker compose pull
docker compose up -d
```

**Smoke tests**

* `https://ollama.yourdomain.tld/api/tags`
* `https://n8n.yourdomain.tld/` (first-run setup)
* `https://grafana.yourdomain.tld/` (login admin / `change-me`)

**Pull a couple models**

```bash
docker exec -it $(docker ps -qf name=ollama) bash -lc \
  'ollama pull mistral:latest && ollama pull llama3:8b-instruct'
```

---

## 5) Email (Optional, with Mailu)

If you want a legit self-hosted mail setup (impressive in a portfolio):

```bash
mkdir -p /opt/mailu && cd /opt/mailu
curl -s https://setup.mailu.io/1.9/compose/ > docker-compose.yml
# Edit generated env/config files (domain, secrets, admin user); bring up with:
docker compose up -d
```

**Add or verify DNS**:

* `MX @ -> mail.yourdomain.tld`
* A/AAAA for `mail.yourdomain.tld`
* SPF TXT: `v=spf1 mx a ~all`
* **DKIM** TXT from Mailu (`mail._domainkey`)
* **DMARC** TXT `_dmarc`: `v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.tld`

> Prefer a faster path? Use a hosted mailbox provider and keep SPF/DKIM/DMARC clean. For the “I can do it” portfolio piece, Mailu is perfect.

---

## 6) Your Demo Automation (End-to-End)

Goal: **Webhook → n8n → Ollama → JSON response**.

In **n8n**:

1. **Webhook** node

   * Method: `POST`
   * Path: `/summarize`
2. **HTTP Request** node → POST to `https://ollama.yourdomain.tld/api/generate`

   * JSON body:

     ```json
     {
       "model": "mistral:latest",
       "prompt": "Summarize:\n{{$json.body.text}}",
       "stream": false
     }
     ```
3. **Respond to Webhook** with the Ollama payload (e.g., `{{$json.response}}`).

**Test it**

```bash
curl -X POST https://n8n.yourdomain.tld/webhook/summarize \
  -H 'Content-Type: application/json' \
  -d '{"text":"Paste any long text here..."}'
```

**Ideas for v2**

* Email in (IMAP) → Whisper (transcribe) → Ollama (summarize) → Email out
* Git webhook → build/test → Slack/Matrix notify
* DNS drift check (dig baseline) → alert

---

## 7) Portfolio Landing Page

Create a tiny site to explain what you built.

**`/opt/forge/site/index.html`**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Impenetrable VPS — Your Name</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Inter,sans-serif;line-height:1.6;max-width:820px;margin:48px auto;padding:0 16px;color:#111}
    code,pre{background:#f6f8fa;border-radius:8px;padding:2px 6px}
    header{margin-bottom:32px}
    .pill{display:inline-block;padding:4px 10px;border:1px solid #eaecef;border-radius:999px;margin-right:8px}
    .grid{display:grid;gap:12px}
  </style>
</head>
<body>
<header>
  <h1>Impenetrable VPS</h1>
  <p class="grid">
    <span class="pill">IPv6</span>
    <span class="pill">Key-only SSH</span>
    <span class="pill">Caddy TLS</span>
    <span class="pill">Dockerized AI</span>
    <span class="pill">Monitoring</span>
    <span class="pill">Mail (optional)</span>
  </p>
</header>

<h2>What I built</h2>
<p>Hardened Ubuntu VPS with Caddy TLS, Ollama (LLMs), n8n (automations), Prometheus + Grafana (observability), and optional Mailu for SPF/DKIM/DMARC-signed mail.</p>

<h2>Why it matters</h2>
<ul>
  <li>Secure by default: key-only SSH, fail2ban, firewall, auto-updates</li>
  <li>Production-ready LLM API at <code>ollama.yourdomain.tld</code></li>
  <li>Automations via <code>n8n.yourdomain.tld</code></li>
  <li>Metrics at <code>grafana.yourdomain.tld</code></li>
</ul>

<h2>How I can help you</h2>
<ul>
  <li>Set up a secure VPS for your team (1–3 days)</li>
  <li>Build custom automations &amp; agents</li>
  <li>Documentation + handoff included</li>
</ul>

<p>Contact: <a href="mailto:hello@yourdomain.tld">hello@yourdomain.tld</a></p>
</body>
</html>
```

> The `Caddyfile` already serves this at `yourdomain.tld`. Restart Caddy if needed:

```bash
docker compose restart caddy
```

---

## 8) Final Checks (The Proof)

* **Security**

  * `ufw status`
  * `fail2ban-client status` (if configured)
  * SSH works **only** with keys; root login is disabled
* **TLS**

  * `curl -I https://yourdomain.tld` (200 + valid cert)
* **AI**

  * `curl https://ollama.yourdomain.tld/api/tags` lists models
* **Automation**

  * `POST` to `/webhook/summarize` returns a summary
* **Monitoring**

  * Grafana shows node\_exporter & cAdvisor dashboards
* **Mail (if enabled)**

  * `dig TXT default._domainkey.yourdomain.tld` shows DKIM
  * Test send/receive; in Gmail “Show original” → SPF/DKIM/DMARC = `pass`

---

## 9) Common Gotchas & Quick Fixes

* **80/443 blocked**
  `ufw allow 80,443/tcp` and open provider firewall if applicable.
* **TLS fails**
  Wait for DNS to propagate; confirm A/AAAA point to VPS; check `docker logs -f <caddy-container>`.
* **n8n webhook 404**
  Ensure workflow is **activated**; path matches; `N8N_HOST=n8n.yourdomain.tld`.
* **Ollama unreachable**
  `docker exec -it ollama ... curl localhost:11434/api/tags` to verify inside container.
* **Grafana login**
  Change default password via env var; add Prometheus datasource `http://prometheus:9090`.

---

## 10) Deliverables to Showcase

* Public links:

  * `https://yourdomain.tld` (landing page)
  * `https://n8n.yourdomain.tld` (screenshot, not necessarily public)
  * `https://grafana.yourdomain.tld` (create a read-only viewer)
* Screenshots:

  * UFW + Fail2ban status
  * Grafana dashboards
  * n8n workflow editor
* A repo with:

  * `docker-compose.yml`, `Caddyfile`, `prometheus.yml`
  * `/site/index.html`
  * A concise `README.md` (these steps)

---

### Notes

* Replace placeholders like `yourdomain.tld` and `<YOUR_SSH_PUBLIC_KEY>`.
* For IPv6, ensure your VPS has v6 enabled and you’ve added AAAA records.
* Self-hosting mail is optional; it’s portfolio gold if you include SPF/DKIM/DMARC correctly.

