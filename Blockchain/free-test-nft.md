# Free Test Resources and Gas-Free Smart Contract Development (Amoy Edition)

## Introduction

This guide walks through how to develop and test smart contracts for free using **Polygon Amoy**, **Foundry**, and **open-source tools**. You'll learn to deploy contracts without spending real tokens, get testnet funds responsibly, and build a front-end to interact with your smart contract.

---

## 1. Understanding Free Test Resources

### 1.1 What Is an RPC?

RPC (Remote Procedure Call) allows your development tools or dApps to send transactions and read data from a blockchain node.

#### Trusted RPC Providers

- [Alchemy](https://www.alchemy.com/) – Ethereum, Polygon, and more  
- [Infura](https://infura.io/) – Ethereum and IPFS  
- [QuickNode](https://www.quicknode.com/)  
- [Chainlist](https://chainlist.org/) – Easy RPC access for many networks  

---

### 1.2 What Are Faucets?

**Faucets** provide free testnet tokens so you can deploy, test, and interact with contracts without real gas fees.

#### Polygon Amoy Faucet Info (as of 2025):

- The **Polygon Mumbai testnet is deprecated** and replaced by **Amoy**.
- Unlike older testnets, Amoy **requires POL tokens** for gas, which can only be received by:
  - **Bridging from mainnet POL** (not ideal for beginners)  
  - **Filling out the developer form** at [Polygon Faucet](https://faucet.polygon.technology/)

#### How to Get Amoy POL

1. Go to [https://faucet.polygon.technology](https://faucet.polygon.technology)  
2. Click "Request Amoy POL"  
3. Fill out the developer form with:
   - Your wallet address  
   - Project use case or links to your dApp or repo  
4. **Wait for email approval** (usually within 24 hours)  
5. You'll receive **100 Amoy POL**, valid for 90 days  

---

## 2. Setting Up Your Development Environment

### 2.1 Install Foundry (Smart Contract Development Toolkit)

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

### 2.2 Install Node.js and Ethers.js (Frontend Tools)

```bash
curl -fsSL https://fnm.vercel.app/install | bash
fnm install 18
npm install ethers dotenv
```

---

## 3. Configure MetaMask and Add the Amoy Testnet

### Amoy Testnet Settings

- **Network Name:** Polygon Amoy  
- **New RPC URL:** `https://rpc-amoy.polygon.technology`  
- **Chain ID:** `80002`  
- **Currency Symbol:** POL  

Once added, you'll be able to receive and use testnet POL to deploy contracts and test dApps.

---

## 4. Writing & Deploying a Simple Smart Contract

### 4.1 Create the Project

```bash
mkdir amoy-free-dapp && cd amoy-free-dapp
forge init
```

### 4.2 Create `src/FreeDapp.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FreeDapp {
    string public message;

    constructor(string memory _message) {
        message = _message;
    }

    function updateMessage(string memory _newMessage) public {
        message = _newMessage;
    }
}
```

### 4.3 Compile the Contract

```bash
forge build
```

---

## 5. Deploying to Polygon Amoy

### 5.1 Setup `.env`

Create a `.env` file in your root project:

```env
PRIVATE_KEY=your_private_key_here
DEPLOYER_ADDRESS=0xYourAddress
RPC_URL=https://rpc-amoy.polygon.technology
```

### 5.2 Write `script/Deploy.s.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../src/FreeDapp.sol";

contract Deploy is Script {
    function run() external {
        vm.startBroadcast();
        new FreeDapp("Hello, Amoy!");
        vm.stopBroadcast();
    }
}
```

### 5.3 Deploy Using Foundry

```bash
forge script script/Deploy.s.sol:Deploy \
  --rpc-url $RPC_URL \
  --broadcast \
  --legacy \
  --private-key $PRIVATE_KEY
```

You should see a transaction hash and deployed contract address if successful.

---

## 6. Optional: Build a Frontend with React + Ethers

### 6.1 Scaffold a React App

```bash
npx create-react-app freedapp-frontend
cd freedapp-frontend
npm install ethers
```

### 6.2 Add Contract Logic in `src/App.js`

```js
import { useEffect, useState } from "react";
import { ethers } from "ethers";

const CONTRACT_ADDRESS = "0xYourDeployedContract";
const ABI = [
  {
    "inputs": [],
    "name": "message",
    "outputs": [{ "internalType": "string", "type": "string" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{ "internalType": "string", "name": "_newMessage", "type": "string" }],
    "name": "updateMessage",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

function App() {
  const [message, setMessage] = useState("");
  const [newMessage, setNewMessage] = useState("");
  const [contract, setContract] = useState(null);

  useEffect(() => {
    async function init() {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
      setContract(contract);
      setMessage(await contract.message());
    }
    init();
  }, []);

  async function updateMessage() {
    const tx = await contract.updateMessage(newMessage);
    await tx.wait();
    setMessage(await contract.message());
  }

  return (
    <div>
      <h1>Free Amoy dApp</h1>
      <p>Stored Message: {message}</p>
      <input onChange={(e) => setNewMessage(e.target.value)} />
      <button onClick={updateMessage}>Update</button>
    </div>
  );
}

export default App;
```

### 6.3 Run the App

```bash
npm start
```

---

## 7. Tips for Working with Amoy

- Amoy **does not support traditional faucets** (Alchemy, QuickNode, etc.)
- **You must apply** through [Polygon's Developer Faucet Form](https://faucet.polygon.technology/)
- Each developer can receive **up to 100 Amoy POL every 90 days** per wallet

---

## Conclusion

You're now fully equipped to:

- Set up a **local smart contract development environment**  
- Deploy contracts to **Polygon Amoy**  
- Request real testnet funds from a trusted source  
- Build and connect a frontend using **React + Ethers**  
- Experiment without mainnet fees

Use this as your full-stack foundation before migrating to production.