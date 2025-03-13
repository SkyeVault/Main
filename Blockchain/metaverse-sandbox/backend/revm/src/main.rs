use hex;
use revm::{
    db::EmptyDB,
    primitives::{Bytecode, Env, SpecId, TxEnv},
    Context,
    Evm,
    EvmContext, // ✅ Import the correct type
    Handler,
};
use std::fs;

/// Main function to load, setup, and execute a contract in REVM.
fn main() {
    // Load compiled bytecode
    let bytecode_str = fs::read_to_string("../../blockchain/bytecode.hex").expect(
        "Failed to load bytecode.hex. Ensure the file exists in ../../blockchain/bytecode.hex",
    );
    let cleaned_bytecode = bytecode_str.trim().trim_start_matches("0x");
    let bytecode_bytes = hex::decode(cleaned_bytecode).expect("Invalid hex");

    // Create contract bytecode
    let contract = Bytecode::new_raw(bytecode_bytes.into());

    // ✅ Corrected: Create an execution environment
    let mut env = Env::default();

    // Initialize the transaction environment (TxEnv)
    let mut tx_env = TxEnv::default();
    tx_env.data = contract.bytes().clone();
    env.tx = tx_env;

    // ✅ Fix: Create an EvmContext with EmptyDB (not using Env directly)
    let evm_context = EvmContext::new(EmptyDB::default());

    // ✅ Fix: Properly initialize Context with EvmContext
    let context = Context::new(evm_context, env);

    // ✅ Fix: Use Handler correctly
    let handler = Handler::mainnet_with_spec(SpecId::LATEST); // ✅ Correct

    // ✅ Fix: Properly create the EVM instance
    let mut evm = Evm::new(context, handler);

    evm.context.evm.inner.env.tx.transact_to = revm::primitives::TransactTo::Create;
    let result = evm.transact().expect("Transaction failed");

    // Output result
    println!("EVM Execution Result: {:?}", result);
}
