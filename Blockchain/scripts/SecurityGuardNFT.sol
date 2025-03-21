// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title TopSecurityNFT
/// @author You
/// @notice NFT contract with multiple built-in security features

contract TopSecurityNFT {
    // === OWNERSHIP ===
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Zero address");
        owner = newOwner;
    }

    // === PAUSABLE ===
    bool public paused = false;

    modifier whenNotPaused() {
        require(!paused, "Contract is paused");
        _;
    }

    function pause() public onlyOwner {
        paused = true;
    }

    function unpause() public onlyOwner {
        paused = false;
    }

    // === REENTRANCY GUARD ===
    bool private locked;

    modifier noReentrancy() {
        require(!locked, "No reentrancy");
        locked = true;
        _;
        locked = false;
    }

    // === NFT-LIKE BALANCE SYSTEM (for illustration) ===
    mapping(address => uint256) public balances;

    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public noReentrancy {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No funds");
        balances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // === RATE LIMITING ===
    mapping(address => uint256) public lastActionTime;

    modifier cooldown() {
        require(block.timestamp > lastActionTime[msg.sender] + 1 minutes, "Cooldown active");
        _;
        lastActionTime[msg.sender] = block.timestamp;
    }

    function claimReward() public cooldown whenNotPaused {
        // Example reward claim logic
    }

    // === NFT MINTING (mock function) ===
    uint256 public totalSupply;
    mapping(uint256 => address) public ownerOf;

    function mint() public whenNotPaused {
        uint256 tokenId = ++totalSupply;
        ownerOf[tokenId] = msg.sender;
    }
}