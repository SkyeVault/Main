// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721, Ownable, and Royalty contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";

contract SyrenworkNFT is ERC721URIStorage, IERC2981, Ownable {
    uint256 private _nextTokenId;
    string private _contractURI;
    mapping(uint256 => string) private _stories;

    // Royalty Info: 10% to the contract owner
    address private _royaltyReceiver;
    uint96 private _royaltyFeeBps = 1000; // 10% in basis points (1000 = 10%)

    constructor(string memory contractMetadataURI) ERC721("SyrenworkNFT", "SYREN") {
        _contractURI = contractMetadataURI;
        _royaltyReceiver = msg.sender; // Royalties go to the contract owner
    }

    // Minting function to create new NFTs
    function mintNFT(address to, string memory metadataURI, string memory story) external onlyOwner {
        uint256 tokenId = _nextTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, metadataURI);
        _stories[tokenId] = story;
        _nextTokenId++;
    }

    // Retrieve the NFT story (Can restrict access to owners only)
    function getStory(uint256 tokenId) public view returns (string memory) {
        return _stories[tokenId];
    }

    // ERC-2981 Royalty Implementation (10% to contract owner)
    function royaltyInfo(uint256, uint256 salePrice) external view override returns (address, uint256) {
        uint256 royaltyAmount = (salePrice * _royaltyFeeBps) / 10000;
        return (_royaltyReceiver, royaltyAmount);
    }

    // OpenSea & Marketplaces use this contract URI to display collection info
    function contractURI() public view returns (string memory) {
        return _contractURI;
    }

    // Supports ERC-165 interface detection (used for royalties)
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }
}