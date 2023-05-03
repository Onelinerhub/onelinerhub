# How to borrow closure in Rust
// plain

Closure is a feature of Rust that allows a function to capture and use variables from its environment. It is a powerful tool for writing concise and expressive code.

## Example code

```
fn main() {
    let x = 5;
    let closure = || x * x;
    println!("{}", closure());
}
```
## Output example

```
25
```

## Code explanation

1. `let x = 5;` - declares a variable `x` with value `5`
2. `let closure = || x * x;` - declares a closure `closure` which captures the variable `x` from its environment and multiplies it by itself
3. `println!("{}", closure());` - prints the result of calling the closure `closure`

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Closure Examples](https://doc.rust-lang.org/book/ch13-02-closures-as-input-parameters.html#examples-of-closures)

group: rust-borrow