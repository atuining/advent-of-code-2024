use std::env;
use std::fs::File;
use std::io::Write;
use std::path::Path;
use reqwest::blocking::Client;
use dotenv::dotenv;

fn download_input(day: u32, year: u32) -> Result<(), Box<dyn std::error::Error>> {
    dotenv()
        .ok();
    let access_token = env::var("AOC_TOKEN").expect("The access token was not found in the .env file");
   
    let url = format!("https://adventofcode.com/{}/day/{}/input", year, day);
    let filename = format!("{}-{}.txt", year, day);

    let client = Client::new();
    let response = client
        .get(&url)
        .header("Cookie", access_token)
        .send()?
        .error_for_status()?;

    let body = response.text()?;
    if !Path::new(&filename).try_exists()? {
        let mut file =  File::create(&filename)?;
        file.write_all(body.as_bytes())?;
    }

    println!("Downloaded input for {}/{} to {}", year, day, filename);
    Ok(())
    
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if let Err(e) = download_input(args[1].parse::<u32>().unwrap(), args[2].parse::<u32>().unwrap()) {
        eprintln!("Error: {}", e);
    }
}
