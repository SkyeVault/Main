use rspotify::{
    auth_code::AuthCodeSpotify,
    clients::OAuthClient,
    model::scope, Credentials, OAuth,
};
use dotenv::dotenv;
use std::{env, error::Error, io};

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    dotenv().ok(); // ✅ Load credentials from .env

    let creds = Credentials::new(
        &env::var("SPOTIFY_CLIENT_ID")?,
        &env::var("SPOTIFY_CLIENT_SECRET")?
    );

    let oauth = OAuth {
        redirect_uri: env::var("SPOTIFY_REDIRECT_URI")?.to_string(),
        scopes: scope!("playlist-modify-public", "user-library-read"),
        ..Default::default()
    };

    let spotify = AuthCodeSpotify::new(creds, oauth);

    let url = spotify.get_authorize_url(false)?;
    println!("Authorize here: {}\nEnter the code:", url);

    let mut auth_code = String::new();
    io::stdin().read_line(&mut auth_code)?;
    spotify.request_token(&auth_code.trim()).await?;

    println!("Authenticated successfully!");
    Ok(())

    // Step 2: Create Playlist "Ember Dance"
    let user = spotify.me().await?;
    let playlist = spotify
        .user_playlist_create(user.id.clone(), "Ember Dance", Some(false), None, None)
        .await?;
    
    println!("Created playlist: {}", playlist.name);

    // Step 3: Add Songs to Playlist
    let song_titles = [
        "Only Child Tierra Whack",
        "Dolly Tierra Whack",
        "Wasteland Tierra Whack",
        "Juice Lizzo",
        "Good as Hell Lizzo",
        "Truth Hurts Lizzo",
        "About Damn Time Lizzo",
        "Afeni Rapsody",
        "Sassy Rapsody",
        "Power Rapsody",
        "Body Megan Thee Stallion",
        "Savage Megan Thee Stallion",
        "Her Megan Thee Stallion",
        "Tap In Saweetie",
        "Best Friend Saweetie",
        "Say So Doja Cat",
        "Woman Doja Cat",
        "Boss B*tch Doja Cat",
        "High Rises Chika",
        "Industry Games Chika",
        "Conceited Flo Milli",
        "No Face Flo Milli",
        "Work It Missy Elliott",
        "Lose Control Missy Elliott",
        "The Rain Missy Elliott"
    ];

    let mut track_uris = Vec::new();

for song in &song_titles {
    let search_result = spotify
        .search(song, rspotify::model::SearchType::Track, None, None, Some(1), None)
        .await?;

    // 🔹 Debug: Print the entire SearchResult to understand its structure
    println!("Full SearchResult: {:#?}", search_result);
}


    // Step 4: Add Songs to Playlist
    if !track_uris.is_empty() {
        spotify
            .playlist_add_items(PlaylistId::from(playlist.id), track_uris, None) // ✅ Fixed borrowing issue
            .await?;
        println!("Added all songs successfully!");
    } else {
        println!("No songs were added.");
    }

    Ok(())
}

