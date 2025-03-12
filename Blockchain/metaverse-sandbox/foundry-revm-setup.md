# Foundry and REVM Setup Guide

## Introduction
This guide explains how to integrate **Foundry** (Ethereum smart contract development framework) with **REVM** (Rust Ethereum Virtual Machine) inside the **Metaverse Sandbox** project. Foundry is used for compiling, testing, and deploying Solidity contracts, while REVM is used for executing EVM bytecode in Rust.

---

## 1. Install Foundry
Foundry provides Solidity tooling, including `forge` (for building and testing), `cast` (for Ethereum RPC interactions), and `anvil` (a local testnet).

Run the following commands to install Foundry:

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

Verify the installation:
```bash
forge --version
```

---

## 2. Initialize Foundry in `blockchain/`
Navigate to the `blockchain/` folder and initialize Foundry:

```bash
cd blockchain
forge init
```

This creates the following structure:
```
blockchain/
├── src/
│   ├── MetaverseLand.sol
│   ├── Marketplace.sol
│   ├── DAO.sol
├── script/       # Deployment scripts
├── test/         # Foundry tests
├── foundry.toml  # Configuration file
```

Move existing contracts into `src/`:
```bash
mv blockchain/contracts/*.sol blockchain/src/
```

Compile the contracts:
```bash
forge build
```

---

## 3. Write and Run Tests in Foundry
Foundry allows writing Solidity-based tests inside `test/`.

Create `blockchain/test/MetaverseLand.t.sol`:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Test.sol";
import "../src/MetaverseLand.sol";

contract MetaverseLandTest is Test {
    MetaverseLand land;

    function setUp() public {
        land = new MetaverseLand();
    }

    function testMintLand() public {
        land.mintLand(address(this));
        assertEq(land.ownerOf(0), address(this));
    }
}
```

Run the test:
```bash
forge test
```

---

## 4. Deploy the Contracts with Foundry
Modify `blockchain/script/Deploy.s.sol`:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/MetaverseLand.sol";

contract Deploy is Script {
    function run() external {
        vm.startBroadcast();
        MetaverseLand land = new MetaverseLand();
        vm.stopBroadcast();
    }
}
```

Deploy to a testnet:
```bash
forge script script/Deploy.s.sol --rpc-url $RPC_URL --private-key $PRIVATE_KEY --broadcast
```

---

## 5. Integrate Foundry with REVM
The `backend/revm/` setup can execute **compiled bytecode** from Foundry contracts inside Rust.

Extract contract bytecode:
```bash
jq -r '.bytecode.object' out/MetaverseLand.json > bytecode.hex
```

Modify `backend/revm/src/main.rs`:
```rust
use revm::{Evm, primitives::Bytecode};
use std::fs;

fn main() {
    let bytecode_str = fs::read_to_string("../blockchain/bytecode.hex").expect("Failed to load bytecode");
    let bytecode_bytes = hex::decode(bytecode_str.trim()).expect("Invalid hex");

    let contract = Bytecode::new_raw(bytecode_bytes.into());
    let mut evm = Evm::default();
    
    evm.env.tx.data = contract.bytes().clone();
    let result = evm.transact().expect("Transaction failed");

    println!("EVM Execution Result: {:?}", result);
}
```

Run the simulation:
```bash
cargo run
```

---

## 6. Automate Tests with GitHub Actions
To automatically test contracts, add `.github/workflows/foundry.yml`:

```yaml
name: Foundry Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Foundry
        run: curl -L https://foundry.paradigm.xyz | bash && foundryup
      - name: Run Tests
        run: forge test
```

---

## Next Steps
- Develop additional Solidity contracts
- Expand the Rust-based REVM execution logic
- Improve deployment pipelines
- Implement an on-chain governance mechanism

This setup ensures a fully integrated workflow between Foundry for Solidity development and REVM for execution testing.

