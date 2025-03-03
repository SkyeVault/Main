# SkyeVault Ops - Rust Lab Setup

## Overview
This Rust lab is designed to provide a structured foundation for working with Rust in **SkyeVault Ops**, focusing on security, automation, and modern DevOps practices. This guide walks you through installing Rust and setting up essential packages.

---

## 1. Installing Rust

Rust has an official toolchain manager called **rustup**, which simplifies installation and keeps Rust updated. Follow these steps to install Rust on your system:

### **Linux & macOS**
Open a terminal and run:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Follow the on-screen instructions to complete the installation. Once installed, restart your terminal and verify the installation:

```sh
rustc --version
cargo --version
```

### **Windows**
1. Download and install **rustup** from the official site:  
   [https://rustup.rs](https://rustup.rs)
2. Open a terminal (**PowerShell** or **cmd**) and check the installation:

```powershell
rustc --version
cargo --version
```

---

## 2. Configuring Rust

After installing Rust, ensure your environment is set up correctly:

- Add Rust to your system `PATH` if it's not automatically configured:

```sh
source $HOME/.cargo/env
```

- Confirm the installation:

```sh
rustup show
```

To update Rust to the latest version at any time:

```sh
rustup update
```

---

## 3. Installing Required Packages

These are the essential packages for the Rust lab:

### **1. Cargo (Rust’s Package Manager)**
Cargo is installed by default with Rust, but you can verify or update it:

```sh
cargo --version
cargo update
```

### **2. Rust Analyzer (For Better Development)**
Rust Analyzer is a powerful language server for Rust. Install it using:

```sh
rustup component add rust-analyzer
```

If using **VS Code**, install the [Rust Analyzer extension](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer).

### **3. Common Rust Developer Tools**
These tools are useful for formatting, linting, and testing Rust projects.

- **Clippy (Linter for Rust Code)**

```sh
rustup component add clippy
```

Run it inside a project:

```sh
cargo clippy
```

- **Rustfmt (Formatter for Rust Code)**

```sh
rustup component add rustfmt
```

Format a project:

```sh
cargo fmt
```

- **Cargo Watch (Automatically Runs Commands on File Changes)**

```sh
cargo install cargo-watch
```

Example usage:

```sh
cargo watch -x "test"
```

- **Cargo Audit (Scans for Security Vulnerabilities)**

```sh
cargo install cargo-audit
```

Run a security scan:

```sh
cargo audit
```

### **4. Cross (Compile Rust for Other Platforms)**
If you want to build Rust projects for different operating systems, install `cross`:

```sh
cargo install cross
```

---

## 4. Running Your First Rust Program
To test your Rust installation, create a new project:

```sh
cargo new my_rust_lab
cd my_rust_lab
```

Edit `src/main.rs` and replace the contents with:

```rust
fn main() {
    println!("Welcome to SkyeVault Ops Rust Lab!");
}
```

Run the program:

```sh
cargo run
```

You should see:

```
Welcome to SkyeVault Ops Rust Lab!
```

---

## 5. Setting Up a Rust Virtual Environment (Optional)
To manage Rust versions and toolchains per project:

```sh
rustup override set stable
```

To revert to the system’s default Rust version:

```sh
rustup override unset
```

---

## 6. Next Steps
Now that Rust is installed, you can start working on **SkyeVault Ops** projects! Here are some suggested next steps:

- Explore **Rust modules and crates**
- Learn **memory safety concepts**
- Implement **concurrency with async Rust**
- Build **Rust-based security tools**

For any issues, check the [Rust documentation](https://doc.rust-lang.org/book/) or run:

```sh
rustc --explain <error_code>
```

Happy coding!