// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/gallery3d/',
  build: {
    outDir: '../../../dist/gallery3d', // places build output inside your main site's dist folder
    emptyOutDir: false                 // prevents deleting the rest of the dist folder
  }
});
