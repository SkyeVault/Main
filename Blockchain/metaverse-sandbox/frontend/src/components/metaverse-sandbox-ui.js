import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { Web3Modal } from 'web3modal';
import { Contract } from '@ethersproject/contracts';
import LAND_ABI from './contracts/LandABI.json';
import { Button, Card } from "@/components/ui";

const LAND_CONTRACT_ADDRESS = "0xYourContractAddressHere";

export default function MetaverseSandbox() {
    const [walletAddress, setWalletAddress] = useState(null);
    const [provider, setProvider] = useState(null);
    const [landTokens, setLandTokens] = useState([]);

    useEffect(() => {
        if (walletAddress) {
            fetchLandTokens();
        }
    }, [walletAddress]);

    async function connectWallet() {
        try {
            const web3Modal = new Web3Modal();
            const connection = await web3Modal.connect();
            const web3Provider = new ethers.providers.Web3Provider(connection);
            const signer = web3Provider.getSigner();
            const address = await signer.getAddress();

            setWalletAddress(address);
            setProvider(web3Provider);
        } catch (error) {
            console.error("Wallet connection failed:", error);
        }
    }

    async function fetchLandTokens() {
        if (!provider) return;
        try {
            const contract = new Contract(LAND_CONTRACT_ADDRESS, LAND_ABI, provider);
            const tokens = await contract.getOwnedLand(walletAddress);
            setLandTokens(tokens);
        } catch (error) {
            console.error("Error fetching land tokens:", error);
        }
    }

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Metaverse Sandbox</h1>
            {!walletAddress ? (
                <Button onClick={connectWallet}>Connect Wallet</Button>
            ) : (
                <p className="mb-4">Connected as: {walletAddress}</p>
            )}

            <h2 className="text-xl font-semibold mt-4">Your Virtual Land</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-2">
                {landTokens.length > 0 ? (
                    landTokens.map((token, index) => (
                        <Card key={index}>
                            <p className="text-lg font-semibold">Land ID: {token.id}</p>
                            <p className="text-sm">Coordinates: {token.coordinates}</p>
                        </Card>
                    ))
                ) : (
                    <p>No land owned.</p>
                )}
            </div>
        </div>
    );
}