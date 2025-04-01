---
title: DevLog 250325b - Deploying to Polygon Amoy
date: 2025-03-25
pubDate: 2025-03-01
description: Ongoing development log for Arynwood’s creative build process.
---
# DevLog: Deploying TopSecurityNFT to Polygon Amoy

**Date:** 2025-03-25  
**Network:** Polygon Amoy Testnet  
**Tooling:** Foundry, Web3.Storage, OpenSea, IPFS, cast

---

## Project Overview

This devlog documents the full process of deploying a smart contract called **TopSecurityNFT** to the Polygon Amoy testnet. The NFT images and metadata were hosted on IPFS using Web3.Storage.

---

## Summary

- Created and deployed `TopSecurityNFT` smart contract
- Used IPFS to store 10 metadata JSON files for NFT images
- Minted token ID `1` to the deployer's wallet
- Viewed NFT on OpenSea testnet
- Used Foundry for contract deployment and `cast` for minting
- Configured `.gitignore` to keep keys and cache private

---

## IPFS Metadata Setup

- Image Uploads: 10 PNGs to Web3.Storage
- Metadata Format (example):

```json
{
  "name": "Aurora's Echo",
  "description": "A feathered traveler bathed in the hues of dawn...",
  "image": "ipfs://<imageCID>/painting_01.png"
}
```

- Metadata Folder CID: `bafybeic2f7dtbhcph4q72ja4avhesovmhmbdmpjtc45brtwbqyfroqsr3y`
- Resulting `tokenURI`:  
  `ipfs://bafy.../metadata1.json`

---

## Smart Contract Setup

### `TopSecurityNFT.sol`

- Built with OpenZeppelin’s `ERC721URIStorage` and `Ownable`
- Constructor takes `initialOwner`
- Uses `baseURI` + token ID to generate `tokenURI`

```solidity
function tokenURI(uint256 tokenId) public view override returns (string memory) {
  return string(abi.encodePacked(baseURI, "metadata", Strings.toString(tokenId), ".json"));
}
```

---

## Deployment Workflow (Foundry)

### 1. `.env`

```env
DEPLOYER_ADDRESS=0xYourAddressHere
PRIVATE_KEY=your_private_key_here
```

### 2. Deploy Script: `script/Deploy.s.sol`

```solidity
contract Deploy is Script {
    function run() external {
        address initialOwner = vm.envAddress("DEPLOYER_ADDRESS");
        vm.startBroadcast();
        new TopSecurityNFT(initialOwner);
        vm.stopBroadcast();
    }
}
```

### 3. Deploy to Amoy:

```bash
forge script script/Deploy.s.sol:Deploy \
  --rpc-url https://rpc-amoy.polygon.technology \
  --broadcast \
  --legacy \
  --sender $DEPLOYER_ADDRESS \
  --private-key $PRIVATE_KEY
```

### Result

- Contract deployed: `0xE85f1711AbFb46b43220521a67519ae28c0c56fA`
- View on Polygonscan Amoy:  
  https://amoy.polygonscan.com/address/0xE85f1711AbFb46b43220521a67519ae28c0c56fA

---

## Minting NFTs

### Mint Token #1

```bash
cast send \
  --rpc-url https://rpc-amoy.polygon.technology \
  --private-key $PRIVATE_KEY \
  0xE85f1711AbFb46b43220521a67519ae28c0c56fA \
  "mintNFT(address)" 0xYourAddressHere
```

Transaction Hash:  
https://amoy.polygonscan.com/tx/0x3ada70455ff57e84b762dc4eaf5554fd967e69ccc81d20d9e5d8a81d9f09fb72

---

## View on OpenSea Testnet

Link:  
https://testnets.opensea.io/assets/amoy/0xE85f1711AbFb46b43220521a67519ae28c0c56fA/1

Note: IPFS images may take a few minutes to appear while OpenSea indexes metadata.

---

## .gitignore

Created `.gitignore` in project root (`~/main/blockchain/metaverse-sandbox/blockchain/`):

```gitignore
.env
broadcast/
cache/
out/
foundry.toml.lock
```

---

## Pausing the Project

Paused development to be MOMMY. The contract is fully deployed, NFT minted, and metadata hosted on IPFS.

---

## Next Steps

- Mint remaining 9 NFTs
- Write an automated minting script
- Begin work on a static or 3D NFT gallery front-end
- Push project to GitHub with clean documentation and license

---

End of session.
