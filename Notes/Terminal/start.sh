#!/bin/bash 
#saved at ./ , open terminal and run ./start

# Start ProtonVPN (OpenVPN method)
echo "Connecting to ProtonVPN..."
sudo openvpn --config ~/vpn/proton_free.ovpn --daemon

# Wait for VPN to stabilize
sleep 10

# Launch Tilix terminal
tilix &

# Launch Firefox
firefox &

# Launch Tor Browser
# Go into the Tor Browser directory
cd ~/tor-browser

# Mark it executable (if not already)
chmod +x start-tor-browser.desktop

# Launch it correctly
./start-tor-browser.desktop --detach

# Wait a moment before opening .onion site
sleep 15

# Open a decentralized email in Tor
# (Uses Tor's control port, if configured — otherwise just document it for now)
echo "Please visit: http://elude.in OR http://mail2torwwfyh2h3n.onion in Tor manually."

# Or you can instruct user:
notify-send "TOR Ready" "Open http://elude.in or http://mail2torwwfyh2h3n.onion in Tor."
