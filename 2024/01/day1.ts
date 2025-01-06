/**********************************************************
* Advent of Code 2024 Day 1
* https://adventofcode.com/2024/day/1
*
*
* My very first typescript program
* 
**********************************************************/

import * as fs from 'fs';
import * as readline from 'readline';

async function parseFile(filePath: string): Promise<[number[], number[]]> {
    const array1: number[] = [];
    const array2: number[] = [];

    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        // Split the line by whitespace
        const numbers = line.trim().split(/\s+/).map(Number);

        if (numbers.length !== 2) {
            console.error(`Invalid input on line: "${line}"`);
            continue; // Skip invalid lines
        }

        array1.push(numbers[0]); // First number goes into Array1
        array2.push(numbers[1]); // Second number goes into Array2
    }

    return [array1, array2];
}

function elementWiseSubtractAbs(array1: number[], array2: number[]): number[] {
    if (array1.length !== array2.length) {
        throw new Error('Arrays must have the same length');
    }

    return array1.map((value, index) => Math.abs(value - array2[index]));
}

function sumArray(array: number[]): number {
    return array.reduce((sum, current) => sum + current, 0);
}

function countOccurrences(array: number[], target: number): number {
    return array.reduce((count, current) => current === target ? count + 1 : count, 0);
}

function addSimilarity(array1:number[], array2:number[]): number {
    return array1.reduce((accumulator, currentValue) => accumulator + currentValue * countOccurrences(array2, currentValue) , 0)
}

async function main() {

    
    // Read input file and parse lists
    const filePath = 'input1.txt'; 

    let array1: number[] = [];
    let array2: number[] = [];

    try {
        [array1, array2] = await parseFile(filePath);
        console.log('Array1:', array1);
        console.log('Array2:', array2);
    } catch (error) {
        console.error('Error reading file:', error);
    }

    // Sort lists
    const sortedArray1 :number[] = array1.sort((a, b) => a - b);
    const sortedArray2 :number[] = array2.sort((a, b) => a - b);

    // Compute Distances
    let distances: number[] = elementWiseSubtractAbs(sortedArray2, sortedArray1);
    console.log('Sum of Distances:', sumArray(distances));

    // Comput Similarity Scores
    console.log('Similarity Score:', addSimilarity(array1, array2))

}

main();

