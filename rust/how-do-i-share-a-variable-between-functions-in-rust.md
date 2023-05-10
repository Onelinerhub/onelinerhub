# How do I share a variable between functions in Rust?
// plain

Variables can be shared between functions in Rust by passing them as arguments. For example, the following code passes a variable `x` to a function `foo`:
```rust
let x = 5;

fn foo(x: i32) {
    println!("x is {}", x);
}

foo(x);
```
## Output example

```
x is 5
```

The code works by passing the value of `x` to the function `foo` as an argument. The function `foo` then prints the value of `x`.

Alternatively, variables can be shared between functions by using a reference. For example, the following code passes a reference to a variable `x` to a function `foo`:
```rust
let x = 5;

fn foo(x: &i32) {
    println!("x is {}", x);
}

foo(&x);
```
## Output example

```
x is 5
```

The code works by passing a reference to the variable `x` to the function `foo` as an argument. The function `foo` then prints the value of `x`.

## Helpful links
- [Rust Book - References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust Book - Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)

group: rust-variables