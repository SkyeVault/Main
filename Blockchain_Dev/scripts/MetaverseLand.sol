// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MetaverseLand is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    struct Land {
        uint256 id;
        string coordinates;
        string metadataURI;
    }

    mapping(uint256 => Land) public landPlots;
    mapping(address => uint256[]) public ownedLand;

    event LandMinted(address owner, uint256 tokenId, string coordinates);
    event LandTransferred(uint256 tokenId, address from, address to);

    constructor() ERC721("MetaverseLand", "MVL") {}

    function mintLand(string memory coordinates, string memory metadataURI) public onlyOwner returns (uint256) {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();

        _mint(msg.sender, newItemId);
        landPlots[newItemId] = Land(newItemId, coordinates, metadataURI);
        ownedLand[msg.sender].push(newItemId);

        emit LandMinted(msg.sender, newItemId, coordinates);
        return newItemId;
    }

    function transferLand(address to, uint256 tokenId) public {
        require(ownerOf(tokenId) == msg.sender, "You do not own this land");
        _transfer(msg.sender, to, tokenId);

        // Update ownership records
        removeOwnedLand(msg.sender, tokenId);
        ownedLand[to].push(tokenId);

        emit LandTransferred(tokenId, msg.sender, to);
    }

    function getOwnedLand(address owner) public view returns (uint256[] memory) {
        return ownedLand[owner];
    }

    function removeOwnedLand(address owner, uint256 tokenId) internal {
        uint256[] storage ownerLands = ownedLand[owner];
        for (uint256 i = 0; i < ownerLands.length; i++) {
            if (ownerLands[i] == tokenId) {
                ownerLands[i] = ownerLands[ownerLands.length - 1];
                ownerLands.pop();
                break;
            }
        }
    }
}
