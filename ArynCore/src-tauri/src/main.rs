use tauri::Manager;
fn main() {
    let app = tauri::Builder::default()
        .manage(app_handler) // This will store the AppHandle in the AppState.
        .build();

    let app = match app {
        Ok(app) => app,
        Err(error) => {
            eprintln!("Error during application startup: {}", error);
            return;
        }
    };

    app.run(move |event| match event {
        tauri::WindowEvent::CloseRequested { .. } => {
            // Handle window closing here, if needed.
            false // Return `true` to close the app.
        }
        _ => false,
    });
}

fn app_handler(app: &mut AppHandle) {
    // Set up your app logic here.
}
