// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract EmergencyStop {
    address public owner;
    bool public stopped = false;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    modifier stopInEmergency() {
        require(!stopped, "Contract is paused");
        _;
    }

    function toggleEmergencyStop() public onlyOwner {
        stopped = !stopped;
    }

    function withdraw() public stopInEmergency {
        // Withdraw logic
    }
}