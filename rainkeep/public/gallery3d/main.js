import * as THREE from 'https://esm.sh/three@0.158.0';
import { OrbitControls } from 'https://esm.sh/three@0.158.0/examples/jsm/controls/OrbitControls.js';

// Setup canvas and renderer
const canvas = document.querySelector('#scene');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// Improve brightness and color accuracy
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 4.0;

// Create scene and camera
const scene = new THREE.Scene();
scene.background = new THREE.Color('#0d0f1c');

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 8, -50);
camera.lookAt(0, 5, 0);

// Orbit controls for rotation and zoom
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.maxPolarAngle = Math.PI / 2;
controls.target.set(0, 5, 0);
controls.update();

// Lighting setup
scene.add(new THREE.AmbientLight('#b48eff', 0.2)); // subtle fill

const moonlight = new THREE.DirectionalLight('#ffffff', 0.5);
moonlight.position.set(5, 10, 5);
scene.add(moonlight);

const topFill = new THREE.PointLight('#ffffff', 20, 30);
topFill.position.set(0, 10, 0);
scene.add(topFill);


// Strong gallery spotlights for each wall
const spotlightBack = new THREE.PointLight('#ffffff', 20, 100);
spotlightBack.position.set(0, 9, -20);
scene.add(spotlightBack);

const spotlightFront = new THREE.PointLight('#ffffff', 20, 100);
spotlightFront.position.set(0, 9, 20);
scene.add(spotlightFront);

const spotlightLeft = new THREE.PointLight('#ffffff', 20, 100);
spotlightLeft.position.set(-20, 9, 0);
scene.add(spotlightLeft);

const spotlightRight = new THREE.PointLight('#ffffff', 20, 100);
spotlightRight.position.set(20, 9, 0);
scene.add(spotlightRight);

const spotlight = new THREE.PointLight('#ffffff', 20, 100);
spotlight.position.set(0, 8, 0);
scene.add(spotlight);
spotlight.intensity = 10;

// --- BACK WALL LIGHTS (z = -20)
const backLight1 = new THREE.PointLight('#ffffff', 15, 60);
backLight1.position.set(-15, 9, -20);
scene.add(backLight1);

const backLight2 = new THREE.PointLight('#ffffff', 15, 60);
backLight2.position.set(0, 9, -20);
scene.add(backLight2);

const backLight3 = new THREE.PointLight('#ffffff', 15, 60);
backLight3.position.set(15, 9, -20);
scene.add(backLight3);

// --- FRONT WALL LIGHTS (z = 20)
const frontLight1 = new THREE.PointLight('#ffffff', 15, 60);
frontLight1.position.set(-15, 9, 20);
scene.add(frontLight1);

const frontLight2 = new THREE.PointLight('#ffffff', 15, 60);
frontLight2.position.set(0, 9, 20);
scene.add(frontLight2);

const frontLight3 = new THREE.PointLight('#ffffff', 15, 60);
frontLight3.position.set(15, 9, 20);
scene.add(frontLight3);

// --- LEFT WALL LIGHTS (x = -20)
const leftLight1 = new THREE.PointLight('#ffffff', 15, 60);
leftLight1.position.set(-20, 9, -15);
scene.add(leftLight1);

const leftLight2 = new THREE.PointLight('#ffffff', 15, 60);
leftLight2.position.set(-20, 9, 0);
scene.add(leftLight2);

const leftLight3 = new THREE.PointLight('#ffffff', 15, 60);
leftLight3.position.set(-20, 9, 15);
scene.add(leftLight3);

// --- RIGHT WALL LIGHTS (x = 20)
const rightLight1 = new THREE.PointLight('#ffffff', 15, 60);
rightLight1.position.set(20, 9, -15);
scene.add(rightLight1);

const rightLight2 = new THREE.PointLight('#ffffff', 15, 60);
rightLight2.position.set(20, 9, 0);
scene.add(rightLight2);

const rightLight3 = new THREE.PointLight('#ffffff', 15, 60);
rightLight3.position.set(20, 9, 15);
scene.add(rightLight3);



// Floor and walls
const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(50, 50),
  new THREE.MeshStandardMaterial({ color: '#b8a0cc', roughness: 0.4, metalness: 0.1 })
);
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

const wallMaterial = new THREE.MeshStandardMaterial({ color: '#2b2b2b' });

const backWallLeft = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 0.5), wallMaterial);
backWallLeft.position.set(-17.5, 5, -25);
scene.add(backWallLeft);

const backWallRight = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 0.5), wallMaterial);
backWallRight.position.set(17.5, 5, -25);
scene.add(backWallRight);

const frontWall = new THREE.Mesh(new THREE.BoxGeometry(50, 10, 0.5), wallMaterial);
frontWall.position.set(0, 5, 25);
scene.add(frontWall);

const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, 10, 50), wallMaterial);
leftWall.position.set(-25, 5, 0);
scene.add(leftWall);

const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, 10, 50), wallMaterial);
rightWall.position.set(25, 5, 0);
scene.add(rightWall);

// Window opening
const rhineView = new THREE.Mesh(
  new THREE.PlaneGeometry(30, 10),
  new THREE.MeshBasicMaterial({
    color: '#b48eff',
    transparent: true,
    opacity: 0.2,
    side: THREE.DoubleSide
  })
);
rhineView.position.set(0, 5, -24.9);
scene.add(rhineView);

// Decorative point light near window
const moonGlow = new THREE.PointLight('#b48eff', 2, 100);
moonGlow.position.set(0, 8, -22);
scene.add(moonGlow);

// Artwork loading
const loader = new THREE.TextureLoader();
const canvasWidth = 3.5;
const canvasHeight = 5;
const spacing = 1.5;
const canvasDepth = 0.2;

let index = 1;

// BACK WALL (skip window area)
{
  const startX = -22;
  for (let i = 0; i < 10 && index <= 40; i++) {
    const posX = startX + i * (canvasWidth + spacing);
    if (posX > -15 && posX < 15) continue;
    addArtwork(index++, posX, 5, -24.5, 0);
  }
}

// FRONT WALL
{
  const startX = -22;
  for (let i = 0; i < 10 && index <= 40; i++) {
    const posX = startX + i * (canvasWidth + spacing);
    addArtwork(index++, posX, 5, 24.5, Math.PI);
  }
}

// LEFT WALL
{
  const startZ = -22;
  for (let i = 0; i < 10 && index <= 40; i++) {
    const posZ = startZ + i * (canvasWidth + spacing);
    addArtwork(index++, -24.5, 5, posZ, Math.PI / 2);
  }
}

// RIGHT WALL
{
  const startZ = -22;
  for (let i = 0; i < 10 && index <= 40; i++) {
    const posZ = startZ + i * (canvasWidth + spacing);
    addArtwork(index++, 24.5, 5, posZ, -Math.PI / 2);
  }
}

// Artwork placement function
function addArtwork(i, x, y, z, rotationY) {
  const url = `https://cdn.jsdelivr.net/gh/SkyeVault/Main@main/rainkeep/public/Arynwood/Untitled_Artwork%20${i}.png`;

  loader.load(url, function (texture) {
    const material = new THREE.MeshStandardMaterial({
      map: texture,
      roughness: 0.5,
      metalness: 0.3
    });

    const sideMaterial = new THREE.MeshStandardMaterial({ color: '#111' });

    const artwork = new THREE.Mesh(
      new THREE.BoxGeometry(canvasWidth, canvasHeight, canvasDepth),
      [
        sideMaterial, // left
        sideMaterial, // right
        sideMaterial, // top
        sideMaterial, // bottom
        material,     // front
        sideMaterial  // back
      ]
    );

    artwork.position.set(x, y, z);
    artwork.rotation.y = rotationY;
    scene.add(artwork);
  });
}

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();
