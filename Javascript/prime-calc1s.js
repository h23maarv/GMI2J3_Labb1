const min = 0;          // Set lower bounds
const max = 1000;       // Set upper bounds
let check4prime = {};   // global object

class Check4Prime {
    // Creates a sieve array to store prime numbers using Sieve of Eratosthenes
    constructor() {
        this.primeBucket = new Array(max + 1).fill(true);
        this.generatePrimeSieve();
    }
    // Builds the prime number sieve using the Sieve of Eratosthenes algorithm
    generatePrimeSieve() {
        this.primeBucket[0] = false; // 0 is not a prime
        this.primeBucket[1] = false; // 1 is not a prime

        // Mark all non-prime numbers in the bucket
        for (let i = 2; i * i <= max; i++) {
            if (this.primeBucket[i]) {
                for (let j = i * i; j <= max; j += i) {
                    this.primeBucket[j] = false;
                }
            }
        }
    }

    // Returns true if the number is prime, otherwise false
    primeCheck(num) {
        return this.primeBucket[num] === true;
    }

    // Validates the input before checking for primality
    checkArgs() {
        if (arguments.length !== 1) {
            throw new Error('Too many arguments');
        }

        if (arguments[0] === undefined || arguments[0] === "") {
            throw new Error('Input is empty, undefined or null');
        }

        if (!Number.isInteger(Number(arguments[0]))) {
            throw new Error('Input is not an integer');
        }

        let input = parseInt(arguments[0], 10);

        if (isNaN(input)) {
            throw new Error('Input is not a number');
        }

        if (input < min || input > max) {
            throw new Error('Input is out of bounds');
        }
    }
}

/*
Run automated test cases when the developer triggers them
*/

function checkTest() {
    check4prime = new Check4Prime(); // Re-initialize object and prime table
    test_Check4Prime_known_true();
    test_Check4Prime_known_false();
    test_Check4Prime_checkArgs_neg_input();
    test_Check4Prime_checkArgs_above_upper_bound();
    test_Check4Prime_checkArgs_char_input();
    test_Check4Prime_checkArgs_2_inputs();
    test_Check4Prime_checkArgs_zero_input();
    test_Check4Prime_checkArgs_undefined_input();
    test_Check4Prime_checkArgs_non_integer_input();
}

/*
Triggered from UI: Reads input, validates, and alerts result
*/

function checkFromInput() {
    let input = document.querySelector('input[name="number"]').value;
    try {
        check4prime.checkArgs(input);
        let isPrime = check4prime.primeCheck(parseInt(input));
        alert(`Is number ${input} a prime? ${isPrime}`);
    } catch (err) {
        alert(`Error: ${err.message} for input: ${input}`);
    }
}

/*
Run prime check with assertions (used for testing)
*/

function check(num) {
    try {
        check4prime.checkArgs(parseInt(num));
        alert(`Is number ${num} a prime? ${check4prime.primeCheck(num)}`);
    } catch (err) {
        let description = `Input/number: ${num}. Error in checkArgs()`;
        assert(check4prime.primeCheck(num), description);
    }
}

/*
Assert function for test output
*/

function assert(outcome, description) {
    let output = document.querySelector('#output');
    let li = document.createElement('li');
    li.className = outcome ? 'pass' : 'fail';
    li.appendChild(document.createTextNode(description));
    output.appendChild(li);
}

/* === Test Cases === */

// Known primes – should all return true
function test_Check4Prime_known_true() {
    let knownTrue = [3, 17, 29, 997];
    for (let num of knownTrue) {
        assert(check4prime.primeCheck(num), `Known prime: ${num}`);
    }
}

// Known non-primes – should all return false
function test_Check4Prime_known_false() {
    let knownFalse = [0, 1, 6, 8, 10];
    for (let num of knownFalse) {
        assert(!check4prime.primeCheck(num), `Known non-prime: ${num}`);
    }
}

// Negative input should throw an error
function test_Check4Prime_checkArgs_neg_input() {
    try {
        check4prime.checkArgs(-1);
        assert(false, `Expected exception for negative input`);
    } catch (e) {
        assert(true, `Test for negative input`);
    }
}

// Input above 1000 should throw an error
function test_Check4Prime_checkArgs_above_upper_bound() {
    try {
        check4prime.checkArgs(1001);
        assert(false, `Expected exception for input > 1000`);
    } catch (err) {
        assert(true, `Test for upper bound input`);
    }
}

// Character input should throw an error
function test_Check4Prime_checkArgs_char_input() {
    try {
        check4prime.checkArgs("r");
        assert(false, `Expected exception for char input`);
    } catch (err) {
        assert(true, `Test for char input`);
    }
}

// Two inputs should throw an error
function test_Check4Prime_checkArgs_2_inputs() {
    try {
        check4prime.checkArgs(1, 2);
        assert(false, `Expected exception for two inputs`);
    } catch (err) {
        assert(true, `Test for more than one input`);
    }
}

// Empty input should throw an error
function test_Check4Prime_checkArgs_zero_input() {
    let zeroInput = "";
    try {
        check4prime.checkArgs(zeroInput);
        assert(false, `Expected exception for empty input`);
    } catch (err) {
        assert(true, `Test for empty input`);
    }
}

// Undefined input should throw an error
function test_Check4Prime_checkArgs_undefined_input() {
    try {
        check4prime.checkArgs(undefined);
        assert(false, `Expected exception for undefined input`);
    } catch (err) {
        assert(true, `Test for undefined input`);
    }
}

// Decimal input should throw an error (not integer)
function test_Check4Prime_checkArgs_non_integer_input() {
    try {
        check4prime.checkArgs("4.20");
        assert(false, `Expected exception for non-integer input`);
    } catch (err) {
        assert(true, `Test for non-integer input`);
    }
}