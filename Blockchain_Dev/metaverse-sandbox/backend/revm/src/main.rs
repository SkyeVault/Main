use revm::primitives::SpecId;
use revm::{Context, Evm, Handler};

fn main() {
    // Create a new EVM execution context
    let context = Context::default();

    // Create a new EVM handler for execution, using a default mainnet configuration
    let handler = Handler::mainnet_with_spec(SpecId::LATEST);

    // Initialize the EVM with context and handler
    let _evm = Evm::new(context, handler);

    println!("EVM successfully initialized!");
}
