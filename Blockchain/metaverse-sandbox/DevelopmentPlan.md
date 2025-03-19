Development Log

## Phase 1: Initial Three.js Virtual Museum Setup

### 1. Create the Project Structure
Set up a new folder and create the following files:

```
/museum_project
│── index.html  # Main entry point
│── main.js  # Three.js scene logic
│── models.json  # JSON file storing model links
│── assets/
│   ├── skybox.jpg  # Background texture
│   ├── floor.jpg  # Floor texture
│── styles.css  # Basic CSS styling
```

---

### 2. Develop the HTML Structure (`index.html`)
Create the base HTML file.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Syrenwork Virtual Museum</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <script type="module" src="main.js"></script>
</body>
</html>
```

---

### 3. Apply Basic Styling (`styles.css`)

```css
body { 
    margin: 0; 
    overflow: hidden; 
    font-family: Arial, sans-serif; 
}
```

---

### 4. Define the 3D Models and Their Locations (`models.json`)

```json
{
  "objects": [
    { "name": "Desk", "url": "https://w3s.link/ipfs/DESK_CID", "position": [1, 0, -3] },
    { "name": "Couch", "url": "https://w3s.link/ipfs/COUCH_CID", "position": [-2, 0, -2] },
    { "name": "Painting", "url": "https://w3s.link/ipfs/PAINTING_CID", "position": [0, 2, -4] }
  ]
}
```

- Replace `DESK_CID`, `COUCH_CID`, and `PAINTING_CID` with actual IPFS CIDs.
- The `"position"` field defines where objects appear in the room.

---

### 5. Implement Three.js (`main.js`)

```javascript
import * as THREE from 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three/examples/jsm/loaders/GLTFLoader.js';

// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 1);
scene.add(ambientLight);

// Floor
const floorTexture = new THREE.TextureLoader().load('assets/floor.jpg');
const floor = new THREE.Mesh(new THREE.PlaneGeometry(10, 10), new THREE.MeshBasicMaterial({ map: floorTexture }));
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

// Skybox (Large Windows Effect)
const skyboxTexture = new THREE.TextureLoader().load('assets/skybox.jpg');
scene.background = skyboxTexture;

// Load models dynamically from models.json
const loader = new GLTFLoader();
fetch('models.json')
  .then(response => response.json())
  .then(data => {
    data.objects.forEach(obj => {
      loader.load(obj.url, function (gltf) {
        const model = gltf.scene;
        model.position.set(...obj.position);
        model.userData.url = obj.url;
        scene.add(model);
      });
    });
  });

// Handle window resize
window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});

// Camera controls
camera.position.set(0, 2, 5);
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();
```

---

## Phase 2: Expanding the Museum with NFT Doorways

### 6. Develop Smart Contract for "Buy a Door" NFTs
- Implement an ERC-721 contract where each **door NFT** represents an artist’s gallery space.
- Store metadata that includes the **gallery link** associated with each door.
- Deploy the contract to **Polygon Mumbai (testnet)** for testing.
- Once validated, deploy to **Polygon Mainnet**.

---

### 7. Enable NFT Ownership and Interactivity in Three.js
- Modify the **doorway objects** so they are linked to **NFT ownership data**.
- When a visitor clicks on a **door**, they will be redirected to the **owner’s gallery**.

---

### 8. Enable NFT Marketplace Features
- List **door NFTs** for sale on OpenSea (Polygon).
- Allow users to **mint new door NFTs** directly from the smart contract.
- Implement a **rental system** where temporary exhibits can be set up.

---

## Phase 3: Hosting the Entire Museum on IPFS

### 9. Upload the Virtual Museum to IPFS
- Convert the **museum website** into a **static HTML/JS bundle**.
- Upload the entire folder to **Web3.Storage**.
- Retrieve the **CID** for the latest version.

---

### 10. Link Syrenwork.com to IPFS Using DNSLink
- Update **DNS records** with a **DNSLink entry** pointing to the latest IPFS CID.

Example DNS record:
```
_dnslink.syrenwork.com TXT "dnslink=/ipfs/YOUR_CID"
```

Now, **syrenwork.com automatically resolves to the latest museum version hosted on IPFS**.

---

### 11. Web2 Compatibility (Allowing Regular Browser Access)
- Web2 users can access the museum via an **IPFS gateway**:
  ```
  https://w3s.link/ipfs/YOUR_CID
  ```
- Web3 users with **Brave browser or MetaMask** can access it natively without a gateway.

---

## Future Features & Expansion

### 12. AI-Generated Story Capsules
- Implement AI-generated **time capsule narratives** linked to NFT metadata.
- Allow NFT owners to **contribute historical updates** over time.

---

### 13. Community Collaboration & Artist Rentals
- Allow artists to **rent short-term space for limited-time exhibitions**.
- Implement **resale options** for existing gallery spaces.

---

### 14. DAO for Museum Governance
- Offer **governance rights** to long-term supporters via a DAO.
- Community votes on **museum upgrades and featured exhibitions**.

---

## Notes & Next Steps
- **Immediate Focus:** Develop the **basic museum layout & NFT minting system**.
- **Next Priority:** Host the museum on **IPFS and link Syrenwork.com**.
- **Long-Term:** Monetize by **selling gallery spaces and exclusive digital art experiences**.

---

## Development Checklist

### **Phase 1: Basic 3D Museum**
- [ ] Set up **Three.js scene** with floor and skybox.
- [ ] Load **models dynamically from IPFS**.
- [ ] Create **clickable artwork** that links to external pages.
- [ ] Deploy initial version **locally**.

### **Phase 2: NFT Doorway System**
- [ ] Develop **ERC-721 smart contract** for doors.
- [ ] Enable **NFT-based gallery ownership**.
- [ ] Integrate **NFT minting & OpenSea listing**.

### **Phase 3: Hosting & Web3 Integration**
- [ ] Upload site to **IPFS/Web3.Storage**.
- [ ] Configure **DNSLink for Syrenwork.com**.
- [ ] Ensure **Web2 users can access via IPFS gateway**.
