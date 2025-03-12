// ERC-721 NFT Land Registry
// This module interacts with the smart contract managing virtual land ownership.

use ethers::contract::Contract;
use ethers::prelude::*;

pub async fn get_owner(land_id: u64) -> Result<Address, Box<dyn std::error::Error>> {
    let provider = Provider::<Http>::try_from("https://eth-mainnet.alchemyapi.io/v2/YOUR_API_KEY")?;
    let contract_address = "0xYourLandRegistryContractAddress".parse::<Address>()?;
    let contract = Contract::new(contract_address, include_bytes!("../contracts/MetaverseLand.abi"), provider);
    
    let owner: Address = contract.method("ownerOf", land_id)?.call().await?;
    Ok(owner)
}

//  How to Use:
// - Call `get_owner(land_id).await` to retrieve the owner of a virtual land parcel.
