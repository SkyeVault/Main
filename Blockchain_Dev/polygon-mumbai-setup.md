# Setting Up Polygon Mumbai with Foundry

Polygon Mumbai is the testnet for Polygon, allowing developers to deploy and test smart contracts before moving to the mainnet. It provides free test MATIC for transactions and supports EVM-compatible smart contracts.

## 1. Add Polygon Mumbai to MetaMask

To interact with the Mumbai testnet, add it to MetaMask:

1. Open MetaMask and click **Networks** > **Add Network**.
2. Enter the following details:
   ```
   Network Name: Polygon Mumbai
   RPC URL: https://rpc-mumbai.maticvigil.com/
   Chain ID: 80001
   Currency Symbol: MATIC
   Block Explorer URL: https://mumbai.polygonscan.com/
   ```

## 2. Get Free Mumbai Test MATIC

Mumbai requires MATIC tokens for gas fees. Use one of the following faucets to get free test MATIC:

- [Alchemy Faucet](https://faucet.polygon.technology/)
- [QuickNode Mumbai Faucet](https://faucet.quicknode.com/polygon/mumbai/)
- [Polygon Official Faucet](https://mumbaifaucet.com/)

Enter your wallet address, request MATIC, and wait for confirmation.

## 3. Install Foundry

Foundry is a powerful tool for compiling, deploying, and testing smart contracts. Install it with:

```sh
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

Verify the installation:

```sh
forge --version
```

## 4. Configure Foundry for Polygon Mumbai

Set up the Foundry project:

```sh
forge init my-metaverse-project
cd my-metaverse-project
```

Create a `.env` file with your private key:

```sh
echo "PRIVATE_KEY=your_private_key_here" > .env
```

Load environment variables:

```sh
source .env
```

## 5. Deploy a Smart Contract on Mumbai

Write a sample contract in `src/MetaverseLand.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "openzeppelin-contracts/contracts/token/ERC721/ERC721.sol";
import "openzeppelin-contracts/contracts/access/Ownable.sol";

contract MetaverseLand is ERC721, Ownable {
    constructor() ERC721("MetaverseLand", "MVL") {}
    function mintLand(address to, uint256 tokenId) public onlyOwner {
        _mint(to, tokenId);
    }
}
```

Compile the contract:

```sh
forge build
```

Deploy it on Polygon Mumbai:

```sh
forge create --rpc-url https://rpc-mumbai.maticvigil.com/ --private-key $PRIVATE_KEY src/MetaverseLand.sol:MetaverseLand
```

## 6. Verify the Contract on Polygonscan

After deploying, verify the contract on [Polygonscan Mumbai](https://mumbai.polygonscan.com/):

```sh
forge verify-contract --chain-id 80001 --watch --etherscan-api-key your_etherscan_key --constructor-args $(cast abi-encode "constructor()") <contract_address> src/MetaverseLand.sol:MetaverseLand
```

## 7. Interact with the Deployed Contract

Use `cast` to interact with the contract:

```sh
cast call <contract_address> "ownerOf(uint256)" 1 --rpc-url https://rpc-mumbai.maticvigil.com/
```

Mint a new land NFT:

```sh
cast send <contract_address> "mintLand(address,uint256)" <your_wallet_address> 2 --private-key $PRIVATE_KEY --rpc-url https://rpc-mumbai.maticvigil.com/
```

## Conclusion

Polygon Mumbai is a scalable and cost-effective environment for testing smart contracts. By using Foundry, developers can efficiently deploy and interact with smart contracts before moving to production on Polygon Mainnet. This setup provides a strong foundation for building and testing metaverse applications and blockchain-based assets.
