# **Rust Programming Basics Guide**  
### **Date: 250309**  

---

## **1. Syntax**  
Rust has a strict and structured syntax with a focus on **safety and performance**.  

```rust
fn main() {
    println!("Hello, world!");
}
```

### **Key Syntax Features**  
- **Semicolons (`;`)** end most statements.  
- **Curly braces (`{}`)** define function bodies and control flow blocks.  
- **Rust enforces strict type safety and borrowing rules.**  

---

## **2. Variables & Data Types**  
- **Variables are immutable by default;** use `mut` for mutability.  
- **Rust enforces strict type safety.**  

```rust
fn main() {
    let x: i32 = 10;    // Immutable integer
    let mut y: f64 = 5.5; // Mutable float
    let name: &str = "Alice"; // String slice
    let is_rust_fun: bool = true; // Boolean

    println!("x: {}, y: {}, name: {}, is_rust_fun: {}", x, y, name, is_rust_fun);
}
```

---

## **3. Operators**  
Rust supports **arithmetic, comparison, logical, bitwise, and assignment operators**.  

```rust
fn main() {
    let a = 10;
    let b = 5;
    let sum = a + b;   // Addition
    let is_equal = a == b;  // Comparison
    let logical = a > 5 && b < 10; // Logical AND

    println!("Sum: {}, Equal: {}, Logical: {}", sum, is_equal, logical);
}
```

---

## **4. Control Structures (Conditionals & Loops)**  

### **If-Else Conditionals**  

```rust
fn main() {
    let num = 10;

    if num > 0 {
        println!("Positive number");
    } else {
        println!("Negative number");
    }
}
```

### **Loops in Rust**  
Rust provides **`for`, `while`, and `loop` (infinite loop, similar to `while true`)**.  

```rust
fn main() {
    for i in 0..5 {
        println!("i: {}", i);
    }

    let mut x = 0;
    while x < 5 {
        println!("x: {}", x);
        x += 1;
    }

    let mut y = 0;
    loop {
        println!("y: {}", y);
        y += 1;
        if y == 3 {
            break; // Exit loop
        }
    }
}
```

---

## **5. Functions & Methods**  
- **Functions are defined with `fn`**.  
- **Rust enforces explicit return types.**  

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b  // No need for return keyword if it's the last expression
}

fn main() {
    let result = add(5, 10);
    println!("Sum: {}", result);
}
```

---

## **6. Data Structures**  

### **Arrays and Vectors**  

```rust
fn main() {
    let arr: [i32; 3] = [1, 2, 3];  // Fixed-size array
    let mut vec = vec![4, 5, 6];  // Dynamic vector

    vec.push(7); // Adding element to vector

    println!("Array: {:?}", arr);
    println!("Vector: {:?}", vec);
}
```

### **Structs in Rust**  

```rust
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let user = Person {
        name: String::from("Alice"),
        age: 30,
    };

    println!("Name: {}, Age: {}", user.name, user.age);
}
```

---

## **7. Input/Output (I/O Operations)**  

### **User Input**  

```rust
use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter your name:");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    println!("Hello, {}", input.trim());
}
```

### **File I/O**  

```rust
use std::fs::File;
use std::io::Write;

fn main() {
    let mut file = File::create("output.txt").expect("Could not create file");
    file.write_all(b"Hello, Rust!").expect("Could not write to file");
}
```

---

## **8. Summary Table**  

| **Concept**        | **Rust Example**                          |
|--------------------|------------------------------------------|
| Syntax            | `fn main() { println!("Hello!"); }`     |
| Variables & Types | `let x: i32 = 5; let mut y = 10;`       |
| Operators         | `let sum = x + y; let is_equal = x == y;` |
| Control Flow      | `if x > 0 { ... } else { ... }`         |
| Loops             | `for i in 0..5 { ... }`                 |
| Functions         | `fn add(a: i32, b: i32) -> i32 { a + b }` |
| Data Structures   | `struct Person { name: String, age: u8 }` |
| I/O Operations    | `io::stdin().read_line(&mut input);`    |

---

## **Next Steps**  
- **Experiment** with each concept by modifying the examples.  
- **Build small Rust projects** to apply what you’ve learned.  
- **Explore ownership, borrowing, lifetimes, and advanced Rust concepts.**  

---

## **How to Use This Guide**  

1. **Save as** `rust_basics.md`.  
2. **Push it to GitHub** for easy reference.  
3. **View it in Markdown format** using:  
   - **GitHub**  
   - **VS Code**  
   - **Obsidian**  
   - **Markdown Viewers**  
4. **Modify & Expand** it as you learn new Rust concepts.  

---

## **Why This Works**  
- **Code blocks (` ```rust `) are enclosed properly**, ensuring correct formatting in **GitHub and Markdown viewers**.  
- **Triple backticks are properly closed** for every Rust example.  
- **Markdown syntax is optimized** for clear readability.  

This guide is now **ready for GitHub, VS Code, or any Markdown-supported platform**. Let me know if you need any modifications.  