// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaverseLand is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;
    mapping(uint256 => LandMetadata) public landDetails;

    struct LandMetadata {
        uint256 x;
        uint256 y;
        string metadataURI;
    }

    event LandMinted(address indexed owner, uint256 indexed tokenId, uint256 x, uint256 y);

    constructor() ERC721("Metaverse Land", "MLAND") {}

    function mintLand(address to, uint256 x, uint256 y, string memory metadataURI) external onlyOwner {
        uint256 tokenId = nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, metadataURI);

        landDetails[tokenId] = LandMetadata(x, y, metadataURI);
        emit LandMinted(to, tokenId, x, y);
    }
}
