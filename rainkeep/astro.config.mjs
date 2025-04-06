// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { astroContent } from '@astrojs/content';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://example.com',
  integrations: [
    astroContent(),
    mdx(),
    sitemap()
  ],

  vite: {
    plugins: [tailwindcss()],
  },
});
