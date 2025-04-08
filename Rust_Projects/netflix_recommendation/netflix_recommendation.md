# **Netflix AI Movie Recommendation Tool – Setup Guide**  

This guide provides step-by-step instructions for setting up the **Rust + Next.js** full-stack project to build an **AI-powered movie recommendation tool**.  

---

## **1. Prerequisites**  

Before running the setup script, ensure the following are installed:  

- **Rust** ([Install via rustup.rs](https://rustup.rs/))  
- **Node.js** ([Install via nodejs.org](https://nodejs.org/))  
- **Cargo** (Rust package manager, included with Rust)  
- **npm** (Node.js package manager, included with Node)  

---

## **2. Running the Setup Script**  

### **1. Download the Setup Script**  
Save the following script as `setup_netflix_tool.sh` inside the `main/rust_projects` directory.  

### **2. Give the Script Execute Permissions**  
Run the following command to make the script executable:  
```bash
chmod +x setup_netflix_tool.sh
```

### **3. Execute the Script**  
Run the script to automatically set up the project:  
```bash
./setup_netflix_tool.sh
```
This will create the project directory at:  
```plaintext
$HOME/main/rust_projects/Netflix-recommendation-tool
```

---

## **3. Project Structure**  

The script will generate the following directory structure:  
```plaintext
Netflix-recommendation-tool
├── backend (Rust Axum)
│   ├── src
│   │   ├── main.rs (API entry point)
│   │   ├── movie_fetcher.rs (Fetches OMDB data)
│   │   ├── ai_recommender.rs (AI-based recommendations)
│   │   ├── netflix_checker.rs (Checks Netflix availability)
│   ├── Cargo.toml (Rust dependencies)
│   ├── .env (API keys)
├── frontend (Next.js)
│   ├── pages
│   │   ├── index.js (Movie search UI)
│   │   ├── results.js (Displays recommendations)
│   ├── components
│   │   ├── MovieCard.js (Reusable UI component)
│   ├── styles
│   ├── package.json
│   ├── tailwind.config.js
├── database (PostgreSQL or Firebase Firestore)
│   ├── schema.sql (PostgreSQL schema)
│   ├── firebase-config.js (If using Firebase)
├── deployment
│   ├── Dockerfile (Optional, for backend containerization)
│   ├── vercel.json (Frontend deployment config)
│   ├── railway.json (Backend deployment config)
├── README.md (Setup instructions)
├── .gitignore
```

---

## **4. Running the Project**  

### **Running the Backend**  

1. Navigate to the backend directory:  
```bash
cd backend
```
2. Run the Rust server:  
```bash
cargo run
```

### **Running the Frontend**  

1. Navigate to the frontend directory:  
```bash
cd frontend
```
2. Install dependencies:  
```bash
npm install
```
3. Start the frontend server:  
```bash
npm run dev
```

Once running, access the frontend at:  
```
http://localhost:3000
```
And the backend at:  
```
http://localhost:3000/movies
```

---

## **5. Deployment**  

### **Frontend Deployment**  
Deploy the **Next.js frontend** using Vercel:  
```bash
vercel
```

### **Backend Deployment**  
Deploy the **Rust Axum backend** using Railway:  
```bash
railway up
```

---

## **Final Notes**  

This setup provides a foundation for a **full-stack movie recommendation tool** that:  
- Fetches movie data from an external API  
- Uses AI-driven recommendations for personalized results  
- Checks Netflix availability for each suggested movie  

Modify and expand the project as needed. Future enhancements may include:  
- **User authentication and watch history tracking**  
- **Improved AI models for smarter recommendations**  
- **Additional streaming service availability checks**  

This guide ensures a **structured and maintainable development process**. Let me know if further refinements are needed.