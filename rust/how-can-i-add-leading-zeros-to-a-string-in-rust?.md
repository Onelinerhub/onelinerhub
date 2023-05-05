# How can I add leading zeros to a string in Rust?
// plain

Adding leading zeros to a string in Rust can be done using the `format!` macro. The `format!` macro takes a format string and a list of arguments and returns a `String` object. The format string can contain placeholders for the arguments, and the placeholders can be used to add leading zeros.

## Example code

```
let num = 5;
let result = format!("{:02}", num);
println!("{}", result);
```

## Output example

```
05
```

## Code explanation

- `let num = 5;`: This line declares a variable `num` and assigns it the value `5`.
- `let result = format!("{:02}", num);`: This line uses the `format!` macro to create a `String` object with the value `05`. The `:02` placeholder tells the macro to add leading zeros to the number until it is two digits long.
- `println!("{}", result);`: This line prints the `String` object to the console.

## Helpful links
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)