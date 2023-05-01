# How to join list of strings in Rust
// plain

Joining a list of strings in Rust can be done using the `join` method of the `String` type. The `join` method takes a `Vec<&str>` as an argument and returns a `String` with the elements of the `Vec` joined together.

## Code example:
```
let list_of_strings = vec!["Hello", "World"];
let joined_string = list_of_strings.join(" ");
```

### Output
```
Hello World
```

## Explanation of code parts:
1. `let list_of_strings = vec!["Hello", "World"];` - This line creates a `Vec` of `&str`s containing the strings "Hello" and "World".
2. `let joined_string = list_of_strings.join(" ");` - This line calls the `join` method on the `Vec` of `&str`s, passing in a single space as the separator. This returns a `String` with the elements of the `Vec` joined together with a single space.

## Helpful links:
1. https://doc.rust-lang.org/std/string/struct.String.html#method.join
2. https://doc.rust-lang.org/std/vec/struct.Vec.html#method.join