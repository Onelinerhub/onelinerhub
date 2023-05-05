# How do I get a substring from a string in Rust?
// plain

You can get a substring from a string in Rust using the `.get()` method. This method takes two parameters, the starting index and the length of the substring.

## Example code

```
let s = String::from("Hello World!");
let substring = s.get(0..5).unwrap();
```

## Output example

```
Hello
```

## Code explanation

- `let s = String::from("Hello World!");`: This line creates a new `String` object with the value `Hello World!`.
- `let substring = s.get(0..5).unwrap();`: This line calls the `.get()` method on the `String` object `s` with the parameters `0` and `5`. This will return a `Some` object containing the substring `Hello`. The `.unwrap()` method is used to extract the value from the `Some` object.

## Helpful links
- [String::get() method](https://doc.rust-lang.org/std/primitive.str.html#method.get)