#!/bin/bash
source "$(dirname "$0")/config.sh"

function show_header() {
  echo ""
  echo "╭────────────────────────────────────────────╮"
  echo "│              AETHER CHAT SESSION           │"
  echo "╰────────────────────────────────────────────╯"
  echo ""
}

function show_last_turns() {
  echo "Memory Snapshot:"
  echo "────────────────"
  tail -n 10 "$CHATLOG_FILE"
  echo ""
}
