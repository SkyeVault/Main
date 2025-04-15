import * as THREE from 'https://esm.sh/three@0.158.0';
import { OrbitControls } from 'https://esm.sh/three@0.158.0/examples/jsm/controls/OrbitControls.js';

const canvas = document.querySelector('#scene');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
scene.background = new THREE.Color('#0d0f1c');

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 6, 10);
camera.lookAt(0, 0, 0);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.maxPolarAngle = Math.PI / 2;
controls.target.set(0, 5, 0);
controls.update();

scene.add(new THREE.AmbientLight('#b48eff', 1));
const moonlight = new THREE.DirectionalLight('#ffffff', 0.5);
moonlight.position.set(5, 10, 5);
scene.add(moonlight);

const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(100, 100),
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

const moonGlow = new THREE.PointLight('#b48eff', 2, 100);
moonGlow.position.set(0, 8, -22);
scene.add(moonGlow);

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();
