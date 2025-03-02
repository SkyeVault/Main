import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API authentication
SPOTIPY_CLIENT_ID = "your_client_id"
SPOTIPY_CLIENT_SECRET = "your_client_secret"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"  # Spotify requires a redirect URI

# Authenticate with Spotify
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Get the current user's ID
user_id = sp.current_user()["id"]

# Create a new playlist
playlist_name = "Clean Hip-Hop & Dance Vibes"
playlist_description = "A mix of fun, clean hip-hop and dance-friendly beats."
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

# List of songs to add (Title - Artist)
songs = [
    "Only Child - Tierra Whack",
    "Waze - Tierra Whack",
    "Diddy Bop - Noname",
    "Shadow Man - Noname",
    "Forever - Sa-Roc",
    "Goddess Gang - Sa-Roc",
    "Sassy - Rapsody",
    "Ibtihaj - Rapsody",
    "Selfish - Little Simz",
    "Gorilla - Little Simz",
    "Doo Wop (That Thing) - Lauryn Hill",
    "Rebirth of Slick (Cool Like Dat) - Digable Planets",
    "U.N.I.T.Y. - Queen Latifah",
    "Lose Control - Missy Elliott",
    "Shoop - Salt-N-Pepa",
    "The Block Party - Lisa ‘Left Eye’ Lopes",
    "Tightrope - Janelle Monáe",
    "Leave Me Alone - Kari Faux",
    "Woman - Doja Cat",
    "10% - Kaytranada"
]

# Search for the songs and get their Spotify track IDs
track_ids = []
for song in songs:
    result = sp.search(q=song, type="track", limit=1)
    if result["tracks"]["items"]:
        track_ids.append(result["tracks"]["items"][0]["id"])

# Add songs to the new playlist
if track_ids:
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_ids)
    print(f"Playlist '{playlist_name}' created successfully!")
else:
    print("No songs found. Check the song titles and try again.")