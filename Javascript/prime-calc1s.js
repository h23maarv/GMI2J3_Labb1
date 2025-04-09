
/*
student version with NO assertion tests or refactoring implemented
*/

const min = 0;          // Set lower bounds
const max = 1000;       // Set upper bounds
let check4prime = {};   // global object
this.primeBucket        // array to hold prime numbers

class Check4Prime {

    /*
    Calculates prime numbers and put true or false in an array
    */

    primeCheck(num) {

        // Initialize array to hold prime numbers
        let primeBucket = new Array(max + 1);

        // Initialize all elements to true, non-primes will be set to false later
        for (let i = 2; i <= max; i++) {
            primeBucket[i] = true;
        }

        // Do all multiples of 2 first
        let j = 2;
        for (let i = j+j; i <= max; i = i+j) { // start with 2j as 2 is prime
            primeBucket[i] = false; // set all multiples of 2 to false
        }

        for (j = 3; j <= max; j = j+2) { // begin from 3 up to max
            if (primeBucket[j] == true) { // only do if primeBucket[j] is still a prime (not a multiple of 3, 5, 7, ...)
                for (let i = j+j; i <= max; i = i+j) { // start with 2j as j is a prime
                    primeBucket[i] = false; // set all multiples of the prime to false
                }
            }
        }

        // Check input against prime array
        if (primeBucket[num] == true) {
            return true;
        }
        else {
            return false;
        }
    }


    /*
    Method to validate input
    */

    checkArgs() {

        // Check arguments for correct number of parameters if not throw new Error();
        for (let i=0; i < arguments.length; i++)
            console.log(arguments[i]);

        // Check arguments for correct number of parameters if not throw new Error();
        if (arguments.length !== 1) {
            throw new Error("Function requires exactly one argument");
        }
        else
        {
            // If undefined throw new Error();
            if (typeof arguments[0] === 'undefined') {
                throw new Error("Input must be between 0 and 1000");
            }

            // If zero/empty throw new Error();
            if (arguments[0] == 0) {
                throw new Error("Input must be between 0 and 1000");
            }

            // If more than one input throw new Error();
            if (typeof arguments[0] !== 'number' || isNaN(arguments[0])) {
                throw new Error("Input must be a number");
            }

            // If less than lower bounds throw new Error();
            if (!Number.isInteger(arguments[0])) {
                throw new Error("Input must be an integer");
            }

            // Get integer from character
            let input = parseInt(arguments[0], 10);

            // If not a number throw new Error();
            if (isNaN(input)) {
                throw new Error("Input must be a number");
            }

            // If less than lower bounds throw new Error();
            if (input < min)
                throw new Error("Input must be between 0 and 1000");

            // If greater than upper bounds throw new Error();
            if (input > max)
                throw new Error("Input must be between 0 and 1000");
        }
    }
} // end Check4Prime class

check4prime.primeCheck = function (n) {
    return primeBucket[n] === true;
};

check4prime.check = function (n) {
    check4prime.checkArgs(n);
    return check4prime.primeCheck(n);
};

/*
do the automated tests cases when developer performs test
*/

function checkTest(num)
{
    // this function is only called with true or false when
    // the developer performs the tests which becomes pass or fail
    //assert(num, "description");

    check4prime = new Check4Prime();
    // run various automated tests
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
do the check for prime when ordinary user is running solution, you can merge this function with checkTest() if you want
*/

function check(num)
{
    checkTest(num) // when code is in production mode running the tests cases is commented away
    check4prime = new Check4Prime();

    try {
        //check4prime.checkArgs(num);
        check4prime.checkArgs(parseInt(num));
        // either use this assertion or the alert box for output
        //assert(check4prime.primeCheck(num), description)
        alert(`Is number ${num} a prime? ${check4prime.primeCheck(num)}`)
    }
    catch (err) {
        let description = `Input/number: ${num}. Error in checkArgs(): ${err.message}`;
        assert(true, description);
    }
}

/*
append test result in list on web page
*/

function assert(outcome, description) {
    let output = document.querySelector('#output');
    if (!output) {
        console.error("Output element not found");
        return;
    }
    let li = document.createElement('li');
    li.className = outcome ? 'pass' : 'fail';
    li.appendChild(document.createTextNode(description));
    output.appendChild(li);
}

/*
Test methods, recommended naming convention
(Test)_MethodToTest_ScenarioWeTest_ExpectedBehaviour
In test method the pattern we use is "tripple A"
Arrange, Act and Assert
*/

// Test case 1, check known true primes (should return true)
function test_Check4Prime_known_true() {
    // The arrangement below is called tripple A
	// Arrange - here we initialize our objects
    let knownTrue = new Array(2, 3, 5, 7, 11, 13, 17, 97, 199, 997);

    // Act - here we act on the objects
    for(let num of knownTrue) {
        // Assert - here we verify the result
        assert(check4prime.primeCheck(num), `Test for known true primes with: ${num}`)
    }
}

// Test case 2, check known false primes (should return false)
function test_Check4Prime_known_false() {
    // The arrangement below is called tripple A
    // Arrange - here we initialize our objects
    let knownFalse = new Array(0, 1, 4, 6, 8, 9, 10, 15, 100, 1000);

    // Act - here we act on the objects
    for(let num of knownFalse) {
        // Assert - here we verify the result
        assert(!check4prime.primeCheck(num), `Test for known false primes with: ${num}`)
    }
}

// Test case 3, check negative input
function test_Check4Prime_checkArgs_neg_input() {
    let description = `Test for negative input: -1`;
    try {
        check4prime.checkArgs(-1);
        assert(check4prime.primeCheck(-1), description);
    }
    catch (err) {
        // Expected: error thrown and primeCheck should return false
        assert(!check4prime.primeCheck(-1), description);
    }
}

// Test case 4, check for upper bound limit (e.g. 1001)
function test_Check4Prime_checkArgs_above_upper_bound() {
    let description = `Test for upper bound limit: 1001`;
    try {
        // the check4prime.checkArgs() method should throw an error if the input is above the upper bound limit
        // otherwise, the primeCheck method should return false
        check4prime.checkArgs(1001);
        assert(check4prime.primeCheck(1001), description);
    }
    catch (err) {
        // if an error is thrown, then the input is above the upper bound limit and this line is executed
        // since the method is expected to throw an error, the primeCheck method should return false
        // if our test case was successful to detect if the input was above the upper bound, true is sent to the assert method
        // in other words, our test case was successful if the error was thrown and the primeCheck method returned false
        // return either
        assert(!check4prime.primeCheck(1001), description);
    }
}

// Test case 5, check for char input (e.g. 'a')
function test_Check4Prime_checkArgs_char_input() {
    let description = `Test for char input: a`;
    try {
        check4prime.checkArgs('a');
        assert(check4prime.primeCheck('a'), description);
    }
    catch (err) {
        assert(!check4prime.primeCheck('a'), description);
    }
}

// Test case 6, check for more than one input
function test_Check4Prime_checkArgs_2_inputs() {
    let description = `Test for more than one input: 1, 2`;
    try {
        check4prime.checkArgs(1, 2);
        assert(check4prime.primeCheck(1, 2), description);
    }
    catch (err) {
        assert(!check4prime.primeCheck(1, 2), description);
    }
}

// Test case 7, check for zero/empty input (invalid case)
function test_Check4Prime_checkArgs_zero_input() {
    let description = `Test for zero/empty input: 0`;
    try {
        check4prime.checkArgs(0);
        assert(check4prime.primeCheck(0), description);
    }
    catch (err) {
        assert(!check4prime.primeCheck(0), description);
    }
}

// Test case 8, check for undefined input
function test_Check4Prime_checkArgs_undefined_input() {
    let description = `Test for undefined input: undefined`;
    try {
        check4prime.checkArgs(undefined);
        assert(check4prime.primeCheck(undefined), description);
    }
    catch (err) {
        assert(!check4prime.primeCheck(undefined), description);
    }
}

// Test case 9, check for non-integer input (e.g. 1.5)
function test_Check4Prime_checkArgs_non_integer_input() {
    let description = `Test for non-integer input: 1.5`;
    try {
        check4prime.checkArgs(1.5);
        assert(check4prime.primeCheck(1.5), description);
    }
    catch (err) {
        assert(!check4prime.primeCheck(1.5), description);
    }
}