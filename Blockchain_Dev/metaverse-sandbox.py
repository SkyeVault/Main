import os

# Base directory
BASE_DIR = "main/blockchaindev/metaverse-sandbox"

# Directory structure
DIRS = [
    "backend/src/db",
    "blockchain/contracts",
    "blockchain/test",
    "blockchain/scripts",
    "frontend/public/assets",
    "frontend/src/components",
    "frontend/src/pages",
    "frontend/src/styles",
    "frontend/src/utils",
    "storage/ipfs",
    "storage/arweave",
    "storage/pinata",
    "governance/snapshot",
    "governance/treasury",
    "governance/staking",
    "docs"
]

# Files to be created with content
FILES = {
    "backend/src/main.rs": "// Rust Axum API entry point\nfn main() {}",
    "backend/src/auth.rs": "// Wallet authentication module\n",
    "backend/src/land_registry.rs": "// ERC-721 NFT Land Registry\n",
    "backend/src/marketplace.rs": "// Smart contract API for land sales\n",
    "backend/src/ipfs.rs": "// IPFS integration module\n",
    "backend/src/graphql.rs": "// GraphQL API module\n",
    "backend/src/db/schema.rs": "// Land ownership database schema\n",
    "backend/src/db/queries.rs": "// Database queries for land retrieval\n",
    "backend/Cargo.toml": "[package]\nname = \"metaverse-backend\"\nversion = \"0.1.0\"\nedition = \"2021\"",
    "backend/package.json": "{\n  \"name\": \"metaverse-backend\",\n  \"version\": \"1.0.0\"\n}",
    "backend/.env": "# Environment variables\nRPC_URL=\nPRIVATE_KEY=",
    "backend/Dockerfile": "FROM rust:latest\nWORKDIR /app\nCOPY . .\nCMD [\"cargo\", \"run\"]",
    "blockchain/contracts/MetaverseLand.sol": "// ERC-721 Land ownership contract",
    "blockchain/contracts/Marketplace.sol": "// Smart contract for land sales",
    "blockchain/contracts/DAO.sol": "// DAO governance contract",
    "blockchain/test/MetaverseLand.test.js": "// Test for ERC-721 contract",
    "blockchain/test/Marketplace.test.js": "// Test for Marketplace contract",
    "blockchain/scripts/deploy.js": "// Deploy script",
    "blockchain/scripts/mintLand.js": "// Mint land NFTs",
    "blockchain/scripts/listLand.js": "// List land for sale",
    "blockchain/hardhat.config.js": "module.exports = { solidity: \"0.8.19\" };",
    "frontend/src/components/MapViewer.js": "// Three.js map viewer",
    "frontend/src/components/LandCard.js": "// Component for land display",
    "frontend/src/pages/index.js": "// Landing page",
    "frontend/src/pages/dashboard.js": "// User dashboard",
    "frontend/src/pages/explore.js": "// Explore parcels",
    "frontend/src/pages/marketplace.js": "// Marketplace UI",
    "frontend/src/styles/global.css": "body { font-family: sans-serif; }",
    "frontend/src/utils/walletConnect.js": "// MetaMask/WalletConnect integration",
    "frontend/src/utils/ipfs.js": "// IPFS fetching utilities",
    "frontend/src/utils/smartContract.js": "// Web3.js or ethers.js contract helpers",
    "frontend/package.json": "{\n  \"name\": \"metaverse-frontend\",\n  \"version\": \"1.0.0\"\n}",
    "frontend/tailwind.config.js": "module.exports = { content: ['./src/**/*.{js,jsx,ts,tsx}'] };",
    "frontend/.env": "# Frontend environment variables",
    "storage/ipfs/metadata.json": "{ \"name\": \"Land Parcel\", \"description\": \"A piece of virtual land\" }",
    "docs/setup.md": "# Installation & Setup Guide",
    "docs/api-reference.md": "# API Reference Documentation",
    "docs/smart-contracts.md": "# Smart Contract Details",
    "docs/contributing.md": "# How to Contribute",
    ".gitignore": "*.env\nnode_modules/\ntarget/",
    "README.md": "# Metaverse Sandbox - Open Source Virtual Land System"
}

# Function to create directories
def create_directories():
    for directory in DIRS:
        path = os.path.join(BASE_DIR, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")

# Function to create files with content
def create_files():
    for file, content in FILES.items():
        path = os.path.join(BASE_DIR, file)
        with open(path, "w") as f:
            f.write(content)
        print(f"Created file: {path}")

# Run setup functions
if __name__ == "__main__":
    create_directories()
    create_files()
    print("Metaverse Sandbox setup completed.")