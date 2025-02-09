# Advent of Code 2024 solutions

in python and rust

## How to use?

Clone the repo. Go to [advent of code](https://adventofcode.com), sign in, go to a problem, and open its problem file. Then right click -> inspect -> Netowrk tab -> go to any request (reload if none) -> cookies -> copy session id

In a .env file, save your id as:
```.env
AOC_TOKEN="session:<your session id>"
````
To download the file for any day and year, use either the shell script or the python file:

##### Shell script get_file.sh
```bash
chmod +x get_file.sh
./get_file.sh <day> <year>
```

#### Python file get_files.py
```bash
uv init
uv run get_files.py <day> <year>
```


To run the rust files:
```bash
cargo run --bin <filename without .rs>
```
