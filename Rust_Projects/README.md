Rust Project Directory
# **Rust Folder Notes**  

## **Overview**  
This folder contains **Rust projects**, categorized based on functionality, development stage, and purpose. It serves as the main workspace for **software development, security tools, blockchain integrations, and utility scripts**.  

---

## **Folder Structure**  

```
/rust_projects  
 ├── spotify_playlist_maker/      # Published Rust package for playlist automation  
 ├── [New Project Name]/          # Blockchain security and storage tool (formerly NanoVault)  
 ├── rust_developer_toolkit/      # Bash scripts for automating Rust environment setup  
 ├── experiments/                 # Small-scale Rust testing and proof-of-concept projects  
 └── docs/                        # Documentation and guides for Rust-based projects  
```

### **Project Breakdown**  

#### **1. Spotify Playlist Maker**  
- **Status:** Published on crates.io  
- **Purpose:** Automates playlist creation using the Spotify API.  
- **Current Focus:** Fixing package status failure due to `lib.rs` update.  
- **Next Steps:** Expand documentation and add dynamic song selection.  

#### **2. Blockchain Security Tool (New Name TBD)**  
- **Status:** Initial project setup complete.  
- **Purpose:** Secure storage solution using blockchain-based verification.  
- **Current Focus:** Refining setup scripts and reviewing environment configuration.  
- **Next Steps:** Implement blockchain integration (IPFS or Arweave).  

#### **3. Rust Developer Toolkit**  
- **Status:** Active development.  
- **Purpose:** Automates Rust and environment setup for new projects.  
- **Current Focus:** Improving installation scripts and adding Windows compatibility.  
- **Next Steps:** Expand functionality for dependency management.  

#### **4. Experiments Folder**  
- **Purpose:** Temporary space for **testing new Rust concepts, learning, and prototyping**.  
- **Current Focus:** Testing new Rust libraries and frameworks before full implementation.  

#### **5. Docs Folder**  
- **Purpose:** Stores Markdown documentation, API references, and project guides.  
- **Current Focus:** Keeping all **Rust project documentation organized and accessible**.  

---

## **Development Workflow**  

1. **All projects follow the Cargo structure** (`src/`, `Cargo.toml`, `tests/`).  
2. **New ideas and prototypes** start in `experiments/` before becoming full projects.  
3. **Docs are kept in Markdown format** for easy integration with GitHub and local reading.  
4. **Version control is managed via Git**, with feature branches for major updates.  

---

## **Next Steps**  
- **Rename and finalize the blockchain security project** to avoid conflicts.  
- **Fix the failing Spotify Playlist Maker package status**.  
- **Continue refining Rust Developer Toolkit installation scripts**.  

This file provides an **up-to-date reference for organizing and managing Rust projects** within the main development environment.  
