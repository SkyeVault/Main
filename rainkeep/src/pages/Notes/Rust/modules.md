# Understanding Rust Modules: Parents, Children, and Grandchildren

## Introduction
Rust uses **modules** to organize code into smaller, reusable components. This guide explains how **parent**, **child**, and **grandchild** modules work, how to structure them, and how to use them effectively in your projects.

---

## What Are Modules?
Modules in Rust allow you to:
- Encapsulate related functionality.
- Reuse code across different files.
- Control visibility with `pub` (public) and private access.

### Defining Modules
Modules are created using the `mod` keyword. They can be defined:
1. **Inline**: Inside a `.rs` file.
2. **In Separate Files**: Each module in its own file within the `src/` directory.
3. **In Subdirectories**: Using a `mod.rs` file to define child modules.

---

## Basic Module Structure
A structured Rust project with modules looks like this:

```
my_project/
├── src/
│   ├── main.rs         # Binary crate entry point
│   ├── lib.rs          # Library crate entry point
│   ├── parent/
│   │   ├── mod.rs      # Parent module
│   │   ├── child.rs    # Child module
│   │   ├── grandchild.rs  # Grandchild module
├── Cargo.toml
```

---

## Example: Defining Modules in a Project

### `main.rs` (Entry Point)
```rust
mod parent;

fn main() {
    println!("Main function running");
    parent::say_hello();
    parent::child::say_hello();
    parent::child::grandchild::say_hello();
}
```

### `lib.rs` (Library Entry Point)
```rust
pub mod parent;
```

### `parent/mod.rs` (Parent Module)
```rust
pub mod child; // Declare child module

pub fn say_hello() {
    println!("Hello from parent module!");
}
```

### `parent/child.rs` (Child Module)
```rust
pub mod grandchild; // Declare grandchild module

pub fn say_hello() {
    println!("Hello from child module!");
}
```

### `parent/grandchild.rs` (Grandchild Module)
```rust
pub fn say_hello() {
    println!("Hello from grandchild module!");
}
```

---

## Advanced Example: Structs and Functions Across Modules

### `main.rs`
```rust
mod parent;

fn main() {
    let parent_struct = parent::ParentStruct::new("Parent Instance");
    parent_struct.display();

    let child_struct = parent::child::ChildStruct::new("Child Instance");
    child_struct.display();

    let grandchild_struct = parent::child::grandchild::GrandchildStruct::new("Grandchild Instance");
    grandchild_struct.display();
}
```

### `parent/mod.rs`
```rust
pub mod child;

pub struct ParentStruct {
    name: String,
}

impl ParentStruct {
    pub fn new(name: &str) -> Self {
        Self { name: name.to_string() }
    }
    
    pub fn display(&self) {
        println!("ParentStruct: {}", self.name);
    }
}
```

### `parent/child.rs`
```rust
pub mod grandchild;

pub struct ChildStruct {
    name: String,
}

impl ChildStruct {
    pub fn new(name: &str) -> Self {
        Self { name: name.to_string() }
    }
    
    pub fn display(&self) {
        println!("ChildStruct: {}", self.name);
    }
}
```

### `parent/grandchild.rs`
```rust
pub struct GrandchildStruct {
    name: String,
}

impl GrandchildStruct {
    pub fn new(name: &str) -> Self {
        Self { name: name.to_string() }
    }
    
    pub fn display(&self) {
        println!("GrandchildStruct: {}", self.name);
    }
}
```

---

## Key Takeaways
- **Modules help structure Rust projects efficiently.**
- **Use `mod` to declare modules and `pub` to expose them.**
- **Organizing code into parents, children, and grandchildren makes it reusable and maintainable.**
- **Each module can contain structs, functions, and other modules.**
- **Call functions and structs using their fully qualified path: `parent::child::grandchild::function()`.**

---

## Conclusion
Rust modules provide a scalable way to structure applications. Using parent, child, and grandchild modules allows for clear separation of concerns, making large projects easier to manage. Experiment with this structure to build your understanding!
