// rainkeep/public/gallery3d/vite.config.js
export default {
  base: '/gallery3d/',
  build: {
    outDir: '../../../dist/gallery3d', // Output INTO your main site's dist
    emptyOutDir: false                 // Don't erase the rest of dist
  }
};
