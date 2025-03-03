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

# SkyeVault Ops - Rust Basics: Commands & Program Execution

## Overview
This guide covers **essential Rust commands** for crafting, editing, compiling, and running Rust programs efficiently. Whether you’re just starting or refining your workflow, this provides a structured approach to Rust development.

---

## 1. Creating a New Rust Project

Rust projects are managed using **Cargo**, Rust's package manager and build system.

### **Create a New Project**
```sh
cargo new my_project
cd my_project
```
- This creates a directory `my_project` with:
  - `Cargo.toml` (Project metadata)
  - `src/main.rs` (Main Rust file)

---

## 2. Editing Rust Code

Rust source files are stored in the **`src`** directory. Open `main.rs` in a code editor (e.g., **VS Code**, **Neovim**, or **Nano**) and edit your Rust program.

### **Example Code: Hello, World!**
Edit `src/main.rs`:

```rust
fn main() {
    println!("Welcome to SkyeVault Ops Rust Lab!");
}
```

---

## 3. Running a Rust Program

### **Run the Program (Without Compilation)**
```sh
cargo run
```
- This compiles and executes the program in **debug mode**.
- Use this for quick testing.

### **Compile and Run Separately**
```sh
cargo build
./target/debug/my_project
```
- `cargo build` compiles the project into an executable in `target/debug/`.
- You can run the executable manually.

### **Run in Release Mode (Optimized Performance)**
```sh
cargo build --release
./target/release/my_project
```
- `--release` generates an optimized binary for production.

---

## 4. Formatting & Linting Code

### **Format Code (Rustfmt)**
```sh
cargo fmt
```
- Ensures your code is clean and well-formatted.

### **Lint Code (Clippy)**
```sh
cargo clippy
```
- Analyzes code for best practices and optimizations.

---

## 5. Managing Dependencies

### **Add a New Dependency**
```sh
cargo add crate_name
```
- Example:
  ```sh
  cargo add rand
  ```
- This adds the `rand` crate (random number generator) to `Cargo.toml`.

### **View Dependencies**
```sh
cargo tree
```
- Displays a tree of all dependencies.

---

## 6. Running Tests

### **Write a Test in `src/lib.rs` or `src/main.rs`**
```rust
#[test]
fn test_addition() {
    assert_eq!(2 + 2, 4);
}
```

### **Run Tests**
```sh
cargo test
```
- Runs all test functions in the project.

---

## 7. Debugging Rust Code

### **Print Debugging Information**
Use `dbg!()` for quick debugging:
```rust
fn main() {
    let x = dbg!(5 * 5);
}
```

### **Run with Debug Symbols**
```sh
RUST_BACKTRACE=1 cargo run
```
- Enables **stack traces** when Rust encounters an error.

---

## 8. Building and Running a Rust Script (Without Cargo)

For simple Rust scripts, you can compile them manually.

### **Create a Rust File**
```sh
nano hello.rs
```
Add this code:

```rust
fn main() {
    println!("Hello from Rust!");
}
```

### **Compile Manually**
```sh
rustc hello.rs
./hello
```
- `rustc` compiles Rust code directly.
- Runs without needing `cargo`.

---

## 9. Cleaning Up Build Files

To remove compiled files and free up space:
```sh
cargo clean
```

---

## 10. Next Steps

Now that you have a foundation, explore:
- **Error handling (`Result`, `Option`)**
- **Async programming (`tokio`, `async-std`)**
- **Building CLIs with `structopt`**
- **Concurrency with threads and channels**

For detailed documentation, visit the [Rust Book](https://doc.rust-lang.org/book/).

Happy coding!