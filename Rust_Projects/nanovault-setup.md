# NanoVault Setup and Customization Guide  

## 1. Prerequisites  
Before running NanoVault, ensure you have the following installed:  
- Rust (latest stable version)  
- Cargo package manager  
- Git  
- PostgreSQL (if using database features)  

---

## 2. Installation  

Clone the repository and navigate to the project directory:  
```sh
git clone https://github.com/yourusername/skyevault-ops.git
cd skyevault-ops/nanovault
```

Initialize the Rust project and install dependencies:  
```sh
cargo build
```

---

## 3. Running the Application  

To start the NanoVault server, run:  
```sh
cargo run
```
The default server will be available at `http://127.0.0.1:8080/`.  

---

## 4. Configuration  

NanoVault uses environment variables for configuration. Copy the example environment file and update it with your settings:  
```sh
cp .env.example .env
```
Edit `.env` to match your database credentials and API settings:  
```sh
DATABASE_URL=postgres://user:password@localhost/nanovault
API_SECRET_KEY=your_secret_key
```

---

## 5. API Endpoints  

NanoVault provides a set of API endpoints for security and file management.  

| Method | Endpoint       | Description                                   |
|--------|--------------|----------------------------------------------|
| GET    | `/`          | Returns API status message                   |
| POST   | `/scan`      | Scans a smart contract file for vulnerabilities |
| POST   | `/store`     | Securely stores a file using blockchain storage |
| GET    | `/audit-log` | Retrieves security audit logs                 |

To test an API call, use `curl`:  
```sh
curl -X GET http://127.0.0.1:8080/
```

---

## 6. Customization  

NanoVault is designed to be extendable. Modify and extend it based on your needs.  

- **Modify API Behavior:**  
  Edit `src/api/file_scan.rs` or `src/api/storage.rs` to add new API logic.  

- **Change Default Port:**  
  Update `main.rs` and modify the bind address:  
  ```rust
  .bind("127.0.0.1:8080")?
  ```

- **Enable Blockchain Storage:**  
  Implement decentralized storage by modifying `src/storage/mod.rs`.  

- **CI/CD Integration:**  
  Add automated security checks by expanding `src/ci_cd/mod.rs`.  

---

## 7. Running Tests  

To execute tests, run:  
```sh
cargo test
```
Unit tests are located in `tests/`.  

---

## 8. Deployment  

To build a release version:  
```sh
cargo build --release
```
For deployment, consider using Docker:  

```sh
docker build -t nanovault .
docker run -p 8080:8080 nanovault
```

---

## 9. Contributing  

To contribute:  
1. Fork the repository  
2. Create a feature branch  
3. Submit a pull request  

---

## 10. License  

NanoVault is released under the MIT License.