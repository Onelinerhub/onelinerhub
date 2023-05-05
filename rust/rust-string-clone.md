# rust string clone
// plain

`String::clone` is a method in Rust that creates a new `String` from an existing one. It is used to create a deep copy of a `String` so that the original `String` can be modified without affecting the new one.

## Example

```
let s1 = String::from("Hello");
let s2 = s1.clone();

println!("s1 = {}, s2 = {}", s1, s2);
```
## Output example

```
s1 = Hello, s2 = Hello
```

The code above creates two `String`s, `s1` and `s2`, from the same string literal. `s2` is created using the `clone` method on `s1`. This creates a deep copy of `s1` so that modifying `s1` does not affect `s2`.

Parts of the code:
- `let s1 = String::from("Hello");`: This creates a `String` from the string literal "Hello".
- `let s2 = s1.clone();`: This creates a deep copy of `s1` and assigns it to `s2`.
- `println!("s1 = {}, s2 = {}", s1, s2);`: This prints out the values of `s1` and `s2`.

## Helpful links
- [Rust Documentation - String::clone](https://doc.rust-lang.org/std/string/struct.String.html#method.clone)