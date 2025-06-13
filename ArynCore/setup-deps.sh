#!/bin/bash

# Enable universe repository for extra packages
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update

# Install development dependencies
sudo apt install -y \
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
  libglib2.0-bin \
  libgobject-2.0-dev \
  pkg-config \
  libayatana-appindicator3-dev \
  librsvg2-dev \
  libwebkit2gtk-4.1-dev || true
