use dotenv::dotenv;
use rspotify::{
    clients::{BaseClient, OAuthClient}, // ✅ Added BaseClient for `.search()`
    model::{PlayableId, SearchResult, SearchType},
    AuthCodeSpotify,
    Credentials,
    OAuth,
};
use std::{collections::HashSet, env, error::Error};
use tiny_http::Server;
use spotify_playlist_maker::{format_track_name, generate_spotify_auth_url};

fn main() {
    let track = format_track_name("Song Title", "Artist Name");
    println!("Formatted Track: {}", track);

    let auth_url = generate_spotify_auth_url();
    println!("Spotify Auth URL: {}", auth_url);
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    dotenv().ok(); // ✅ Load credentials from .env

    let creds = Credentials::new(
        &env::var("SPOTIFY_CLIENT_ID")?,
        &env::var("SPOTIFY_CLIENT_SECRET")?,
    );

    let oauth = OAuth {
        redirect_uri: env::var("SPOTIFY_REDIRECT_URI")?.to_string(),
        scopes: HashSet::from([
            "playlist-modify-public".to_string(),
            "playlist-modify-private".to_string(),
            "user-library-read".to_string(),
        ]), // ✅ Fixed scopes
        ..Default::default()
    };

    let spotify = AuthCodeSpotify::new(creds, oauth);

    // ✅ **Step 1: Display Authorization URL**
    let auth_url = spotify.get_authorize_url(false)?;
    println!("Authorize here: {}", auth_url);

    // ✅ **Step 2: Start Local Server to Capture Auth Code**
    println!("Waiting for Spotify authentication...");
    let server = Server::http("127.0.0.1:8888").unwrap();
    let request = server.recv().unwrap();
    let url = request.url().to_string();
    let code = url
        .split("code=")
        .nth(1)
        .unwrap_or("")
        .split('&')
        .next()
        .unwrap();

    println!("Received authorization code: {}", code);
    request
        .respond(tiny_http::Response::from_string(
            "You can close this tab now.",
        ))
        .unwrap();

    // ✅ **Step 3: Request Token Using Captured Code**
    spotify.request_token(code).await?;
    println!("Authenticated successfully!");

    // ✅ **Step 4: Create Playlist**
    let user = spotify.me().await?;
    println!("Spotify User ID: {}", user.id); // ✅ Debugging

    let playlist = spotify
        .user_playlist_create(user.id, "Rick Roll Playlist", Some(false), None, None)
        .await?;

    // ✅ **Step 5: Add Songs to Playlist**
    let song_titles = [
        "Never Gonna Give You Up Rick Astley",
        "MMM Bop Hansen",
        "Feeling Good Nina Simone",
    ];

    let mut track_uris: Vec<PlayableId> = Vec::new(); // ✅ FIX: Store as `PlayableId`

    for song in &song_titles {
        let search_result = spotify
            .search(song, SearchType::Track, None, None, Some(1), None)
            .await?;

        // 🔹 Debugging: Print the full search result to see the correct structure
        println!("Full SearchResult: {:#?}", search_result);

        if let SearchResult::Tracks(tracks) = search_result {
            if let Some(track) = tracks.items.first() {
                println!("Adding {} to playlist...", track.name);
                let track_id = track.id.as_ref().unwrap();
                track_uris.push(track_id.clone().into());
            }
        } else {
            println!("Could not find {}", song);
        }
    }

    // ✅ **Step 6: Add Songs to Playlist**
    if !track_uris.is_empty() {
        spotify
            .playlist_add_items(playlist.id, track_uris, None)
            .await?;
        println!("Added all songs successfully!");
    } else {
        println!("No songs were added.");
    }

    Ok(())
} // ✅ **Closing `main()` Properly**

mod utils; // Keep this so Rust knows about utils.rs

#[cfg(test)]
mod tests {
    use crate::utils::{format_track_name, generate_spotify_auth_url}; // ✅ Only used in tests

    #[test]
    fn test_format_track_name() {
        let formatted = format_track_name("Upside Down", "Jack Johnson");
        assert_eq!(formatted, "Upside Down - Jack Johnson");
    }

    #[test]
    fn test_spotify_auth_url() {
        let test_url = generate_spotify_auth_url();
        assert!(test_url.contains("https://accounts.spotify.com/authorize"));
    }
}
