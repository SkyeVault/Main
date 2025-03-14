// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaverseLand is ERC721, Ownable {
    constructor() ERC721("MetaverseLand", "MTL") Ownable(msg.sender) {}

    // Example function (replace with your own logic)
    function mintLand(address to, uint256 tokenId) external onlyOwner {
        _safeMint(to, tokenId);
    }
}

// How to Use:
// 1. Deploy the contract with Hardhat or Foundry.
// 2. Call `mintLand(userAddress)` to assign land NFTs.