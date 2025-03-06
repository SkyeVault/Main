# Rust Testing, Logging, and CI/CD Guide

## Introduction
Testing, logging, and automation are essential in modern Rust development. This guide covers:
- How to write and run tests in Rust.
- How logging works in Rust.
- Continuous Integration (CI) and Continuous Deployment (CD) basics.
- Best practices for project structure and naming conventions.

This guide is designed for absolute beginners!

---

## 1. Testing in Rust
Rust provides a robust framework for writing tests to ensure your code behaves as expected.

### 1.1 Unit Tests
Unit tests verify the functionality of individual components (functions or methods). They are typically written in the same file as the code they’re testing, within a `tests` module annotated with `#[cfg(test)]`.

#### Example:
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_addition() {
        assert_eq!(2 + 2, 4);
    }
}
```

### 1.2 Integration Tests
Integration tests assess how different parts of your project work together. They are placed in the `tests` directory at the root of your project. Each Rust file in this directory is compiled as a separate crate.

#### File Structure:
```
my_project/
├── src/
│   └── lib.rs
└── tests/
    └── integration_test.rs
```

#### Example (`tests/integration_test.rs`):
```rust
extern crate my_project;

#[test]
fn test_integration() {
    assert!(my_project::some_function());
}
```

This structure allows you to test the public API of your library as an external user would.

### 1.3 Documentation Tests
These tests ensure that example code in documentation works correctly.

#### Example:
```rust
/// Adds two numbers.
///
/// # Example
/// ```
/// let sum = my_project::add(2, 2);
/// assert_eq!(sum, 4);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

#### Running Tests:
- Run all tests: `cargo test`
- Run specific test: `cargo test test_name`
- Run integration tests only: `cargo test --test integration_test`

---

## 2. Logging in Rust
Logging helps track what’s happening in a Rust application. The `log` crate provides logging functionality, and `env_logger` is commonly used as a backend.

### 2.1 Setting Up Logging
Add dependencies to `Cargo.toml`:
```toml
[dependencies]
log = "0.4"
env_logger = "0.10"
```

### 2.2 Basic Logging Example
```rust
use log::{info, warn, error};
use env_logger;

fn main() {
    env_logger::init(); // Initialize logging
    info!("This is an info message");
    warn!("This is a warning");
    error!("This is an error");
}
```

#### Logging in Tests
To capture log output during tests, initialize `env_logger` at the start of your tests:
```rust
#[cfg(test)]
mod tests {
    use super::*;
    use log::info;
    use env_logger;

    #[test]
    fn test_logging() {
        let _ = env_logger::builder().is_test(true).try_init();
        info!("This is a log message.");
        assert_eq!(2 + 2, 4);
    }
}
```

The `is_test(true)` configuration ensures that log output is captured and displayed only when tests fail, keeping your test output clean.

---

## 3. Continuous Integration (CI) & Continuous Deployment (CD)
CI/CD automates testing, building, and deploying Rust applications.

### 3.1 What is CI/CD?
- **Continuous Integration (CI):** Every time you push code to your repository, automated tests run to ensure new changes don’t break existing functionality. Services like GitHub Actions, Travis CI, or CircleCI can be configured to run `cargo test` on your project.
- **Continuous Deployment (CD):** Upon successful tests, your application can be automatically deployed to your production environment. This might involve building your project with `cargo build --release` and deploying the binaries to your servers or publishing your crate to `crates.io`.

### 3.2 Setting Up CI with GitHub Actions
GitHub Actions can automate Rust testing.

#### Example CI Workflow (`.github/workflows/ci.yml`):
```yaml
name: Rust CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable
      
      - name: Build project
        run: cargo build --verbose
      
      - name: Run tests
        run: cargo test --verbose
```

### 3.3 Where to Place `.github/workflows/` in Rust Projects

### **Single-Project Repository**
If you have separate repositories for each Rust project, place the `.github/workflows/` folder inside **each project** repository:

```
rust-projects/   # Main folder for all Rust projects (not a Git repository)
├── project-a/   # Individual Rust project
│   ├── .github/
│   │   └── workflows/
│   │       ├── ci.yml
│   ├── src/
│   ├── Cargo.toml
│   └── README.md
├── project-b/   # Another Rust project
│   ├── .github/
│   │   └── workflows/
│   │       ├── ci.yml
│   ├── src/
│   ├── Cargo.toml
│   └── README.md
```
Each project gets its **own CI/CD workflow**, ensuring independent build and test pipelines.

---

## **Monorepo (Multiple Projects in One Repo)**
If you have a **monorepo** (a single GitHub repository containing multiple Rust projects), use **one `.github/workflows/` folder at the root**:

```
my-monorepo/  # One GitHub repo containing multiple Rust projects
├── .github/
│   └── workflows/
│       ├── ci-project-a.yml
│       ├── ci-project-b.yml
├── project-a/
│   ├── src/
│   ├── Cargo.toml
│   └── README.md
├── project-b/
│   ├── src/
│   ├── Cargo.toml
│   └── README.md
```
Your workflow YAML files can check which project changed and run CI/CD for the relevant project.

---

## **Key Takeaways:**
- **Separate repositories**: Each project has its own `.github/workflows/` inside the project folder.
- **Monorepo**: One central `.github/workflows/` at the root of the repository managing all projects.

Choose the structure based on whether your Rust projects are in separate repositories or a single monorepo!
---

## 4. Project Structure and Naming Conventions
A well-organized project structure and consistent naming conventions improve code readability and maintainability.

### 4.1 Project Structure:
```
my_project/
├── Cargo.toml
├── src/
│   ├── main.rs
│   ├── lib.rs
│   └── module.rs
├── tests/
│   └── integration_test.rs
└── benches/
    └── benchmark.rs
```

- **`Cargo.toml`**: Contains metadata about your project and dependencies.
- **`src/main.rs`**: Entry point for binary projects.
- **`src/lib.rs`**: Entry point for library projects.
- **`tests/`**: Contains integration tests.
- **`benches/`**: Contains benchmark tests.

### 4.2 Naming Conventions:
- **Files and Modules:** Use `snake_case` (e.g., `module_name.rs`).
- **Structs and Enums:** Use `CamelCase` (e.g., `struct MyStruct`).
- **Functions and Variables:** Use `snake_case` (e.g., `fn my_function`).

---

## 5. Addressing the "Function Not Found in This Scope" Error
This error message occurs when Rust cannot locate a function. Common causes include:
- **Function Location:** The function is defined in a different module, and you haven’t brought it into scope with a `use` statement.
- **Visibility:** The function is private to its module. In Rust, functions are private by default; prefix them with `pub` to make them public.

#### Example Fix:
```rust
mod my_module {
    pub fn my_function() {}
}

fn main() {
    my_module::my_function();
}
```

---

## Conclusion
By following these practices, you can structure your Rust project effectively, implement reliable tests, maintain clear logs, and establish a robust CI/CD pipeline, all while adhering to Rust’s conventions and best practices.
