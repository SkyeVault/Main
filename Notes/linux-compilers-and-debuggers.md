# Compiling & Debugging in Linux  Beginner to Advanced Guide

---

## 1. What is Compiling?

Think of compiling like **baking bread from a recipe**:
- **Source code** (`.c`, `.cpp`, etc.) = recipe (human-readable)
- **Compiler** = chef that translates the recipe into machine code
- **Executable binary** = finished bread the computer can “eat”

Common Linux compilers:
- `gcc` — GNU C Compiler
- `g++` — GNU C++ Compiler
- `clang` — Alternative C/C++ compiler
- `javac` — Java compiler
- `rustc` — Rust compiler

### Compilation Stages
1. **Preprocessing** — expands `#include`, replaces macros.
2. **Compiling** — turns code into assembly.
3. **Assembling** — converts assembly into object files (`.o`).
4. **Linking** — combines object files & libraries into one executable.

---

## 2. What is Debugging?

Debugging = **finding and fixing bugs in your program**.

Types of bugs:
1. **Compile-time errors** — detected by compiler (syntax errors).
2. **Run-time errors** — happen while program runs (crashes, wrong results).

Debugging lets you:
- Pause the program at **breakpoints**
- Step line-by-line
- Inspect variables
- View the call stack

---

## 3. Why Compile & Debug?

- Without compiling, your computer can’t understand the code.
- Without debugging, you’re guessing why something fails.

---

## 4. First Compile

```bash
gcc hello.c -o hello
```
- `gcc` → compiler
- `hello.c` → source file
- `-o hello` → output file name

Run:
```bash
./hello
```

Error example:
```
hello.c:5:5: error: expected ';' before 'return'
```

---

## 5. Compiling with Debug Info

```bash
gcc hello.c -o hello -g -Wall
```
- `-g` → include debug symbols for `gdb`
- `-Wall` → enable all warnings

---

## 6. Debugging with gdb

```bash
gdb ./hello
```

Inside gdb:
```gdb
run            # start program
break main     # stop at main
next           # step over to next line
step           # step into function
print varName  # show variable value
continue       # resume execution
quit           # exit debugger
```

---

## 7. Core Dumps

Enable:
```bash
ulimit -c unlimited
```

After crash:
```bash
gdb ./program core
(gdb) backtrace
```

---

## 8. Useful Debugging Tools

- **Valgrind** — find memory leaks  
  ```bash
  valgrind --leak-check=full ./program
  ```
- **strace** — trace system calls  
  ```bash
  strace ./program
  ```
- **ltrace** — trace library calls  
  ```bash
  ltrace ./program
  ```

---

## 9. Automating Builds with make

**Makefile example**:
```makefile
program: main.o utils.o
	gcc main.o utils.o -o program

main.o: main.c utils.h
	gcc -c main.c -Wall -g

utils.o: utils.c utils.h
	gcc -c utils.c -Wall -g

clean:
	rm -f *.o program
```

Run:
```bash
make        # build
make clean  # remove build files
```

---

## 10. Troubleshooting Checklist

Compile with:
```bash
gcc program.c -o program -Wall -g
```
Read compiler errors carefully  
If it crashes, run with `gdb`  
For memory bugs, use `valgrind`  
For file/system call issues, use `strace`

---

## 11. Mental Model Recap

- **Compile** = translate code to machine language
- **Debug** = inspect and fix problems
- **Warnings** = helpful hints  
- **Errors** = must fix  
- **`-g`** = maps code to debug info for `gdb`

---