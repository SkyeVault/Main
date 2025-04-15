import { defineConfig } from 'vite';

export default defineConfig({
  base: '/gallery3d/',
  build: {
    outDir: '../../../dist/gallery3d',
    emptyOutDir: false
  }
});
