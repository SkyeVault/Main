Virtual Museum - Doors NFT Implementation

## **Phase 1: Setting Up NFT Doorways in the Virtual Museum**

### **1. Overview of NFT Doorways**
The goal is to create **NFT-based doorways** that function as **entry points** to different galleries. These door NFTs will:
- Represent **ownership of a virtual space** within the museum.
- Allow owners to **set and update their destination links**.
- Be fully **interactive in Three.js**, enabling visitors to enter different spaces.
- Remain **separate from the 3D model**, allowing repositioning without changing ownership.

---

## **Phase 2: Smart Contract for NFT Door Ownership**

### **2. Smart Contract Implementation**
The contract:
- **Mints NFT doors** with metadata.
- **Stores a `destinationURL` that owners can update**.
- **Restricts updates to the NFT owner only**.
- **Emits an event when a door’s URL is updated**, allowing Three.js to refresh dynamically.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MuseumDoors is ERC721URIStorage, Ownable {
    uint256 private _nextTokenId;
    mapping(uint256 => string) private _doorMetadata; // Stores metadata links

    event DoorMetadataUpdated(uint256 indexed tokenId, string newMetadata);

    constructor() ERC721("MuseumDoor", "DOOR") {}

    function mintDoor(address to, string memory metadataURI) external onlyOwner {
        uint256 tokenId = _nextTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, metadataURI);
        _doorMetadata[tokenId] = metadataURI;
        _nextTokenId++;
    }

    function updateDoorMetadata(uint256 tokenId, string memory newMetadata) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can update this door's metadata");
        _doorMetadata[tokenId] = newMetadata;
        _setTokenURI(tokenId, newMetadata);
        emit DoorMetadataUpdated(tokenId, newMetadata);
    }

    function getDoorMetadata(uint256 tokenId) public view returns (string memory) {
        return _doorMetadata[tokenId];
    }
}
```

---

## **Phase 3: Three.js Integration with the Smart Contract**

### **3. Fetching Door Data from the Blockchain**
Three.js will retrieve NFT metadata, including door destinations.

```javascript
async function loadDoorDestinations() {
    const contractAddress = "0xYOUR_CONTRACT_ADDRESS";
    const abi = [
        "function getDoorDestination(uint256 tokenId) public view returns (string memory)"
    ];
    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contract = new ethers.Contract(contractAddress, abi, provider);
    
    for (let i = 0; i < totalDoors; i++) {
        const destination = await contract.getDoorDestination(i);
        doorNFTs[i].destination = destination;
    }
}
```

---

### **4. Making Doors Clickable in Three.js**
This will allow visitors to click on doors and be redirected to the gallery set by the NFT owner.

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

window.addEventListener('click', function(event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(scene.children, true);

    if (intersects.length > 0) {
        const clickedObject = intersects[0].object;
        if (clickedObject.userData.nftId !== undefined) {
            window.open(doorNFTs[clickedObject.userData.nftId].destination, "_blank");
        }
    }
});
```

---

## **Phase 4: Updating Doors Without Changing Ownership**

### **5. Moving Doors in the Museum Space**
Since doors are just **3D objects in Three.js**, they can be repositioned **without affecting NFT ownership**.

```javascript
doorNFTs[0].position.set(3, 0, -2); // Move door 0 to a new location
```

### **6. Listening for Door Destination Updates**
If an NFT owner updates their door’s URL, Three.js will **detect and refresh it in real-time**.

```javascript
contract.on("DoorDestinationUpdated", (tokenId, newDestination) => {
    doorNFTs[tokenId].destination = newDestination;
});
```

---

## **Phase 5: Allowing NFT Owners to Change Their Door Image**

### **7. Dynamic Metadata for Custom Door Images**
NFT owners can replace their door image with **any other image**, including **different doors, abstract portals, or objects like tacos or bells**.

### **How It Works**
- Each NFT stores a **metadata URL** on IPFS.
- Owners can **upload a new JSON file** with an updated `"image"` field.
- The contract allows them to **update their metadata link**, ensuring OpenSea and the museum **automatically display the new image**.

### **Metadata Example (Stored on IPFS)**
```json
{
  "name": "Custom Museum Door",
  "description": "A doorway that leads to a virtual gallery.",
  "image": "ipfs://NEW_IMAGE_CID",
  "destination": "https://artist-gallery.com"
}
```

### **Updating the Door Metadata**
```solidity
function updateDoorMetadata(uint256 tokenId, string memory newMetadata) external {
    require(ownerOf(tokenId) == msg.sender, "Only the owner can update this door's metadata");
    _doorMetadata[tokenId] = newMetadata;
    _setTokenURI(tokenId, newMetadata);
    emit DoorMetadataUpdated(tokenId, newMetadata);
}
```

### **Effect in Three.js and OpenSea**
- The NFT owner updates their metadata file.
- The new image **automatically appears** on OpenSea and inside the museum.

---

## **Final Implementation Summary**

| Feature | Implemented In |
|---------|---------------|
| Minting door NFTs | Solidity smart contract |
| Storing NFT destinations | Solidity smart contract |
| Updating NFT links | Smart contract function |
| Fetching NFT data | Three.js (Ethers.js) |
| Clicking doors to open URLs | Three.js |
| Moving doors freely | Three.js |
| Allowing owners to change door image | Smart contract + IPFS metadata |

---

## **Next Steps**

1. **Deploy the contract to Polygon Mumbai (testnet)**  
2. **Mint some test door NFTs**  
3. **Connect the contract to Three.js**  
4. **Make doors clickable & responsive**  
5. **Test updating NFT door destinations dynamically**  
6. **Test updating door images dynamically**  

Once the test version is successful, deploy to **Polygon Mainnet** and integrate it with **the full virtual museum space**.
