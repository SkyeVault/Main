import { useState, useEffect } from "react";
import { ethers } from "ethers";

const CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS";
const ABI = [
  {
    "inputs": [{"internalType": "string","name": "_message","type": "string"}],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "message",
    "outputs": [{"internalType": "string","name":"","type":"string"}],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{"internalType": "string","name":"_newMessage","type":"string"}],
    "name": "updateMessage",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

function App() {
  const [message, setMessage] = useState("");
  const [newMessage, setNewMessage] = useState("");
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);

  useEffect(() => {
    async function loadContract() {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        setSigner(signer);

        const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
        setContract(contract);

        const currentMessage = await contract.message();
        setMessage(currentMessage);
      }
    }
    loadContract();
  }, []);

  const updateMessage = async () => {
    if (contract) {
      const tx = await contract.updateMessage(newMessage);
      await tx.wait();
      setMessage(await contract.message());
    }
  };

  return (
    <div>
      <h1>Free dApp</h1>
      <p>Stored Message: {message}</p>
      <input onChange={(e) => setNewMessage(e.target.value)} placeholder="New Message"/>
      <button onClick={updateMessage}>Update</button>
    </div>
  );
}

export default App;