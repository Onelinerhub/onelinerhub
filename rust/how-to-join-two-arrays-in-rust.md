# How to join two arrays in Rust
// plain

Joining two arrays in Rust can be done using the `concat()` method. This method takes two arrays as arguments and returns a new array containing all the elements of both the arrays.

## Code example:
```
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let array3 = array1.concat(array2);
println!("{:?}", array3);
```
### Output `[1, 2, 3, 4, 5, 6]`

Explanation:
1. The `let` keyword is used to declare a variable. Here, two variables `array1` and `array2` are declared and assigned with two arrays containing elements `1, 2, 3` and `4, 5, 6` respectively.
2. The `concat()` method is used to join two arrays. It takes two arrays as arguments and returns a new array containing all the elements of both the arrays.
3. The `println!` macro is used to print the elements of the array `array3` which contains the elements of both the arrays `array1` and `array2`.
4. The `{:?}` is used to print the elements of the array in a debug format.

## Helpful links:
1. https://doc.rust-lang.org/std/primitive.slice.html#method.concat
2. https://doc.rust-lang.org/std/macro.println.html