# How to loop string chars in Rust
// plain

Looping through a string in Rust is a simple process. The `chars()` method can be used to iterate over the characters of a string. The following example code will loop through each character of a string and print it out:

```rust
let s = "Hello World";

for c in s.chars() {
    println!("{}", c);
}
```

## Output example

```
H
e
l
l
o

W
o
r
l
d
```

The code works by using the `chars()` method to get an iterator over the characters of the string. The `for` loop then iterates over the characters and prints them out.

## Code explanation

- `let s = "Hello World";`: This line declares a string variable `s` and assigns it the value `"Hello World"`.
- `for c in s.chars()`: This line starts a `for` loop that iterates over the characters of the string `s`. The variable `c` is used to store each character as the loop iterates.
- `println!("{}", c);`: This line prints out the character stored in the variable `c`.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)

group: rust-loops