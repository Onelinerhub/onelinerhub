# How to pass a Rust slice as a parameter?
// plain

Passing a Rust slice as a parameter is done by using the `&[T]` syntax. This syntax indicates that a slice of type `T` is being passed as a parameter.

## Example

```
fn print_slice(slice: &[i32]) {
    println!("{:?}", slice);
}

fn main() {
    let arr = [1, 2, 3];
    print_slice(&arr);
}
```
## Output example

```
[1, 2, 3]
```

## Code explanation

- `fn print_slice(slice: &[i32])`: This is the function definition, which takes a slice of type `i32` as a parameter.
- `let arr = [1, 2, 3]`: This is the array that will be passed as a parameter.
- `print_slice(&arr)`: This is the function call, which passes the array as a parameter.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust Documentation - Function Parameters](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#function-parameters)

group: rust-slice