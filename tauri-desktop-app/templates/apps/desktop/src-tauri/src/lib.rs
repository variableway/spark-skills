use tauri::Manager;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![greet, get_platform])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

#[command]
fn greet(name: &str) -> String {
    format!("Hello, {}! Welcome.", name)
}

#[command]
fn get_platform() -> String {
    let os = std::env::consts::OS.to_string();
    let arch = std::env::consts::ARCH.to_string();
    format!("{}-{}", os, arch)
}
