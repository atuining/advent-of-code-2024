use std::{fs::File, io::read_to_string};

fn part1(line: &str) -> bool {
    let x: Vec<i32> = line.split(" ").map(|num| num.parse().unwrap()).collect();
    if x.len() < 2 {
        return true;
    }
    let sign = x[1] > x[0];
    for (i, num) in x[1..].iter().enumerate() {
        let diff = num - x[i];
        if ((diff > 0) != sign) || diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }
    }
    true
}

fn part2(line: &str) -> bool {
    true
}

fn main() {
    let filename = "./2024-2.txt";
    let file = File::open(filename).unwrap();
    let mut count = 0;

    for line in read_to_string(file).unwrap().lines() {
        if part1(line) {
            count += 1;
        }
    }
    println!("{count}");

    let mut count2 = 0;
    for line in read_to_string(file).unwrap().lines() {
        if part2(line) {
            count2 += 1;
        }
    }
    println!("{count2}");
}
