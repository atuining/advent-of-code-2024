use std::{fs::File, io::read_to_string};

fn calculate(filename: &str) {
    let mut left: Vec<u32> = Vec::new();
    let mut right: Vec<u32> = Vec::new();

    let file = File::open(filename).unwrap();

    for line in read_to_string(file).unwrap().lines() {
        left.push(line.split_once("   ")
            .unwrap()
            .0
            .parse()
            .unwrap());
        right.push(line.split_once("   ").unwrap().1.parse().unwrap());
    }

    left.sort();
    right.sort();

    let mut distance = 0;
    for (index, element) in left.iter().enumerate() {
        distance += element.abs_diff(right[index]);
    }
    println!("{}", distance);

    let mut distance2 = 0;

    

}


fn main() {
    calculate("./2024-1.txt");
}
