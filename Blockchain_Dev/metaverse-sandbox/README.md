# Metaverse Sandbox - Developer Guide

## Introduction
The Metaverse Sandbox is a **non-gaming open-source metaverse** built using Rust, Solidity, and JavaScript. It features blockchain-based land ownership, a marketplace for virtual land sales, and a governance model for community-driven decisions.

This guide explains how to navigate the project structure, perform the initial setup, and understand how each file interacts with the system.

---

## Project Structure

```plaintext
metaverse-sandbox/
├── backend/                    # Rust/Node backend for authentication, APIs, and land management
│   ├── src/
│   │   ├── main.rs              # Rust Axum API entry point
│   │   ├── auth.rs              # Wallet authentication (MetaMask, WalletConnect)
│   │   ├── land_registry.rs      # ERC-721 NFT Land Registry integration
│   │   ├── marketplace.rs        # Smart contract API for land sales, leases, and transfers
│   │   ├── ipfs.rs               # IPFS integration for metadata storage
│   │   ├── graphql.rs            # GraphQL API for querying land data
│   │   ├── db/
│   │   │   ├── schema.rs          # Land ownership database schema
│   │   │   ├── queries.rs         # Database queries for land retrieval
│   ├── revm/                     # REVM-based smart contract execution
│   │   ├── Cargo.toml             # Rust dependencies for REVM
│   │   ├── src/
│   │   │   ├── main.rs            # REVM smart contract executor
│   ├── Cargo.toml                # Rust dependencies
│   ├── package.json              # Node dependencies (if using hybrid Rust/Node backend)
│   ├── .env                      # Environment variables for API keys, RPC URLs
│   ├── Dockerfile                # Containerization setup
├── blockchain/                   # Smart contracts and blockchain integrations
│   ├── foundry/                   # Foundry framework for Solidity contracts
│   │   ├── src/
│   │   │   ├── MetaverseLand.sol  # ERC-721 Land ownership contract
│   │   │   ├── Marketplace.sol    # Smart contract for land sales and leases
│   │   │   ├── DAO.sol            # Governance contract
│   │   ├── test/                  # Solidity-based tests with Foundry
│   │   ├── script/                # Foundry deployment scripts
│   │   ├── foundry.toml           # Foundry configuration
│   ├── hardhat.config.js          # Hardhat configuration for Solidity development
├── frontend/                      # Web-based UI for land management
│   ├── src/
│   │   ├── components/
│   │   │   ├── MapViewer.js         # Renders metaverse map using Three.js
│   │   │   ├── LandCard.js          # Displays land details
│   │   ├── pages/
│   │   │   ├── index.js             # Main landing page
│   │   │   ├── dashboard.js         # User dashboard
│   │   │   ├── explore.js           # Explore metaverse parcels
│   │   │   ├── marketplace.js       # Buy/sell land UI
│   │   ├── utils/
│   │   │   ├── walletConnect.js     # MetaMask/WalletConnect integration
│   │   │   ├── ipfs.js              # IPFS data fetching
│   │   │   ├── smartContract.js     # Web3.js or ethers.js contract helpers
│   ├── package.json                 # Dependencies for React/Next.js frontend
│   ├── tailwind.config.js            # TailwindCSS configuration
│   ├── .env                          # Frontend environment variables
├── storage/                          # Decentralized storage integration
│   ├── ipfs/                          # IPFS metadata storage
│   ├── arweave/                        # Arweave metadata (optional)
│   ├── pinata/                         # Pinata cloud storage API scripts
├── governance/                        # DAO & governance integrations
│   ├── snapshot/                       # Snapshot.org proposal scripts
│   ├── treasury/                        # DAO-controlled funds management
│   ├── staking/                         # Staking mechanism for landowners
├── docs/                               # Documentation
│   ├── setup.md                         # Installation & setup guide
│   ├── api-reference.md                 # API endpoints documentation
│   ├── smart-contracts.md                # Smart contract details
│   ├── contributing.md                   # How to contribute
├── .gitignore                           # Ignore unnecessary files
├── README.md                            # Project overview
```

---

## Initial Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SkyeVault/Main.git
cd Main/Blockchain_Dev/metaverse-sandbox
```

### 2. Install Backend Dependencies
```bash
cd backend
cargo build  # If using Rust
npm install  # If using Node.js
```

### 3. Install Blockchain Dependencies
```bash
cd blockchain/foundry
forge install
forge build
```

### 4. Install Frontend Dependencies
```bash
cd frontend
npm install
```

### 5. Set Up Environment Variables
Copy `.env.example` to `.env` in each folder and update the values.

---

## Next Steps
- Run the backend with `cargo run` or `npm start`.
- Deploy smart contracts using Foundry with `forge script script/Deploy.s.sol --rpc-url $RPC_URL --private-key $PRIVATE_KEY --broadcast`.
- Test smart contracts with `forge test`.
- Execute smart contract bytecode in `revm` with `cargo run`.
- Start the frontend with `npm run dev`.
- Explore metaverse land and interact with smart contracts.

For more details, refer to `docs/setup.md` and `docs/api-reference.md`.