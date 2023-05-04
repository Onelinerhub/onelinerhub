# How to iterate over string in Rust
// plain

Iterating over strings in Rust is done using the `chars()` method. This method returns an iterator over the characters of a string.

Example:
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

- `let my_string = "Hello World!";`: This declares a string variable called `my_string` and assigns it the value `"Hello World!"`.
- `for c in my_string.chars()`: This starts a loop that iterates over each character in the string `my_string`. The current character is stored in the variable `c`.
- `println!("{}", c);`: This prints the current character stored in the variable `c`.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)

group: rust-loops