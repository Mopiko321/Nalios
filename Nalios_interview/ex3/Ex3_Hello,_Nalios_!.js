// Ex3 :Hello, Nalios !
// # The task is to say hello to Nalios without using any string literals.

// The natural step to say hello would be to use a string. 
// If i cannot use it i can just use the characters that compose it.
// A quick google search shows that the ASCII values of the characters in "Hello, Nalios !" are:
// H: 72, e: 101, l: 108, o: 111,
// ",": 44, "space": 32, N: 78, a: 97, l: 108, i: 105, o: 111, s: 115, "!": 33
// So i can use these values to create the string 
// without using any string literals by constructing one from scratch.
// This is tested with the testing.html file in the same directory.

function sayHellotoNalios() {
    console.log(
        String.fromCharCode(72, 101, 108, 108, 111, 44, 
        32, 78, 97, 108, 105, 111, 115, 32, 33)
    );
}

sayHellotoNalios();