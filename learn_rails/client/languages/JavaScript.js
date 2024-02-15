// String Methods

// ***


// charAt(index_number) ==> returns character at specified index in a string


let text1 = "Hello World!"
console.log("character at index 2 ==> ", text1.charAt(2))



console.log("\n***\n")
// concat(target_string_to_add) ==> joins two or more strings, returns new string, non destructive



let string1 = "Hello"
let string2 = " World!"

console.log("hello + world joined ==> ", string1.concat(string2))



console.log("\n***\n")
// includes(string) ==> case sensitive, returns true or false if string contains substring



let text2 = "Hello World"
console.log("Hello World contains 'World'? ==> ", text2.includes("World"))
console.log("Hello World contains 'world'? ==> ", text2.includes("world"))



console.log("\n***\n")
// indexOf(specified_value_in_string) ==> case sensitive, returns the index of the first occurrence of value in string, and returns -1 if not found

let text3 = "Hello World!"
console.log("index of 'World' in 'Hello World'? ==> ", text3.indexOf("World"))
console.log("index of 'world' in 'Hello World'? ==> ", text3.indexOf("world"))
console.log("index of 'o' in 'Hello World'? ==> ", text3.indexOf("o"))




console.log("\n***\n")
// lastIndexOf(specified_value_in_string) ==> similar to indexOf except this returns last occurrence instead of first occurrence, and searches from the end of the string to the beginning, useful for finding last occurrence of char or substring, also returns -1 if it doesn't exist

let text4 = "Hello, World, Hello Moon, Hello Sun!"
console.log(text4)
console.log("last instance of 'World'? ==> ", text4.lastIndexOf("World"))
console.log("last instance of 'world'? ==> ", text4.lastIndexOf("world"))
console.log("last instance of 'H'? ==> ", text4.lastIndexOf("H"))





console.log("\n***\n")
// match(regExp) ==> searches a string for match against regular expression, returns array with matches, and returns null if there are none

let text5 = "The rain in SPAIN stays mainly in the plain"
console.log(text5)
console.log("all instances of ain", text5.match(/ain/gi))