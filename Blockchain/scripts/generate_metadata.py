import json
import os

# Define the NFT metadata
nft_data = [
    {
        "name": "Aurora's Echo",
        "description": "A feathered traveler bathed in the hues of dawn, its sapphire wings carrying the whispers of an unspoken melody.",
        "cid": "bafybeicgvw3jccyjhtg7o3lfjlii6nru5dowejevwgbgetvgjb3wjnlqcq",
        "file": "painting_01.png"
    },
    {
        "name": "Nocturne Watcher",
        "description": "Perched in the embrace of twilight, eyes like amethyst lanterns pierce the dark, guarding the secrets of the night.",
        "cid": "bafybeidmsqhy7wxamg4vofxx66jhnfffmk4holhxvftbicqyse4lowozr4",
        "file": "painting_02.png"
    },
    {
        "name": "Crimson Soliloquy",
        "description": "A lone ember against the jade mist, its call a poetic hymn to the shifting winds of time.",
        "cid": "bafybeifthhmms575d4lma42lep6dun2nkoh7qgufyeivovgx6fxioa3y5u",
        "file": "painting_03.png"
    },
    {
        "name": "Ancient Reverie",
        "description": "A gentle titan, draped in cosmic hues, walks between memory and myth, where the earth hums beneath its feet.",
        "cid": "bafybeigocxlcnfdufqqqfxouupkjvb5g5t47oqekmj7sm3z6u3awxqm44q",
        "file": "painting_04.png"
    },
    {
        "name": "Celestial Bloom",
        "description": "A fiery blossom kissed by the stars, its golden heart shimmering with the pulse of the universe.",
        "cid": "bafybeigjpgyj37i3o2btlfhmgnl5fw7zjgzavf3z66vs2xuvvbzprdxz6u",
        "file": "painting_05.png"
    },
    {
        "name": "Enchanted Haven",
        "description": "A sanctuary of emerald whispers and violet dreams, where the fountain sings and flowers waltz in the glow of unseen magic.",
        "cid": "bafybeifjpa7xwhfstt44sqj4fk5rm44d74t4dk2vlhrymu7usmwmkagtaa",
        "file": "painting_06.png"
    },
    {
        "name": "Phantom Locomotive",
        "description": "A spectral train rides through the mist of forgotten dreams, its wheels turning through echoes of time and neon shadows.",
        "cid": "bafybeiczfi643ge6dc3fx6b3pynqwodvfc33xa52m5nblnjgpezgflvr4u",
        "file": "painting_07.png"
    },
    {
        "name": "Lighthouse of the Forgotten",
        "description": "A beacon flickers against the violet dusk, calling to lost souls drifting on the tides of longing.",
        "cid": "bafybeie2tqiandqmgp7xbirtsa3yz6b3h6emjbc4z4kb2myhkc3qz5k53e",
        "file": "painting_08.png"
    },
    {
        "name": "Sanctuary by the River",
        "description": "A hidden refuge cradled in the arms of towering sentinels, its windows aglow with stories left untold.",
        "cid": "bafybeib5g4niy3ht2lxntgniianxryyg2khizb547icvub5n52wq7gty7y",
        "file": "painting_09.png"
    },
    {
        "name": "Drifting in Eternity",
        "description": "A solitary boat floats upon an ocean of indigo dreams, tethered to the silent whispers of the horizon.",
        "cid": "bafybeift3am3yjr46sb2o64nmjg5pjmxp6vhgj42qrwe7knfkkkco3sdyu",
        "file": "painting_10.png"
    }
]

# Define the save path
save_path = os.path.expanduser("~/2025NFT/metadata")
os.makedirs(save_path, exist_ok=True)

# Generate JSON files
for i, nft in enumerate(nft_data, start=1):
    filename = os.path.join(save_path, f"metadata{i}.json")
    image_ipfs = f"ipfs://{nft['cid']}/{nft['file']}"
    data = {
        "name": nft["name"],
        "description": nft["description"],
        "image": image_ipfs
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

print(f"Metadata files created in: {save_path}")
