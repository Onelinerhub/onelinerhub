# rust string array
// plain

A Rust string array is a collection of strings stored in a contiguous memory block. It is a data structure that allows for efficient access and manipulation of strings. The syntax for declaring a string array in Rust is ```let array_name: [String; size] = [String::new(); size];```, where ```size``` is the number of strings in the array.

The example code below creates an array of strings with three elements:

```
let array_name: [String; 3] = [String::new(), String::from("Hello"), String::from("World")];
```

The output of the example code is:

```
[String::new(), String::from("Hello"), String::from("World")]
```

## Code explanation


* ```let array_name: [String; 3]``` - This declares a string array named ```array_name``` with a size of 3.

* ```String::new()``` - This creates a new empty string.

* ```String::from("Hello")``` - This creates a string from the given string literal.

* ```String::from("World")``` - This creates a string from the given string literal.

## Helpful links

* [Rust String Array](https://doc.rust-lang.org/std/primitive.str.html#string-arrays)
* [Rust String](https://doc.rust-lang.org/std/string/struct.String.html)