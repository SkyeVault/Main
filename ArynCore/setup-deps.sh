# setup-deps.sh
#!/bin/bash
sudo apt update && sudo apt install -y \
  libwebkit2gtk-4.0-dev \
  build-essential \
  curl \
  wget \
  libssl-dev \
  libgtk-3-dev \
  libappindicator3-dev \
  libx11-dev \
  libgdk-pixbuf2.0-dev \
  libpango1.0-dev \
  libatk1.0-dev \
  libglib2.0-dev \
  pkg-config \
  libayatana-appindicator3-dev \
  librsvg2-dev
