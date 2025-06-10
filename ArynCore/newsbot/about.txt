
---

##  NewsBot — Daily News Scraper + Summarizer

NewsBot is a lightweight Python tool that scrapes approved news sites, extracts recent articles, and passes them into a summarizer for a daily digest.

###  Setup Instructions

```bash
# Clone or enter your project folder
cd ~/dev/main/ArynCore/newsbot

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install newspaper3k beautifulsoup4 requests lxml_html_clean
```

---

###  Run the Scraper

```bash
python scrape_news.py
```

This will:

* Scrape article links from pre-approved sources (NPR, BBC, AP, Reuters)
* Download and parse the text
* Output the collected titles and sources

---

###  Summarizer (Optional)

You can plug in a local summarizer model (such as `llama.cpp`, `GPT4All`, or `transformers`) by modifying the `summarize_text()` function inside `scrape_news.py`.

Example (using Hugging Face):

```python
from transformers import pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text[:1024])[0]['summary_text']
```

---

###  Output Digest

To save a daily markdown file, modify `scrape_news.py` to call:

```python
save_digest(articles)
```

This creates a file like `daily_digest_2025-06-10.md` containing all article summaries.

---

###  Automation (Optional)

You can add a `cron` job or `Makefile` to auto-run this daily and generate a summary for your local bot or terminal.

---


