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
        .user_playlist_create(user.id, "Playtime Playlist", Some(false), None, None)
        .await?;

    // ✅ **Step 5: Add Songs to Playlist**
    let song_titles = [
        "Upside Down Jack Johnson",
        "Banana Pancakes Jack Johnson",
        "We Are Going to Be Friends Jack Johnson",
        "Count on Me Unknown",
        "Brave Unknown",
        "Fireflies Owl City",
        "Hurry Up We're Dreaming M83",
        "Three Little Birds Bob Marley",
        "All I Want Is You Barry Louis Polisar",
        "Lollipop Unknown",
        "All I Have to Do Is Dream The Everly Brothers",
        "Teddy Bear Elvis Presley",
        "Can't Help Falling in Love Elvis Presley",
        "Hound Dog Elvis Presley",
        "Coconut Harry Nilsson",
        "Raindrops Keep Falling on My Head B.J. Thomas",
        "My Favorite Things Julie Andrews",
        "O-o-h Child The Five Stairsteps",
        "The Promise When in Rome",
        "Thunder Imagine Dragons",
        "I Gotta Feeling The Black Eyed Peas",
        "I'm on Top of the World Imagine Dragons",
        "Take On Me a-ha",
        "You Make My Dreams Come True Hall & Oates",
        "Mother and Child Reunion Paul Simon",
        "Unchained Melody The Righteous Brothers",
        "Positive Vibrations Bob Marley",
        "Banana Boat Song (Day-O) Harry Belafonte",
        "Everyday Buddy Holly",
        "Rockin' Robin Bobby Day",
        "Splish Splash Bobby Darin",
        "Safe and Sound Capital Cities",
        "Everyday People Sly & The Family Stone",
        "Boogie Shoes KC & The Sunshine Band",
        "Sugar Sugar The Archies",
        "The Lion Sleeps Tonight The Tokens",
        "You're My Best Friend Queen",
        "Obvious Child Paul Simon",
        "Father and Daughter Paul Simon",
        "Me and Julio Down by the Schoolyard Paul Simon",
        "The Boy in the Bubble Paul Simon",
        "Born at the Right Time Paul Simon",
        "Lookin' Out My Back Door Creedence Clearwater Revival",
        "Stay I Missed You Lisa Loeb",
        "Dedicated to the One I Love The Shirelles",
        "Earth Angel The Penguins",
        "Walk Like an Egyptian The Bangles",
        "Oh Mickey Toni Basil",
        "Girls Just Want to Have Fun Cyndi Lauper",
        "Down Under Men at Work",
        "Stay Up Late Talking Heads",
        "This Must Be the Place Naive Melody Talking Heads original & cover",
        "Wild Life Talking Heads",
        "You Can Call Me Al Paul Simon",
        "Walking on Sunshine Katrina & The Waves",
        "Wake Me Up Before You Go Go Wham!",
        "All Star Smash Mouth",
        "The Tide Is High Blondie",
        "Silly Love Songs Paul McCartney & Wings",
        "Yellow Coldplay",
        "How Bizarre OMC",
        "Five Years Time Noah and the Whale",
        "Wouldn't It Be Nice The Beach Boys",
        "MMMBop Hanson",
        "Home Phillip Phillips",
        "River of Dreams Billy Joel",
        "A Little Bit of Love Unknown",
        "Best Day of My Life American Authors",
        "The Middle Jimmy Eat World",
        "Roar Katy Perry",
        "Keep Your Head Up Andy Grammer",
        "Let the Good Times Roll Shirley and Lee",
        "What I Like About You The Romantics",
        "Stand R.E.M.",
        "Birdhouse in Your Soul They Might Be Giants",
        "Love Is in the Heart Deee-Lite",
        "Gettin' Jiggy Wit It Will Smith",
        "U Can't Touch This MC Hammer",
        "Friday I'm in Love The Cure",
        "If I Had $1,000,000 Barenaked Ladies",
        "Got to Have You The Weepies",
        "Mona Lisa and Mad Hatters Elton John",
        "Forever Young Rod Stewart",
        "Against the Wind Bob Seger",
        "You Can Get It If You Really Want Jimmy Cliff",
        "Over the Rainbow Israel Kamakawiwo'ole",
        "In the Jungle The Lion Sleeps Tonight The Tokens",
        "We Are Going to Be Friends The White Stripes",
        "Yellow Submarine The Beatles",
        "Good Day Sunshine The Beatles",
        "Here Comes the Sun The Beatles",
        "Twist and Shout The Beatles",
        "All You Need Is Love The Beatles",
        "You and I Ingrid Michaelson",
        "Backyard Ingrid Michaelson",
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
