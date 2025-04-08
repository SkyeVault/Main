# Understanding `lib.rs` vs `utils.rs` in Rust

## **1. What is `lib.rs`?**
- `lib.rs` is the **main entry point** for a Rust library crate.
- Functions defined here are **accessible throughout the crate** and can be **exported for external use** if the crate is published.
- Cargo automatically recognizes `lib.rs` when you define a library crate in `Cargo.toml`:

```toml
[lib]
name = "my_project"
path = "src/lib.rs"
```

### **Example Usage**
```rust
// src/lib.rs

/// Formats a track name with title and artist.
pub fn format_track_name(title: &str, artist: &str) -> String {
    format!("{} - {}", title, artist)
}
```

Now, this function can be used inside `main.rs`:
```rust
use my_project::format_track_name;

fn main() {
    let formatted = format_track_name("Song Title", "Artist Name");
    println!("Formatted: {}", formatted);
}
```

---

## **2. What is `utils.rs`?**
- `utils.rs` is **not automatically recognized** by Cargo.
- It is typically used to **store helper functions** that don't belong in `lib.rs` but are needed within the project.
- You must **explicitly include it** inside `lib.rs`:

```rust
pub mod utils;
```

### **Example Usage**
```rust
// src/utils.rs
pub fn capitalize_first_letter(s: &str) -> String {
    let mut chars = s.chars();
    match chars.next() {
        None => String::new(),
        Some(first) => first.to_uppercase().collect::<String>() + chars.as_str(),
    }
}
```

#### **Use it inside `lib.rs`**
```rust
pub mod utils;
```

#### **Use it inside `main.rs`**
```rust
use my_project::utils::capitalize_first_letter;

fn main() {
    let word = "rust";
    let capitalized = capitalize_first_letter(word);
    println!("Capitalized: {}", capitalized);
}
```

---

## **3. Key Differences Between `lib.rs` and `utils.rs`**

| Feature | `lib.rs` | `utils.rs` |
|---------|---------|------------|
| **Main library entry point** | ✅ Yes | ❌ No |
| **Automatically recognized by Cargo?** | ✅ Yes | ❌ No |
| **Needs to be included manually?** | ❌ No | ✅ Yes (`pub mod utils;`) |
| **Can contain public functions?** | ✅ Yes | ✅ Yes |
| **Can be used in `main.rs`?** | ✅ Yes | ✅ Yes (if included) |

---

## **4. When to Use Each One**

| **Scenario** | **Use `lib.rs`?** | **Use `utils.rs`?** |
|--------------|----------------|----------------|
| You need a **library** that can be used externally | ✅ Yes | ❌ No |
| You need helper functions **only inside the project** | ✅ Yes | ✅ Yes |
| You need to organize **small utility/helper functions** | ❌ No | ✅ Yes |
| You want functions accessible **in `main.rs`** | ✅ Yes | ✅ Yes (if included) |

---

## **5. Should You Keep Both in Your Project?**
- **If you only need a library**, keep everything in `lib.rs`.
- **If you have a lot of helper functions**, create `utils.rs` and include it in `lib.rs`.
- **If `utils.rs` is just duplicating `lib.rs`, delete it.**

### **Deleting `utils.rs` If It's Unnecessary**
If all functions inside `utils.rs` are already in `lib.rs`, remove it:
```bash
rm src/utils.rs
```
Then commit and push the change:
```bash
git add .
git commit -m "Removed unnecessary utils.rs file"
git push origin main
```

---

## **Final Takeaways**
 **`lib.rs` is for defining the core library of your Rust project.**  
 **`utils.rs` is useful for organizing helper functions but must be explicitly included.**  
 **If `utils.rs` only duplicates `lib.rs`, delete it.**  

By following this structure, you keep your Rust project **organized, maintainable, and efficient**.
