// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// ERC-721 NFT contract for virtual land ownership in the metaverse.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaverseLand is ERC721, Ownable {
    uint256 public nextLandId;
    
    constructor() ERC721("MetaverseLand", "MLAND") {}

    function mintLand(address to) public onlyOwner {
        _mint(to, nextLandId);
        nextLandId++;
    }
}

// How to Use:
// 1. Deploy the contract with Hardhat or Foundry.
// 2. Call `mintLand(userAddress)` to assign land NFTs.