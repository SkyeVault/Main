// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title MultiCurrencyConversion
/// @notice Allows minting an NFT with USDC, WETH, or MATIC (Polygon native token)
contract MultiCurrencyConversion is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;
    string public baseURI;

    IERC20 public usdc;
    IERC20 public weth;

    uint256 public priceInMatic = 1 ether; // 1 MATIC
    uint256 public priceInUSDC = 1 * 10**6; // 1 USDC (USDC has 6 decimals)
    uint256 public priceInWETH = 0.001 ether; // 0.001 WETH

    constructor(
        string memory _baseURI,
        address _usdc,
        address _weth
    ) ERC721("MultiCurrencyNFT", "MCNFT") {
        baseURI = _baseURI;
        usdc = IERC20(_usdc);
        weth = IERC20(_weth);
    }

    function setPrices(uint256 maticPrice, uint256 usdcPrice, uint256 wethPrice) external onlyOwner {
        priceInMatic = maticPrice;
        priceInUSDC = usdcPrice;
        priceInWETH = wethPrice;
    }

    function mintWithMatic() external payable {
        require(msg.value == priceInMatic, "Incorrect MATIC amount");
        _mintTo(msg.sender);
    }

    function mintWithUSDC() external {
        require(usdc.transferFrom(msg.sender, address(this), priceInUSDC), "USDC payment failed");
        _mintTo(msg.sender);
    }

    function mintWithWETH() external {
        require(weth.transferFrom(msg.sender, address(this), priceInWETH), "WETH payment failed");
        _mintTo(msg.sender);
    }

    function _mintTo(address recipient) internal {
        uint256 tokenId = nextTokenId++;
        _safeMint(recipient, tokenId);
        _setTokenURI(tokenId, string(abi.encodePacked(baseURI, Strings.toString(tokenId), ".json")));
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
        usdc.transfer(owner(), usdc.balanceOf(address(this)));
        weth.transfer(owner(), weth.balanceOf(address(this)));
    }
}