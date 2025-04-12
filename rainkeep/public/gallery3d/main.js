import { OrbitControls } from 'https://cdn.skypack.dev/three/examples/jsm/controls/OrbitControls.js';
import * as THREE from 'https://unpkg.com/three@0.158.0/build/three.module.js';

// Renderer setup
const canvas = document.querySelector('#scene');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// Scene and camera
const scene = new THREE.Scene();
scene.background = new THREE.Color('#0d0f1c');

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 6, 10);  // Raise the camera up and pull back
camera.lookAt(0, 0, 0);

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // Smooth motion
controls.dampingFactor = 0.05;
controls.enablePan = false;
controls.maxPolarAngle = Math.PI / 2; // Prevent flipping
controls.target.set(0, 1.6, 0); // Focus on gallery center

// Lights
const ambientLight = new THREE.AmbientLight('#b48eff', 1);
scene.add(ambientLight);

const moonlight = new THREE.DirectionalLight('#ffffff', 0.5);
moonlight.position.set(5, 10, 5);
scene.add(moonlight);

// Floor
const floorGeometry = new THREE.PlaneGeometry(100, 100);
const floorMaterial = new THREE.MeshStandardMaterial({
  color: '#b8a0cc',
  roughness: 0.4,
  metalness: 0.1,
});
const floor = new THREE.Mesh(floorGeometry, floorMaterial);
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

// Wall material (charcoal grey)
const wallMaterial = new THREE.MeshStandardMaterial({ color: '#2b2b2b' });

// Left side of the back wall
const backWallLeft = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 0.5), wallMaterial);
backWallLeft.position.set(-17.5, 5, -25);
scene.add(backWallLeft);

// Right side of the back wall
const backWallRight = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 0.5), wallMaterial);
backWallRight.position.set(17.5, 5, -25);
scene.add(backWallRight);


// Front wall (with doorway to cut later)
const frontWall = new THREE.Mesh(new THREE.BoxGeometry(50, 10, 0.5), wallMaterial);
frontWall.position.set(0, 5, 25);
scene.add(frontWall);

// Left wall
const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, 10, 50), wallMaterial);
leftWall.position.set(-25, 5, 0);
scene.add(leftWall);

// Right wall
const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, 10, 50), wallMaterial);
rightWall.position.set(25, 5, 0);
scene.add(rightWall);

// Rhine river glowing night view (background plane)
const rhineTexture = new THREE.MeshBasicMaterial({
  color: '#b48eff',
  transparent: true,
  opacity: 0.2,
  side: THREE.DoubleSide,
});

const rhineView = new THREE.Mesh(
  new THREE.PlaneGeometry(30, 10),
  rhineTexture
);
rhineView.position.set(0, 5, -24.9); // Slightly behind the back wall
scene.add(rhineView);

const moonGlow = new THREE.PointLight('#b48eff', 2, 100);
moonGlow.position.set(0, 8, -22);
scene.add(moonGlow);

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();


