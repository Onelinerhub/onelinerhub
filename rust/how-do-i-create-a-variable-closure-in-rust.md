# How do I create a variable closure in Rust?
// plain

A variable closure in Rust is a closure that captures a variable from its environment. It is created using the `move` keyword, which captures the variable from its environment and moves it into the closure.

## Example code

```
let x = 5;
let closure = move || x * x;
```

## Output example

```
closure: [closure@src/main.rs:2:26: 2:35]
```

## Code explanation

- `let x = 5;`: This declares a variable `x` with the value `5`.
- `let closure = move || x * x;`: This creates a closure `closure` that captures the variable `x` from its environment and moves it into the closure. The closure will return the square of `x` when called.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Closures: Capturing Environment](https://doc.rust-lang.org/book/ch13-02-closures-capturing-environment-variables.html)

group: rust-variables