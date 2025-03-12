// MapViewer.js - Renders the metaverse map using Three.js
import * as THREE from "three";
import { useEffect } from "react";

const MapViewer = () => {
    useEffect(() => {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        camera.position.z = 5;
        renderer.render(scene, camera);
    }, []);

    return null;
};

export default MapViewer;

// How to Use:
// - Import `<MapViewer />` in a React component to display the metaverse map.