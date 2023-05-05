# rust string add string
// plain

Rust strings are a type of data structure used to store and manipulate text. They are stored as a sequence of Unicode scalar values, which are numbers that represent characters. Strings can be added together using the `+` operator.

## Example code

```
let s1 = "Hello";
let s2 = "World";
let s3 = s1 + " " + s2;
println!("{}", s3);
```

## Output example

```
Hello World
```

The code above creates two strings, `s1` and `s2`, and then adds them together using the `+` operator. The result is stored in `s3`, which is then printed out.

## Code explanation

- `let s1 = "Hello";`: This creates a string called `s1` and assigns it the value `"Hello"`.
- `let s2 = "World";`: This creates a string called `s2` and assigns it the value `"World"`.
- `let s3 = s1 + " " + s2;`: This adds `s1` and `s2` together, separated by a space, and stores the result in `s3`.
- `println!("{}", s3);`: This prints out the value of `s3`.

## Helpful links
- [Rust Strings](https://doc.rust-lang.org/std/string/struct.String.html)