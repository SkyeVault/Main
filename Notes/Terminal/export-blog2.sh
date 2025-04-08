#!/bin/bash

# Path to markdown blog posts
INPUT_DIR="rainkeep/src/content/blog2"
# Output folder outside repo
OUTPUT_DIR="$HOME/blog2"
# Path to the Pandoc template
TEMPLATE="rainkeep/arynwood-template.html"

# Make sure output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop through all markdown files
for file in "$INPUT_DIR"/*.md; do
  filename=$(basename "$file" .md)
  outfile="$OUTPUT_DIR/${filename}.html"
  echo "Exporting $filename..."
  pandoc "$file" -o "$outfile" \
    --template="$TEMPLATE" \
    --metadata title="$filename" \
    --metadata date="${filename:6:8}" # Extract date from DevLogYYMMDD
done

echo "All blog posts exported to $OUTPUT_DIR"