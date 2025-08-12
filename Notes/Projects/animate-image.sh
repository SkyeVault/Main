#!/bin/bash

IMG="output/generated.png"
OUTPUT_DIR="output/animation"
mkdir -p "${OUTPUT_DIR}"

# Run AnimateDiff inside the container (adjust path as needed)
docker exec -it animatediff python scripts/animate.py \
  --input "${IMG}" \
  --output "${OUTPUT_DIR}" \
  --motion_strength 1.0 \
  --num_frames 16

echo "Animation rendered to ${OUTPUT_DIR}"