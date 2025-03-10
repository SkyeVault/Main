```
 netflix-ai-recommender
├── 📂 backend (Rust Axum or Python FastAPI)
│   ├── main.rs (or api.py for FastAPI)
│   ├── movie_fetcher.rs (handles OMDB API)
│   ├── ai_recommender.rs (calls OpenAI API)
│   ├── netflix_checker.rs (checks Netflix availability)
│   ├── Cargo.toml (Rust dependencies) or requirements.txt (Python)
│   ├── .env (API keys)
├── 📂 frontend (Next.js + TailwindCSS)
│   ├── 📂 pages
│   │   ├── index.js (Movie search UI)
│   │   ├── results.js (Shows recommendations)
│   ├── 📂 components
│   │   ├── MovieCard.js (Reusable UI component)
│   ├── 📂 styles
│   ├── package.json
│   ├── tailwind.config.js
├── 📂 database (PostgreSQL or Firebase Firestore)
│   ├── schema.sql (for PostgreSQL)
│   ├── firebase-config.js (if using Firebase)
├── 📂 deployment
│   ├── Dockerfile (Optional, for backend containerization)
│   ├── vercel.json (Frontend deployment config)
│   ├── railway.json (Backend deployment config)
├── README.md (Project setup & instructions)
├── .gitignore

```