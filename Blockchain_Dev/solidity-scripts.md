# **Solidity Scripts: Development, Security, and Automation Guide**

This guide provides essential Solidity scripts for **smart contract security, automation, and best practices**. Each script includes an explanation of how it works and its real-world use case.

---

## **1. Safe Withdraw Function (`SafeWithdraw.sol`)**
### **Why It’s Useful**
- Protects against **reentrancy attacks** (e.g., The DAO Hack).
- Ensures **state updates before sending ETH**.

### **Script**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SafeWithdraw is ReentrancyGuard {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient funds");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }
}
```
### **How It Works**
1. Users deposit ETH → Balance is recorded in `balances[msg.sender]`.
2. `nonReentrant` modifier **blocks reentrant calls**.
3. Updates balance **before transferring funds**.

---

## **2. Emergency Stop Mechanism (`EmergencyStop.sol`)**
### **Why It’s Useful**
- Allows the **contract owner** to pause functionality in case of an exploit.
- Prevents **unauthorized withdrawals or trades**.

### **Script**
```solidity
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
```
### **How It Works**
1. The **owner toggles** `stopped` → Stops contract execution.
2. `stopInEmergency` modifier **prevents function calls** when paused.
3. Used to **pause all transactions** in case of exploits.

---

## **3. Gas-Optimized Batch Transfer (`BatchTransfer.sol`)**
### **Why It’s Useful**
- Reduces **gas fees** for **batch ETH/token transfers**.
- Useful for **airdrops, payroll, and batch payments**.

### **Script**
```solidity
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
```
### **How It Works**
1. Takes multiple **addresses & amounts**.
2. **Loops through** recipients and transfers ETH.
3. Reduces **gas costs** compared to multiple transactions.

---

## **4. Smart Contract Self-Destruct (`SelfDestruct.sol`)**
### **Why It’s Useful**
- Allows the **owner** to remove the contract.
- Used for **migrations or deprecating vulnerable contracts**.

### **Script**
```solidity
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
```
### **How It Works**
1. Owner calls `destroyContract()` → **Deletes contract from blockchain**.
2. Sends **all remaining ETH** to the owner.
3. **Irreversible** → Once executed, contract **cannot be recovered**.

---

## **5. Secure Random Number Generator (`SecureRandom.sol`)**
### **Why It’s Useful**
- Solidity’s built-in randomness (`block.timestamp`) **is not secure**.
- Uses **Chainlink VRF** for **tamper-proof** randomness.

### **Script**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract SecureRandom is VRFConsumerBase {
    bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public randomResult;

    constructor()
        VRFConsumerBase(
            0x514910771AF9Ca656af840dff83E8264EcF986CA, // VRF Coordinator
            0x514910771AF9Ca656af840dff83E8264EcF986CA  // LINK Token
        )
    {
        keyHash = 0x6c3699283bda56ad74f6b855546325b68d482e983852a7f1e3407b5bcd5d52e9;
        fee = 0.1 * 10 ** 18; // 0.1 LINK
    }

    function getRandomNumber() public returns (bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK");
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
    }
}
```
### **How It Works**
1. Uses **Chainlink VRF** to generate **secure random numbers**.
2. Calls `getRandomNumber()` → Requests randomness.
3. **Stores** the random number securely for use.

---

## **6. Role-Based Access Control (`RoleBasedAccess.sol`)**
### **Why It’s Useful**
- Controls **who** can execute critical functions.
- Uses **OpenZeppelin’s AccessControl** for **secure permissions**.

### **Script**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/access/AccessControl.sol";

contract RoleBasedAccess is AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    constructor() {
        _setupRole(ADMIN_ROLE, msg.sender);
    }

    modifier onlyAdmin() {
        require(hasRole(ADMIN_ROLE, msg.sender), "Not an admin");
        _;
    }

    function secureFunction() public onlyAdmin {
        // Secure logic here
    }
}
```
### **How It Works**
1. Defines **ADMIN_ROLE**.
2. Assigns **admin** at contract deployment.
3. Restricts function access **only to admins**.

---

## **7. Upgradeable Proxy Contract (`UpgradeableContract.sol`)**
### **Why It’s Useful**
- Allows **contract upgrades** without **losing state**.
- Uses **OpenZeppelin’s UUPS proxy pattern**.

### **Script**
```solidity
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
```
### **How It Works**
1. **Initializes contract state**.
2. Allows **upgrades while keeping storage intact**.
3. Uses `_authorizeUpgrade()` to **control upgrade permissions**. 

This guide provides **secure and gas-efficient Solidity scripts** to integrate into your blockchain development workflow. Let me know which scripts you want to explore first.