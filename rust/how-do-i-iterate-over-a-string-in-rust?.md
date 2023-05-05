# How do I iterate over a string in Rust?
// plain

Iterating over a string in Rust is done using the `chars()` method. This method returns an iterator over the characters of a string.

## Example code

```
let my_string = "Hello World!";

for c in my_string.chars() {
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
!
```

## Code explanation

- `let my_string = "Hello World!";`: This line declares a string variable.
- `for c in my_string.chars()`: This line starts a for loop that iterates over the characters of the string.
- `println!("{}", c);`: This line prints each character of the string.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)