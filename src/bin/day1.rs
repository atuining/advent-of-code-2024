use std::{
    collections::{HashMap, HashSet},
    fs::File,
    io::read_to_string,
};

fn calculate(filename: &str) {
    let mut left: Vec<u32> = Vec::new();
    let mut right: Vec<u32> = Vec::new();

    let file = File::open(filename).unwrap();

    for line in read_to_string(file).unwrap().lines() {
        left.push(line.split_once("   ").unwrap().0.parse().unwrap());
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

    let mut left2 = HashSet::new();
    for num in &left {
        left2.insert(num);
    }
    let mut right2 = HashMap::new();
    for num in &right {
        right2.entry(num).and_modify(|val| *val += 1).or_insert(1);
    }

    for num in left2 {
        if right2.contains_key(&num) {
            distance2 += num * right2[&num];
        }
    }

    println!("{}", distance2);

    let mut similarity = 0;

    for element in left {
        similarity += element * (right.iter().filter(|&n| *n == element).count() as u32);
    }
    println!("{}", similarity);
}

fn main() {
    calculate("./2024-1.txt");
}
