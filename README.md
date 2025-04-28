# Main Repository

[![Rust CI](https://github.com/SkyeVault/Main/actions/workflows/ci.yml/badge.svg)](https://github.com/SkyeVault/Main/actions/workflows/ci.yml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/8cbde920-cd5b-4822-bfce-4a41dc7e7e70/deploy-status)](https://app.netlify.com/sites/rainkeep/deploys)

# Overview

This is the technical portfolio and development hub for Lorelei Noble. Projects include a 3D sandbox using Three.js, decentralized infrastructure, blockchain development, security automation, and Rust-based tooling.

This repository supports:
- Arynwood.com — a terminal-styled hub for projects and technical logs
- SkyeVault Ops — cloud and contract security research
- On-Chain Metaverse — a 2D and 3D open metaverse experiment using decentralized storage and Ethereum-compatible contracts
- Genesis — an NFT collection deployed to the Polygon testnet and stored on IPFS

---

## Directory Overview

```
Blockchain/         # Smart contracts, metaverse, NFT systems
Notes/              # Personal knowledge base (AWS, Web3, Rust, etc.)
Rust_Projects/      # Rust-based CLI tools and creative automation
lib/                # OpenZeppelin contracts (referenced locally)
rainkeep/           # Source for Arynwood devlog system (Astro)
security/           # AWS security labs, firewall configs, SkyeVault Ops
README.md           # This file
```

---

## Devlog Engine (rainkeep)

The rainkeep folder contains the custom blog system that powers [arynwood.com](https://arynwood.com). It is built using Astro and styled with a minimalist terminal-inspired aesthetic.

- Blog posts are written in standalone HTML files
- Currently building a 3d art gallery using Three.js at rainkeep/public/gallery3d
- New chatbot feature can be tested at arynwood.com/robot
- The site is deployed via Netlify
- Source: `rainkeep/src/pages/blog/` and `rainkeep/static/blog-html/`

---

## Featured Project: Original NFT Collection: Lorelei Noble Genesis

- Hand-drawn original artwork converted into a NFT collection
- Custom smart contract written in Solidity and deployed with Foundry (Rust)
- Deployed to: Polygon Amoy Testnet (proof of concept)
- Smart Contract Address: 0x1C5ec3De32C1cA8e1da93A99c176fa0eF2711783  
- Hosted on IPFS: bafybeihdo27nu3iak7njllgpkmx3ra27mbazlrr444t4sdp46z3sn2v5ye  
- OpenSea (Testnet): https://testnets.opensea.io/assets/amoy/0x1C5ec3De32C1cA8e1da93A99c176fa0eF2711783/

---

## Technologies in Use

### Blockchain and Web3
- Three.js
- Foundry and Solidity
- IPFS, Web3.Storage
- Polygon Amoy Testnet
- Smart contract security best practices

### Rust Tooling
- CLI tools and scripting
- Spotify Playlist Maker (published crate)
- High-performance logic and automation

### Cloud Security and Infrastructure
- AWS IAM, GuardDuty, CloudTrail, WAF
- Terraform and CloudFormation
- GitHub Actions for CI/CD pipelines

---

## Current Testing and Build Status
### Rust CI Workflow
[![Rust CI](https://github.com/SkyeVault/Main/actions/workflows/ci.yml/badge.svg)](https://github.com/SkyeVault/Main/actions/workflows/ci.yml)

- **Latest Tests:** [GitHub Actions](https://github.com/SkyeVault/Main/actions)
- **Build Status:** Check the badge above for the latest result

---

## My Published Crate: Spotify Playlist Maker

[![Crates.io](https://img.shields.io/crates/v/spotify_playlist_maker)](https://crates.io/crates/spotify_playlist_maker)
![Crates.io](https://img.shields.io/crates/d/spotify_playlist_maker)
![Crates.io](https://img.shields.io/crates/l/spotify_playlist_maker)
[![Docs.rs](https://docs.rs/spotify_playlist_maker/badge.svg)](https://docs.rs/spotify_playlist_maker)

### Overview
Spotify Playlist Maker is a Rust package for automating the creation and management of Spotify playlists.

### View the Package
- [Spotify Playlist Maker on Crates.io](https://crates.io/crates/spotify_playlist_maker)
- [Documentation on Docs.rs](https://docs.rs/spotify_playlist_maker)
  
---

## Development Goals

- Expand open-source metaverse and contract transparency projects
- Harden smart contracts with audit-style documentation
- Complete on-chain governance and token logic prototypes
- Develop visual UI for 2D and 3D metaverse layers

---

## My Journey
I started in web design and graphic arts before shifting my focus to Web3, cloud security, and Rust development.  
My goal is to build expertise in:
- Blockchain Development
- Infrastructure automation
- Scalable security architecture
  
![GitHub Streak](https://streak-stats.demolab.com/?user=skyevault&theme=dark)

---

## Connect and Collaborate
Interested in blockchain development, cloud security, automation, or full-stack applications?  
Feel free to check out my repositories and reach out.

- GitHub: [SkyeVault](https://github.com/skyevault)
- Site: [arynwood.com](https://arynwood.com)
- LinkedIn: [Lorelei Noble](https://www.linkedin.com/in/lorelein/)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

![Rust](https://img.shields.io/badge/Rust-Language-brown?style=flat-square&logo=rust)
![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat-square&logo=github)
