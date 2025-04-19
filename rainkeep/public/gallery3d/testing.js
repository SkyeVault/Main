
import * as THREE from 'https://esm.sh/three@0.158.0';
import { OrbitControls } from 'https://esm.sh/three@0.158.0/examples/jsm/controls/OrbitControls.js';

// Setup canvas and renderer
const canvas = document.querySelector('#scene');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 4.0;

// Scene and camera
const scene = new THREE.Scene();
scene.background = new THREE.Color('#0d0f1c');

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 6, 15);
camera.lookAt(0, 5, 0);

// Orbit controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.08;
controls.rotateSpeed = 0.3;
controls.zoomSpeed = 0.25;
controls.panSpeed = 0.4;
controls.minDistance = 5;
controls.maxDistance = 30;
controls.maxPolarAngle = Math.PI / 2;
controls.target.set(0, 5, 0);
controls.update();

if ('ontouchstart' in window) {
  controls.enablePan = false;
  controls.maxPolarAngle = Math.PI / 3;
}

// Lighting
scene.add(new THREE.AmbientLight('#b48eff', 0.2));
const topFill = new THREE.PointLight('#ffffff', 20, 30);
topFill.position.set(0, 10, 0);
scene.add(topFill);

// Floor and walls
const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(50, 50),
  new THREE.MeshStandardMaterial({ color: '#b8a0cc', roughness: 0.4, metalness: 0.1 })
);
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

const wallMaterial = new THREE.MeshStandardMaterial({ color: '#2b2b2b' });
const wallPositions = [
  { pos: [-17.5, 5, -25], size: [15, 10, 0.5] },
  { pos: [17.5, 5, -25], size: [15, 10, 0.5] },
  { pos: [0, 5, 25], size: [50, 10, 0.5] },
  { pos: [-25, 5, 0], size: [0.5, 10, 50] },
  { pos: [25, 5, 0], size: [0.5, 10, 50] }
];
wallPositions.forEach(w => {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(...w.size), wallMaterial);
  mesh.position.set(...w.pos);
  scene.add(mesh);
});

// Window
const rhineView = new THREE.Mesh(
  new THREE.PlaneGeometry(30, 10),
  new THREE.MeshBasicMaterial({ color: '#b48eff', transparent: true, opacity: 0.2, side: THREE.DoubleSide })
);
rhineView.position.set(0, 5, -24.9);
scene.add(rhineView);

const moonGlow = new THREE.PointLight('#b48eff', 2, 100);
moonGlow.position.set(0, 8, -22);
scene.add(moonGlow);

// Artwork
const loader = new THREE.TextureLoader();
const canvasWidth = 4.5;
const canvasHeight = 6.2;
const canvasDepth = 0.25;

function addArtwork(i, x, y, z, rotationY, lightColor = '#ffffff') {
  const url = `https://cdn.jsdelivr.net/gh/SkyeVault/Main@main/rainkeep/public/Arynwood/Untitled_Artwork%20${i}.png`;
  loader.load(url, function (texture) {
    const material = new THREE.MeshStandardMaterial({ map: texture, roughness: 0.5, metalness: 0.3 });
    const sideMaterial = new THREE.MeshStandardMaterial({ color: '#111' });
    const artwork = new THREE.Mesh(
      new THREE.BoxGeometry(canvasWidth, canvasHeight, canvasDepth),
      [sideMaterial, sideMaterial, sideMaterial, sideMaterial, material, sideMaterial]
    );
    artwork.position.set(x, y, z);
    artwork.rotation.y = rotationY;
    scene.add(artwork);

    const light = new THREE.PointLight(lightColor, 4, 10);
    light.position.set(x, y + 1.5, z + 0.5);
    scene.add(light);
  });
}

// Manual placements
addArtwork(1, -18, 5.2, -24.5, 0);
addArtwork(2, 0, 5.2, -24.5, 0);
addArtwork(3, 18, 5.2, -24.5, 0);
addArtwork(4, -18, 5.2, 24.5, Math.PI);
addArtwork(5, 0, 5.2, 24.5, Math.PI);
addArtwork(6, 18, 5.2, 24.5, Math.PI);
addArtwork(7, -24.5, 5.2, -18, Math.PI / 2);
addArtwork(8, -24.5, 5.2, 0, Math.PI / 2);
addArtwork(9, -24.5, 5.2, 18, Math.PI / 2);
addArtwork(10, 24.5, 5.2, -18, -Math.PI / 2);

// Animation
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();
