# Rust Loop Functions Guide

## Introduction
Loops in Rust allow you to execute a block of code multiple times without rewriting the same statements. Rust provides three main types of loops:

- `loop` (infinite loop)
- `while` loop (condition-based loop)
- `for` loop (iteration-based loop)

Each type of loop serves a different purpose. This guide will explain each loop with examples and best practices.

---

## 1. `loop` (Infinite Loop)
The `loop` keyword creates an infinite loop that runs until explicitly stopped using `break`.

### Example:
```rust
let mut count = 0;

loop {
    println!("Count is: {}", count);
    count += 1;
    
    if count >= 5 {
        break; // Exits the loop when count reaches 5
    }
}
```

### Explanation:
- The `loop {}` block runs indefinitely.
- We use `break;` to **stop** the loop when a condition is met.
- This type of loop is useful when you don't know the exact number of iterations needed.

### When to Use:
- When waiting for an event (e.g., a server continuously listening for requests).
- When you need to retry an operation until it succeeds.

---

## 2. `while` Loop
A `while` loop runs **as long as** a condition is `true`.

### Example:
```rust
let mut count = 1;

while count <= 5 {
    println!("Count is: {}", count);
    count += 1;
}
```

### Explanation:
- The loop checks the condition (`count <= 5`) **before** each iteration.
- If the condition is `false`, the loop stops.
- This is useful when the number of iterations depends on a condition.

### When to Use:
- When waiting for a condition to become false.
- When iterating based on user input.

---

## 3. `for` Loop
A `for` loop iterates over a range or collection and is the preferred loop when the number of iterations is known.

### Example:
```rust
for number in 1..=5 {
    println!("Number: {}", number);
}
```

### Explanation:
- `1..=5` is a **range** that starts at `1` and ends at `5`.
- The loop automatically stops after the last value.
- This is the most idiomatic way to iterate over a sequence in Rust.

### When to Use:
- When looping over a sequence of numbers.
- When iterating over collections (arrays, vectors, etc.).

---

## 4. Loop Control Statements
Rust provides control statements to alter loop execution:

### `break` (Exit a Loop Early)
```rust
for num in 1..=10 {
    if num == 5 {
        break; // Stops the loop at 5
    }
    println!("{}", num);
}
```

### `continue` (Skip to Next Iteration)
```rust
for num in 1..=5 {
    if num == 3 {
        continue; // Skips printing 3
    }
    println!("{}", num);
}
```

---

## 5. Nested Loops
Loops can be nested within each other.

### Example:
```rust
for i in 1..=3 {
    for j in 1..=2 {
        println!("i: {}, j: {}", i, j);
    }
}
```

This prints:
```
i: 1, j: 1
i: 1, j: 2
i: 2, j: 1
i: 2, j: 2
i: 3, j: 1
i: 3, j: 2
```

---

## 6. Loop Labels (Breaking Out of Nested Loops)
Rust allows **loop labels** to break out of specific loops.

### Example:
```rust
'l_outer: for i in 1..=3 {
    for j in 1..=3 {
        if i == 2 && j == 2 {
            break 'l_outer; // Exits both loops
        }
        println!("i: {}, j: {}", i, j);
    }
}
```

---

## 7. Choosing the Right Loop
| Loop Type | When to Use |
|-----------|------------|
| `loop` | When you need an infinite loop with manual exit (`break`). |
| `while` | When looping until a condition becomes `false`. |
| `for` | When iterating over a known range or collection. |

---

## Conclusion
Loops are essential in Rust for handling repetition efficiently. Choosing the right loop type improves both readability and performance. Practice using loops in different scenarios to get comfortable with them!
