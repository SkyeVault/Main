// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LoreleiNobleGenesis is ERC721URIStorage, Ownable {
    uint256 private _tokenIdCounter;
    string private baseURI;

    constructor(string memory _baseURI) ERC721("LoreleiNobleGenesis", "LNG") Ownable(msg.sender) {
        baseURI = _baseURI;
    }

    function mintNFT(address recipient) public onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _safeMint(recipient, tokenId);
        _setTokenURI(
            tokenId,
            string(abi.encodePacked(baseURI, "metadata", _toString(tokenId), ".json"))
        );
        _tokenIdCounter += 1;
    }

    function updateBaseURI(string memory newBaseURI) public onlyOwner {
        baseURI = newBaseURI;
    }

    function burn(uint256 tokenId) public {
        address owner = ownerOf(tokenId);
        require(
            _msgSender() == owner ||
            getApproved(tokenId) == _msgSender() ||
            isApprovedForAll(owner, _msgSender()),
            "Not approved to burn"
        );
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function _toString(uint256 value) internal pure returns (string memory) {
        if (value == 0) return "0";
        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
        bytes memory buffer = new bytes(digits);
        while (value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + uint256(value % 10)));
            value /= 10;
        }
        return string(buffer);
    }
}
