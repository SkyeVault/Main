use revm::{Context, Database, Evm, Handler};

fn main() {
    let context = Context::default();
    let handler = Handler::default();

    let evm = Evm::new(context, handler);

    println!("EVM successfully initialized!");
}
