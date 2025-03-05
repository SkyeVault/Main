#[cfg(test)]
mod tests {
    use dotenv::dotenv;
    use std::env;

    #[test]
    fn test_env_variables() {
        dotenv().ok();

        assert!(env::var("SPOTIFY_CLIENT_ID").is_ok());
        assert!(env::var("SPOTIFY_CLIENT_SECRET").is_ok());
        assert!(env::var("SPOTIFY_REDIRECT_URI").is_ok());
    }
}

