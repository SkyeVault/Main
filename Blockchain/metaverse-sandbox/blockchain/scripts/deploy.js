// Deploys smart contracts to Ethereum testnet/mainnet
const { ethers } = require("hardhat");

async function main() {
    const Land = await ethers.getContractFactory("MetaverseLand");
    const land = await Land.deploy();
    await land.deployed();

    console.log("MetaverseLand deployed to:", land.address);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});

//  How to Use:
// 1. Run `npx hardhat run scripts/deploy.js --network goerli` to deploy the contract.