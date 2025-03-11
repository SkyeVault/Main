# **Solidity & Smart Contracts: The Complete Guide**  

This guide takes you from **Solidity fundamentals** to **writing, deploying, and securing smart contracts** on Ethereum and other EVM-compatible blockchains.

---

## **1. Understanding Solidity & Smart Contracts**  

### **What is Solidity?**  
- Solidity is a **high-level, statically-typed** language designed for writing **smart contracts**.  
- It **compiles to EVM bytecode** and runs on the **Ethereum Virtual Machine (EVM)**.  

### **What is a Smart Contract?**  
A smart contract is a **self-executing program** stored on the blockchain. It can:  
- **Store & manage assets** (ETH, tokens, NFTs).  
- **Automate rules & logic** (DAOs, lending, staking).  
- **Interact with other contracts** (Uniswap, Compound).  

---

## **2. Setting Up Solidity Development with Foundry**  

### **Install Foundry (Solidity Framework)**  
```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```
Verify installation:  
```bash
forge --version
```

### **Create a New Foundry Project**  
```bash
forge init solidity_project
cd solidity_project
```

### **Install VS Code & Solidity Extension**  
- Install **VS Code**.  
- Add the **Solidity Plugin** (by Juan Blanco) for syntax highlighting.  

---

## **3. Writing Your First Solidity Contract**  

Create `src/HelloWorld.sol`:  
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract HelloWorld {
    string public message;

    constructor(string memory _message) {
        message = _message;
    }

    function updateMessage(string memory _newMessage) public {
        message = _newMessage;
    }
}
```

### **Understanding the Code**  
- `pragma solidity ^0.8.19;` → Specifies Solidity version.  
- `contract HelloWorld {}` → Defines the contract.  
- `string public message;` → Declares a **public** state variable.  
- `constructor()` → Runs **once** when the contract is deployed.  
- `updateMessage()` → Allows users to **update** the message.  

---

## **4. Compiling & Deploying the Contract**  

### **Compile the Contract**  
```bash
forge build
```

### **Deploy to Local Ethereum Network**  
1. Start a local blockchain:  
   ```bash
   anvil
   ```
2. Deploy the contract using `cast`:  
   ```bash
   cast send --rpc-url http://127.0.0.1:8545 --private-key 0xYOUR_PRIVATE_KEY "HelloWorld('Hello, Solidity!')"
   ```

### **Deploy to Testnet (Goerli or Sepolia)**  
```bash
forge create --rpc-url $RPC_URL --private-key $PRIVATE_KEY src/HelloWorld.sol:HelloWorld --constructor-args "Hello, Solidity!"
```

---

## **5. Solidity Basics & Key Concepts**  

### **1. Solidity Data Types**  

| Type      | Example                           | Description                    |
|-----------|----------------------------------|--------------------------------|
| `uint`    | `uint256 count = 100;`          | Unsigned integer (no negatives) |
| `int`     | `int256 balance = -50;`         | Signed integer (can be negative) |
| `bool`    | `bool isOpen = true;`           | Boolean (true/false) |
| `string`  | `string name = "Lorelei";`      | String (text) |
| `address` | `address owner = msg.sender;`   | Ethereum address |
| `bytes32` | `bytes32 hash;`                 | Fixed-size byte array |

---

### **2. Functions & Visibility**  

```solidity
function setMessage(string memory _newMessage) public {
    message = _newMessage;
}
```
| Visibility  | Who Can Access? |
|------------|----------------|
| `public`   | Anyone |
| `private`  | Only inside the contract |
| `internal` | Inside the contract & inherited contracts |
| `external` | Only other contracts |

---

### **3. Mappings & Structs**  

Used for storing complex data.  
```solidity
struct User {
    uint id;
    string name;
}

mapping(address => User) public users;
```

---

### **4. Modifiers (Access Control)**  

Restrict function access:  
```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "Not owner");
    _;
}
```

---

### **5. Events & Logging**  

Use events to **emit logs**:  
```solidity
event MessageUpdated(string oldMessage, string newMessage);

function updateMessage(string memory _newMessage) public {
    emit MessageUpdated(message, _newMessage);
    message = _newMessage;
}
```

---

## **6. Security & Smart Contract Best Practices**  

### **1. Preventing Reentrancy Attacks**  

Reentrancy occurs when a contract **calls another contract before updating its state**.

#### **Vulnerable Code (DO NOT DO THIS)**  
```solidity
function withdraw() public {
    uint amount = balances[msg.sender];
    msg.sender.call{value: amount}("");
    balances[msg.sender] = 0;
}
```
#### **Fix: Use ReentrancyGuard**  
```solidity
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SecureBank is ReentrancyGuard {
    function withdraw() public nonReentrant {
        uint amount = balances[msg.sender];
        balances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
```

---

### **2. Prevent Integer Overflow**  

#### **Old Vulnerability: Integer Overflow**  
```solidity
uint8 count = 255;
count++;  // Overflow, wraps back to 0
```
#### **Fix: Use Solidity 0.8+ (Built-in SafeMath)**  
```solidity
uint256 count = 255;
count++; // Throws error instead of wrapping
```

---

## **7. Testing Smart Contracts**  

### **Write a Foundry Test**  

Create `test/HelloWorld.t.sol`:  
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Test.sol";
import "../src/HelloWorld.sol";

contract HelloWorldTest is Test {
    HelloWorld hello;

    function setUp() public {
        hello = new HelloWorld("Hello, Foundry!");
    }

    function testUpdateMessage() public {
        hello.updateMessage("New Message");
        assertEq(hello.message(), "New Message");
    }
}
```
#### **Run Tests**  
```bash
forge test
```

---

## **Next Steps**  

### Master Solidity Basics  
### Write & Deploy Contracts  
### Learn Solidity Security  
### Run Foundry Tests  

### **What’s Next?**  
1. Deep dive into **Solidity security challenges**.  
2. Advanced smart contract **hacking & auditing**.  
3. Step-by-step guide for **deploying secure dApps**.  

Let me know where you want to go next.  