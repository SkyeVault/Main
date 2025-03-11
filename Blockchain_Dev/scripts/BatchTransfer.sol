// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract BatchTransfer {
    function batchSend(address payable[] memory recipients, uint256[] memory amounts) public payable {
        require(recipients.length == amounts.length, "Mismatched arrays");

        for (uint i = 0; i < recipients.length; i++) {
            recipients[i].transfer(amounts[i]);
        }
    }
}
