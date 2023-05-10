# How do I use a variable in a match statement in Rust?
// plain

Using a variable in a match statement in Rust is a powerful way to control the flow of your program. The match statement is a powerful tool for pattern matching and allows you to compare a variable to a set of patterns.

## Example code

```
let x = 5;

match x {
    1 => println!("x is 1"),
    2 => println!("x is 2"),
    3 => println!("x is 3"),
    4 => println!("x is 4"),
    5 => println!("x is 5"),
    _ => println!("x is something else"),
}
```

## Output example

```
x is 5
```

## Code explanation


1. `let x = 5;` - This declares a variable `x` and assigns it the value `5`.
2. `match x {` - This begins the match statement and uses the variable `x` as the value to be matched.
3. `1 => println!("x is 1"),` - This is a pattern that matches the value `1` and prints the string `x is 1` if the value of `x` is `1`.
4. `_ => println!("x is something else"),` - This is a catch-all pattern that matches any value that is not matched by the other patterns and prints the string `x is something else`.

## Helpful links

- [Rust Documentation - Match](https://doc.rust-lang.org/book/ch06-02-match.html)

group: rust-variables