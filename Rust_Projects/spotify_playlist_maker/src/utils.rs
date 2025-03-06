#[allow(dead_code)] // This prevents warnings about unused functions
pub fn format_track_name(title: &str, artist: &str) -> String {
    format!("{} - {}", title, artist)
}

#[allow(dead_code)]
pub fn generate_spotify_auth_url() -> String {
    "https://accounts.spotify.com/authorize".to_string()
}
