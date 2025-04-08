// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract SelfDestruct {
    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    function destroyContract() public onlyOwner {
        selfdestruct(owner);
    }
}