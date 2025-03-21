import json
import os

# Define the NFT metadata
nft_data = [
    {
        "name": "Aurora's Echo",
        "description": """A feathered traveler bathed in the hues of dawn, 
        its sapphire wings carrying the whispers of an unspoken melody.""",
        "image": "ipfs://bafybeicgvw3jccyjhtg7o3lfjlii6nru5dowejevwgbge..."
    },
    {
        "name": "Nocturne Watcher",
        "description": """Perched in the embrace of twilight, 
        eyes like amethyst lanterns pierce the dark, guarding the secrets of the night.""",
        "image": "ipfs://bafybeidmsqhy7wxamg4vofxx66jhnfffmk4holhxvftbi..."
    },
    {
        "name": "Crimson Soliloquy",
        "description": """A lone ember against the jade mist, 
        its call a poetic hymn to the shifting winds of time.""",
        "image": "ipfs://bafybeifthhmms575d4lma42lep6dun2nkoh7qgufyeivo..."
    },
    {
        "name": "Ancient Reverie",
        "description": """A gentle titan, draped in cosmic hues, 
        walks between memory and myth, where the earth hums beneath its feet.""",
        "image": "ipfs://bafybeigocxlcnfdufqqqfxouupkjvb5g5t47oqekmj7sm..."
    },
    {
        "name": "Celestial Bloom",
        "description": """A fiery blossom kissed by the stars, 
        its golden heart shimmering with the pulse of the universe.""",
        "image": "ipfs://bafybeigjpgyj37i3o2btlfhmgnl5fw7zjgzavf3z66vs2..."
    },
    {
        "name": "Enchanted Haven",
        "description": """A sanctuary of emerald whispers and violet dreams, 
        where the fountain sings and flowers waltz in the glow of unseen magic.""",
        "image": "ipfs://bafybeicdmrth8vlqzx7lj3o6dqx3xj5x5ax6f76cxhmox..."
    },
    {
        "name": "Phantom Locomotive",
        "description": """A spectral train rides through the mist of forgotten dreams, 
        its wheels turning through echoes of time and neon shadows.""",
        "image": "ipfs://bafybeicvgw3zmpo7nzjxqk6fqvpbht4nzw5hqxdhgfzyh..."
    },
    {
        "name": "Lighthouse of the Forgotten",
        "description": """A beacon flickers against the violet dusk, 
        calling to lost souls drifting on the tides of longing.""",
        "image": "ipfs://bafybeicfzwppmv7jtmysx6bv7xyl2t24khqlo2wxf73lq..."
    },
    {
        "name": "Sanctuary by the River",
        "description": """A hidden refuge cradled in the arms of towering sentinels, 
        its windows aglow with stories left untold.""",
        "image": "ipfs://bafybeibj76gsgfzf5xftw47kwuzlpnj7qzebqndhgjvtn..."
    },
    {
        "name": "Drifting in Eternity",
        "description": """A solitary boat floats upon an ocean of indigo dreams, 
        tethered to the silent whispers of the horizon.""",
        "image": "ipfs://bafybeicdmqwf7h2s5vygbtlyq62uytbqf4qv2yknpjbfy..."
    }
]

# Define the save path
save_path = os.path.expanduser("~/NFT2025/metadata")
os.makedirs(save_path, exist_ok=True)

# Generate JSON files
for i, nft in enumerate(nft_data, start=1):
    filename = os.path.join(save_path, f"metadata{i}.json")
    with open(filename, "w") as f:
        json.dump(nft, f, indent=4)

print(f"Metadata files created in: {save_path}")
