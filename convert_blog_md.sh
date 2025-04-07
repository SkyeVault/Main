#!/bin/bash

# Path to your source and output directories
SOURCE_DIR="rainkeep/src/content/blog2"
OUTPUT_DIR="rainkeep/static/blog-html"
TEMPLATE_PATH="./rainkeep/pandoc-template.html"

# Make sure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop over each .md file in the source directory
for file in "$SOURCE_DIR"/*.md; do
  filename=$(basename "$file" .md)

  pandoc "$file" \
    -o "$OUTPUT_DIR/$filename.html" \
    --template="$TEMPLATE_PATH" \
    --metadata title="$filename"

  echo "✓ Converted $file → $OUTPUT_DIR/$filename.html"
done
