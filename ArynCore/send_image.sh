#!/bin/bash
source "$(dirname "$0")/config.sh"

# Check for required args
if [[ -z "$1" ]]; then
  echo "Usage: ./send_image.sh /path/to/image.jpg"
  exit 1
fi

IMAGE_PATH="$1"
[[ -f "$IMAGE_PATH" ]] || { echo "File does not exist: $IMAGE_PATH"; exit 1; }

# Create unique ID
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BASENAME=$(basename "$IMAGE_PATH")
TARGET_NAME="img_${TIMESTAMP}_${BASENAME}"
TARGET_PATH="$MEDIA_DIR/$TARGET_NAME"

# Copy image into local storage
cp "$IMAGE_PATH" "$TARGET_PATH"

# Ask for a description or caption
echo -n "Describe the image: "
read -r DESCRIPTION

# Create metadata JSON
METAFILE="$MEDIA_DIR/meta_${TIMESTAMP}.json"
jq -n \
  --arg file "$TARGET_NAME" \
  --arg desc "$DESCRIPTION" \
  --arg time "$TIMESTAMP" \
  '{filename: $file, description: $desc, timestamp: $time}' > "$METAFILE"

# Log into chat memory
{
  echo ""
  echo "You: [Image sent: $TARGET_NAME]"
  echo "Caption: $DESCRIPTION"
  echo "Assistant: (image stored for training)"
} >> "$CHATLOG_FILE"

echo "✅ Image stored at: $TARGET_PATH"
echo "📝 Metadata logged: $METAFILE"

# Optional: open the image
xdg-open "$TARGET_PATH" >/dev/null 2>&1 &
