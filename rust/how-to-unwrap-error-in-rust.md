# How to unwrap error in Rust
// plain

Error unwrapping in Rust is a process of extracting the underlying error from a `Result` or `Option` type. This is done using the `unwrap()` method, which returns the value inside the `Result` or `Option` type if it is `Ok`, or panics if it is `Err`.

## Code example:

```
let result: Result<i32, &str> = Ok(5);
let value = result.unwrap();
println!("The value is: {}", value);
```

### Output

The value is: 5

## Explanation:

1. The `let result` line declares a variable `result` of type `Result<i32, &str>` and assigns it the value `Ok(5)`. This means that the `Result` type contains an `Ok` variant with the value `5`.
2. The `let value` line declares a variable `value` and assigns it the result of calling the `unwrap()` method on `result`. This will extract the value `5` from the `Ok` variant and assign it to `value`.
3. The `println!` line prints the value of `value` to the console.

## Helpful links:

1. [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
2. [Rust Documentation - Result](https://doc.rust-lang.org/std/result/)