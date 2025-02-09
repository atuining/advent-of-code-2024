#!/bin/zsh

day=$1
year=$2

source .env

curl --cookie "${AOC_TOKEN}" https://adventofcode.com/${year}/day/${day}/input >> day${day}.txt
