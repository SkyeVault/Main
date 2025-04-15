// ~/main/rainkeep/public/gallery3d/vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/gallery3d/',
  build: {
    outDir: '../../../rainkeep/dist/gallery3d',
    emptyOutDir: false
  }
});
