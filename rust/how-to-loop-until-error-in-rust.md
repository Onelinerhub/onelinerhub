# How to loop until error in Rust
// plain

Looping until an error occurs in Rust can be done using a `loop` and `match` statement. The `loop` statement will execute the code within its block until a `break` statement is encountered. The `match` statement is used to check the result of the code within the loop and `break` if an error is encountered.

```rust
loop {
    let result = do_something();
    match result {
        Ok(val) => println!("{}", val),
        Err(err) => {
            println!("Error: {}", err);
            break;
        }
    }
}
```

## Output example

```
Value
Error: Something went wrong
```

## Code explanation

- `loop`: Executes the code within its block until a `break` statement is encountered.
- `match`: Checks the result of the code within the loop and `break` if an error is encountered.
- `Ok(val)`: If the result is successful, the value is printed.
- `Err(err)`: If the result is an error, the error is printed and the loop is broken.

## Helpful links
- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust Documentation - Match](https://doc.rust-lang.org/book/ch06-02-match.html)

group: rust-loops