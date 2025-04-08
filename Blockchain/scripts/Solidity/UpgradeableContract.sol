// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract UpgradeableContract is Initializable, UUPSUpgradeable {
    uint256 public number;

    function initialize() public initializer {
        number = 42;
    }

    function _authorizeUpgrade(address) internal override {}
}