cat <<EOF > src-tauri/src/main.rs
#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use std::fs;
use std::process::Command;
use tauri::command;

#[command]
fn read_system_prompt() -> Result<String, String> {
    fs::read_to_string("../instructions/system.txt").map_err(|e| e.to_string())
}

#[command]
fn read_chatlog() -> Result<String, String> {
    fs::read_to_string("../memory/chatlog.json").map_err(|e| e.to_string())
}

#[command]
fn send_prompt(prompt: String) -> Result<String, String> {
    let full_prompt = format!(
        "{}\\n\\n{}",
        read_system_prompt().unwrap_or_default(),
        prompt
    );

    let curl_result = Command::new("curl")
        .arg("-s")
        .arg("http://localhost:11434/api/generate")
        .arg("-d")
        .arg(format!(
            "{{\"model\": \"mistral\", \"prompt\": \"{}\", \"stream\": false}}",
            full_prompt.replace("\"", "\\\"")
        ))
        .output();

    match curl_result {
        Ok(output) => {
            let output_str = String::from_utf8_lossy(&output.stdout);
            Ok(output_str.to_string())
        }
        Err(e) => Err(e.to_string()),
    }
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            read_system_prompt,
            read_chatlog,
            send_prompt
        ])
        .run(tauri::generate_context!())
        .expect("error while running ArynCore");
}
EOF
