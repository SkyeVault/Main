# Setting Up and Debugging REVM for Ethereum Smart Contracts

**Author:** Your Name  
**Date:** March 2025  
**Project:** Metaverse Sandbox  

This guide documents the **end-to-end setup, debugging, and deployment of an Ethereum smart contract in REVM** using **Foundry** for contract compilation and **Rust** for execution.

---

## **1. Setting Up Foundry for Smart Contract Compilation**

### **1.1 Install Foundry**
Foundry provides Solidity tooling for compiling, testing, and deploying contracts. Install it using:

```sh
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

Verify the installation:

```sh
forge --version
```

### **1.2 Navigate to the Smart Contract Directory**
Move to the blockchain project folder:

```sh
cd ~/main/blockchain/metaverse-sandbox/blockchain
```

Initialize Foundry (if not already initialized):

```sh
forge init
```

### **1.3 Compile the Solidity Contracts**
Ensure your Solidity contracts exist in `src/`, then run:

```sh
forge build
```

If compilation fails with missing imports (e.g., OpenZeppelin), install dependencies:

```sh
forge install OpenZeppelin/openzeppelin-contracts
```

If Foundry does not recognize imports, add a remapping in `remappings.txt`:

```
@openzeppelin/=lib/openzeppelin-contracts/
```

Run `forge build` again to verify successful compilation.

---

## **2. Extracting Smart Contract Bytecode for REVM**

### **2.1 Locate the Compiled Contract JSON**
After running `forge build`, the compiled JSON file should be inside `out/`. Verify its existence:

```sh
find out/ -name "MetaverseLand.json"
```

If missing, rebuild the contracts:

```sh
forge build
```

### **2.2 Extract the Bytecode**
If the compiled JSON exists at `out/MetaverseLand.sol/MetaverseLand.json`, extract the **deployment bytecode**:

```sh
jq -r '.bytecode.object' out/MetaverseLand.sol/MetaverseLand.json > ../blockchain/bytecode.hex
```

Verify the file:

```sh
ls -l ../blockchain/bytecode.hex
```

Ensure the extracted bytecode does not contain an `0x` prefix. If it does, remove it:

```sh
sed -i '' 's/^0x//' ../blockchain/bytecode.hex
```

---

## **3. Running REVM in Rust**

### **3.1 Navigate to the REVM Rust Project**
Move to the Rust REVM execution directory:

```sh
cd ~/main/blockchain/metaverse-sandbox/backend/revm
```

Ensure `Cargo.toml` exists:

```sh
ls -l Cargo.toml
```

### **3.2 Modify `main.rs` to Load Bytecode**
Open `src/main.rs` and ensure it reads `bytecode.hex` properly:

```rust
let bytecode_str = fs::read_to_string("../../blockchain/bytecode.hex")
    .expect("Failed to load bytecode.hex. Ensure the file exists in ../../blockchain/bytecode.hex");

let cleaned_bytecode = bytecode_str.trim().trim_start_matches("0x");
let bytecode_bytes = hex::decode(cleaned_bytecode).expect("Invalid hex");
```

### **3.3 Simulate Contract Deployment in REVM**
Modify `main.rs` to ensure REVM correctly interprets the bytecode as a contract creation:

```rust
evm.context.evm.inner.env.tx.transact_to = revm::primitives::TransactTo::Create;
let result = evm.transact().expect("Transaction failed");
```

Recompile and run REVM:

```sh
cargo clean
cargo build
cargo run
```

---

## **4. Debugging Common Errors**

### **4.1 File Not Found: `MetaverseLand.json`**
If Foundry cannot locate `MetaverseLand.json`, verify the file's existence:

```sh
find out/ -name "MetaverseLand.json"
```

If missing, recompile:

```sh
forge build
```

---

### **4.2 Bytecode Not Found**
If `bytecode.hex` is missing, regenerate it:

```sh
jq -r '.bytecode.object' out/MetaverseLand.sol/MetaverseLand.json > ../blockchain/bytecode.hex
```

Verify:

```sh
ls -l ../blockchain/bytecode.hex
```

---

### **4.3 Invalid Hex Character Error**
If REVM throws an `InvalidHexCharacter` error, ensure `bytecode.hex` does not contain `0x`:

```sh
sed -i '' 's/^0x//' ../blockchain/bytecode.hex
```

---

### **4.4 REVM Does Not Deploy the Contract**
If REVM executes but returns `0x00` bytecode, ensure you are using **deployment bytecode**, not runtime bytecode:

```sh
jq -r '.bytecode.object' out/MetaverseLand.sol/MetaverseLand.json | head -n 5
jq -r '.deployedBytecode.object' out/MetaverseLand.sol/MetaverseLand.json | head -n 5
```

If `.deployedBytecode.object` contains valid data, use that instead:

```sh
jq -r '.deployedBytecode.object' out/MetaverseLand.sol/MetaverseLand.json > ../blockchain/bytecode.hex
```

---

## **5. Confirming Contract Deployment**
A successful deployment should return an **EVM Execution Result** similar to:

```
EVM Execution Result: Success { reason: Return, gas_used: 53000, gas_refunded: 0, logs: [], output: Create(0x, Some(0xbd770416a3345f91e4b34576cb804a576fa48eb1)) }
```

This confirms that:
- The contract **was created successfully**.
- It was deployed at address: `0xbd770416a3345f91e4b34576cb804a576fa48eb1`.

---

## **6. Conclusion**
By following these steps, you successfully:
- Set up **Foundry** for contract compilation.
- Extracted the correct **bytecode**.
- Configured **REVM** to execute smart contract deployments.
- Debugged **common Rust and REVM errors**.
- Successfully **deployed and interacted with a smart contract** in a simulated Ethereum environment.

This guide serves as a **complete reference for setting up and debugging REVM-based Ethereum development**.

