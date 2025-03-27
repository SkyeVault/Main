// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract TopSecurityNFT is ERC721URIStorage, Ownable {
    uint256 public currentTokenId = 1;
    string public baseURI = "ipfs://bafybeihdo27nu3iak7njllgpkmx3ra27mbazlrr444t4sdp46z3sn2v5ye/";

    constructor(address initialOwner) ERC721("TopSecurityNFT", "TSNFT") Ownable(initialOwner) {}

    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = currentTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, string(abi.encodePacked(baseURI, "metadata", Strings.toString(tokenId), ".json")));
        currentTokenId += 1;
    }

    function updateBaseURI(string memory newBaseURI) public onlyOwner {
        baseURI = newBaseURI;
    }
}
