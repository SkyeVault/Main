 TopSecurityNFT Deployment Recap (Polygon Amoy)

**Network:** Polygon Amoy (chain ID: 80002)  
**Contract Address:** `0xE85f1711AbFb46b43220521a67519ae28c0c56fA`  
**Deployer Address:** `0xa0046753e7f9Ccb1A52876055c06d47ABfb84EaB`  
**Explorer:** [Polygonscan Amoy](https://amoy.polygonscan.com/address/0xE85f1711AbFb46b43220521a67519ae28c0c56fA)

---

## Metadata Hosting (IPFS)

- **CID:** `bafybeic2f7dtbhcph4q72ja4avhesovmhmbdmpjtc45brtwbqyfroqsr3y`  
- **Base URI Format in Contract:**

```solidity
string public baseURI = "ipfs://bafybeic2f7dtbhcph4q72ja4avhesovmhmbdmpjtc45brtwbqyfroqsr3y/";
```

- **Example tokenURI:**

`ipfs://bafy.../metadata1.json`

---

## Contract Deployment with Foundry

### .env Template (Do NOT include in GitHub)

```env
DEPLOYER_ADDRESS=0xa0046753e7f9Ccb1A52876055c06d47ABfb84EaB
PRIVATE_KEY=your_private_key_here
```

### script/Deploy.s.sol

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../src/TopSecurityNFT.sol";

contract Deploy is Script {
    function run() external {
        address initialOwner = vm.envAddress("DEPLOYER_ADDRESS");
        vm.startBroadcast();
        new TopSecurityNFT(initialOwner);
        vm.stopBroadcast();
    }
}
```

### Deployment Command

```bash
forge script script/Deploy.s.sol:Deploy \
  --rpc-url https://rpc-amoy.polygon.technology \
  --broadcast \
  --legacy \
  --sender $DEPLOYER_ADDRESS \
  --private-key $PRIVATE_KEY
```

---

## Minting NFT

### Mint token ID 1 to your wallet

```bash
cast send \
  --rpc-url https://rpc-amoy.polygon.technology \
  --private-key $PRIVATE_KEY \
  0xE85f1711AbFb46b43220521a67519ae28c0c56fA \
  "mintNFT(address)" 0xa0046753e7f9Ccb1A52876055c06d47ABfb84EaB
```

- **Tx Hash:** `0x3ada7045â¦f09fb72`

### View on OpenSea:

[OpenSea Amoy Testnet](https://testnets.opensea.io/assets/amoy/0xE85f1711AbFb46b43220521a67519ae28c0c56fA/1)

---

## .gitignore Setup

Add the following to your `.gitignore`:

```gitignore
.env
broadcast/
cache/
out/
foundry.toml.lock
```

---

## Next Steps

- Reuse the `mintNFT()` function for the next 9 tokens
- Create a batch minting script
- Add a minting interface
- Launch your Metaverse NFT Gallery front-end
