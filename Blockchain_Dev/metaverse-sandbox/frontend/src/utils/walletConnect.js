// WalletConnect.js - Handles MetaMask and WalletConnect authentication
import { ethers } from "ethers";

export async function connectWallet() {
    if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: "eth_requestAccounts" });
        return provider.getSigner();
    } else {
        alert("Please install MetaMask!");
    }
}

//  How to Use:
// - Call `connectWallet()` to prompt the user to connect their wallet.