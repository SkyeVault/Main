const loader = new THREE.TextureLoader();
loader.load(
  'https://cdn.jsdelivr.net/gh/SkyeVault/Main@main/rainkeep/public/Arynwood/Untitled_Artwork%201.png',
  function (texture) {
    const artMaterial = new THREE.MeshBasicMaterial({ map: texture });
    const artwork = new THREE.Mesh(
      new THREE.BoxGeometry(4, 5, 0.2),
      [
        new THREE.MeshBasicMaterial({ color: '#111' }),
        new THREE.MeshBasicMaterial({ color: '#111' }),
        new THREE.MeshBasicMaterial({ color: '#111' }),
        new THREE.MeshBasicMaterial({ color: '#111' }),
        artMaterial, // front
        new THREE.MeshBasicMaterial({ color: '#111' }),
      ]
    );
    artwork.position.set(0, 5, -24.5);
    scene.add(artwork);
  },
  undefined,
  function (err) {
    console.error('Error loading artwork texture:', err);
  }
);