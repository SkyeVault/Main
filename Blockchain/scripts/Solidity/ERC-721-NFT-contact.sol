// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyNFT is ERC721, Ownable {
    uint256 public nextTokenId;
    string public baseURI;

    constructor(string memory _baseURI) ERC721("Free NFT", "FNFT") {
        baseURI = _baseURI;
    }

    function mint() public {
        _safeMint(msg.sender, nextTokenId);
        nextTokenId++;
    }

    function setBaseURI(string memory _newURI) public onlyOwner {
        baseURI = _newURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}