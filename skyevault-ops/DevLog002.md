# **SkyeVault Ops - Dev Log for March 3, 2025**  
### *Rust, APIs, and the Joy of Debugging*  

---

## **Tasks Completed**  

### **1. Terminal & Zsh Workflow Enhancements**  
- **Oh My Zsh + Powerlevel10k:** Customized prompt for clarity and efficiency.  
- **Plugins Installed & Configured:**  
  - `zsh-syntax-highlighting` for improved readability.  
  - `zsh-autosuggestions` for command predictions.  
  - `fzf` for fuzzy searching through files and history.  
  - `autojump` for quick directory navigation.  
- **Optimized Command History:**  
  - Re-mapped `CTRL + R` to search history **without requiring fzf.**  
  - Ensured frequently used commands are surfaced quickly.  
- **Homebrew & Performance Fixes:**  
  - Homebrew is installed at `/usr/local/bin/brew` instead of `/opt/homebrew`.  
  - Identified that Homebrew is slow on macOS 12 but manageable with direct installs.  

### **2. Rust Installation & First Project Setup**  
- Installed **Rust via rustup**, ensuring the correct environment variables were loaded.  
- Verified installation with:  
  ```sh
  rustc --version  
  cargo --version  
  ```
- Created a new Rust project:  
  ```sh
  cargo new skyevault-spotify
  ```
- Explored Rust's package management:  
  ```sh
  cargo add reqwest serde_json tokio
  ```
  *(Adding dependencies efficiently instead of manually updating `Cargo.toml`.)*  

### **3. Spotify Playlist Generator - API Integration**  
- **Authentication Setup:**  
  - Implemented OAuth2 authentication for Spotify.  
  - Generated access token, set up auto-refresh to handle expiration.  
- **Rust Dependencies Used:**  
  - `reqwest` for making API requests.  
  - `serde_json` for parsing Spotify’s JSON responses.  
- **Troubleshooting & Fixes:**  
  - Encountered `reqwest` SSL certificate issues—fixed by ensuring `native-tls` was enabled.  
  - JSON parsing errors due to mismatched struct types—resolved by refining `serde_json` struct definitions.  
  - API request initially returned empty data—fixed by adjusting query parameters to ensure valid results.  
- **Successes:**  
  - Successfully authenticated with Spotify API.  
  - Retrieved playlist data—next step is refining how results are displayed.  

---

## **Git Journal Entry - March 3, 2025**  

### **Detailed Log:**  
Today, I **streamlined my terminal workflow**, ensuring Zsh is set up for peak efficiency. This included improving history search, adding plugins for quick navigation, and optimizing command completion. These small changes make a big difference in workflow speed.  

On the development side, **Rust is fully installed and configured**, and I started my first Rust-based API project: a **Spotify playlist generator.** The main challenge was **handling authentication and structuring API requests in Rust**, but I got it working after some deep dives into `reqwest` and `serde_json`.  

**Troubleshooting highlights:**  
- Adjusted Rust structs to properly handle JSON responses.  
- Resolved SSL issues in `reqwest`.  
- Fixed empty API responses by refining request parameters.  

Overall, **a solid foundation is now in place** for both Rust development and DevOps workflow.  

---

## **Next Steps for Tomorrow:**  
- **Spotify Project:** Improve how playlist data is structured and displayed.  
- **Rust Learning:** Explore error handling and async programming.  
- **Git & DevOps Documentation:** Start drafting SkyeVault Ops README for project transparency.  

---

## **Final Thoughts:**  
Rust’s strict typing and ownership system **force a deeper understanding of code structure**, which makes debugging a rewarding challenge. The **Spotify API project is a great real-world test**, and now that authentication is working, the next steps will focus on data formatting and usability. Looking forward to refining it further!  