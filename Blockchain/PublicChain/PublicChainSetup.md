# US Public Chain - Initialization & Implementation Plan

## Phase 1: MVP Setup (Minimum Viable Prototype)

### 1. Smart Contract Development

#### Contracts to Build
- `PublicAssistanceToken.sol`
  - Non-transferable ERC20
  - Resets monthly
  - Category restrictions (food, housing, transit, etc.)
- `PublicWorkerPayroll.sol`
  - USDC payroll distribution
  - Salary visibility
  - Monthly disbursement logic

#### Tools
- Solidity
- Hardhat or Foundry
- OpenZeppelin libraries

#### Tasks
- [ ] Scaffold contract repo
- [ ] Write basic logic
- [ ] Add tests
- [ ] Deploy to Polygon Amoy testnet

---

### 2. Frontend Development

#### Framework
- Astro or React
- Tailwind CSS

#### Pages
- Public Dashboard (View aid and payroll stats)
- Recipient Portal (PAT wallet, spending interface)
- Worker Portal (Payroll record, balance view)

#### Tasks
- [ ] Create project structure
- [ ] Set up WalletConnect or MetaMask login
- [ ] Connect to contracts using Ethers.js or Wagmi
- [ ] Build UI components for token display and interaction

---

### 3. Deployment

#### Blockchain Deployment
- Use Amoy testnet for both contracts
- Verify contracts on Polygonscan
- Upload metadata to IPFS (if applicable)

#### Frontend Hosting
- Use GitHub Pages (temporary)
- Optional: Host on IPFS with Fleek or Pinata

#### Tasks
- [ ] Deploy contracts to Amoy
- [ ] Deploy frontend site
- [ ] Link wallet interactions

---

## Phase 2: Token Flow Simulation & Analytics

### 1. Monthly Token Flow Visuals
- Use Recharts or D3.js
- Data from smart contract events

#### Graphs
- Monthly PAT issued
- Payroll disbursed (USDC)
- Spend by category (aggregate)

### 2. Anonymity & Traceability
- Use anonymized wallet IDs
- Public view of transaction logs
- Exportable CSV or JSON formats

---

## Phase 3: Public Documentation & Repository

### 1. Documentation
- `README.md` with:
  - Project description
  - Install/setup instructions
  - Contract summaries
- `/docs/` folder:
  - Vision
  - Use cases
  - System architecture
  - Public onboarding guide
  - FAQ

### 2. GitHub Setup
- [ ] Organize repo folders:

```
us-public-chain/
├── contracts/          # Smart contracts for PAT and USDC logic
├── frontend/           # User interface for recipients, workers, and the public
├── data/               # Token flow simulation and program analytics
├── docs/               # System philosophy, use cases, and public onboarding
├── scripts/            # Deployment and contract management
└── README.md           # This file
```

- [ ] Add MIT or GPL license
- [ ] Enable GitHub Discussions for community feedback

---

## Phase 4: Future Features

- [ ] Mobile wallet UI for recipients
- [ ] DAO-based local budgeting
- [ ] Token-based voting system
- [ ] City/state pilot partnership docs
- [ ] Public worker salary audit portal

---

## Notes

- Contracts should favor upgradability via proxy pattern or redeployable logic.
- Privacy layers must anonymize data but maintain public verification.
- Keep initial systems simple and focus on proving the *flow* and *transparency*.