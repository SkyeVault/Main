import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  // THIS is the fix: generates slug from the filename
  slug: ({ defaultSlug }) => defaultSlug,

  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
  }),
});

export const collections = {
  blog,
};