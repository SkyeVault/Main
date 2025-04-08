#!/bin/bash

# Define project root directory
PROJECT_ROOT="$HOME/main/rust_projects/Netflix-recommendation-tool"

# Create main project directory
mkdir -p "$PROJECT_ROOT"

# Create Backend (Rust Axum)
mkdir -p "$PROJECT_ROOT/backend/src"
cd "$PROJECT_ROOT/backend"
cargo init
touch src/main.rs
echo '[dependencies]
axum = "0.6"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
reqwest = { version = "0.11", features = ["json"] }
dotenv = "0.15"' > Cargo.toml

# Create main.rs with basic Axum setup
echo 'use axum::{routing::get, Router};
use std::net::SocketAddr;

async fn hello_world() -> String {
    "Hello, Netflix AI Recommender!".to_string()
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(hello_world));
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    axum::Server::bind(&addr).serve(app.into_make_service()).await.unwrap();
}' > src/main.rs

# Create Frontend (Next.js)
cd "$PROJECT_ROOT"
npx create-next-app@latest frontend --use-npm
cd frontend
npm install tailwindcss axios

# Configure TailwindCSS
npx tailwindcss init -p
echo 'module.exports = {
  content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};' > tailwind.config.js

# Create basic frontend component
echo 'import { useState } from "react";
import axios from "axios";

export default function Home() {
    const [movies, setMovies] = useState([]);

    const fetchMovies = async () => {
        const res = await axios.get("http://localhost:3000/movies");
        setMovies(res.data);
    };

    return (
        <div className="p-5">
            <button onClick={fetchMovies} className="bg-blue-500 text-white p-2 rounded">Get Recommendations</button>
            <ul>{movies.map(m => <li key={m.imdbID}>{m.Title}</li>)}</ul>
        </div>
    );
}' > pages/index.js

# Create deployment configs
cd "$PROJECT_ROOT"
mkdir -p deployment
echo '{
  "rewrites": [{ "source": "/api/:path*", "destination": "http://localhost:3000/:path*" }]
}' > deployment/vercel.json

echo '{
  "services": { "backend": { "buildCommand": "cargo build", "startCommand": "cargo run" } }
}' > deployment/railway.json

# Create README
echo "# Netflix AI Movie Recommendation Tool
This project fetches Netflix movies using AI-powered recommendations.
## How to Run
- **Backend:** \`cd backend && cargo run\`
- **Frontend:** \`cd frontend && npm run dev\`" > README.md

# Done
echo " Project structure created at $PROJECT_ROOT"