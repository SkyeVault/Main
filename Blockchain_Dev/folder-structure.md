metaverse-land/
│── contracts/            # Smart contracts
│   ├── MetaverseLand.sol  # Land NFT contract (ERC-721)
│   ├── Marketplace.sol    # Land marketplace contract
│   ├── Rental.sol         # Land rental contract
│   ├── utils/             # Utility contracts (e.g., libraries)
│── scripts/              # Deployment and automation scripts
│   ├── DeployLand.s.sol   # Script to deploy land contract
│   ├── DeployMarket.s.sol # Script to deploy marketplace
│── test/                 # Smart contract tests
│   ├── MetaverseLand.t.sol
│   ├── Marketplace.t.sol
│── storage/              # Land metadata (IPFS JSON files)
│   ├── parcels/          # Individual land parcel metadata
│   ├── metadata-schema.json  # JSON structure for land data
│── frontend/             # Frontend integration (Next.js, Ethers.js)
│   ├── components/
│   ├── pages/
│── docs/                 # Documentation
│   ├── README.md         # Project overview
│   ├── LAND_NFT.md       # Detailed explanation of land NFTs
│   ├── MARKETPLACE.md    # Marketplace documentation
│── foundry.toml          # Foundry project configuration
│── .env                  # Environment variables (private keys, RPC URLs)
│── package.json          # Dependencies for frontend (if applicable)