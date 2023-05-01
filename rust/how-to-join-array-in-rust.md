# How to join array in Rust
// plain

Joining an array in Rust can be done using the `join` method. This method takes a string as an argument, which will be used as a separator between the elements of the array.

## Code example:
```
let array = ["a", "b", "c"];
let joined_array = array.join(", ");
println!("{}", joined_array);
```

### Output
`a, b, c`

## Explanation of code parts:
1. `let array = ["a", "b", "c"];` - This line creates an array of strings with the elements "a", "b", and "c".
2. `let joined_array = array.join(", ");` - This line calls the `join` method on the array, passing in a string with a comma and a space as an argument. This will be used as a separator between the elements of the array.
3. `println!("{}", joined_array);` - This line prints the joined array to the console.

## Helpful links:
1. https://doc.rust-lang.org/std/primitive.slice.html#method.join
2. https://doc.rust-lang.org/book/ch08-03-strings.html