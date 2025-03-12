// Rust Axum API entry point
// This file initializes the Rust backend API for handling metaverse requests.

use axum::{Router, routing::get};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(|| async { "Metaverse Backend Running" }));
    
    let addr = SocketAddr::from(([0, 0, 0, 0], 3000));
    println!("Listening on {}", addr);
    
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}

// How to Use:
// 1. Run `cargo run` to start the backend.
// 2. Visit `http://localhost:3000` in your browser.