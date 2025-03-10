use std::fs::File;

fn main() {
    let filename = "./2024-3.txt";
    let file = File::open(filename).unwrap();
}
