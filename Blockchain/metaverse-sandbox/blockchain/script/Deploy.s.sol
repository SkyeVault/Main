// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "forge-std/Script.sol";
import "../src/LoreleiNobleGenesis.sol";

contract Deploy is Script {
    function run() external {
        vm.startBroadcast();

        new LoreleiNobleGenesis("ipfs://bafybeihdo27nu3iak7njllgpkmx3ra27mbazlrr444t4sdp46z3sn2v5ye/");

        vm.stopBroadcast();
    }
}
