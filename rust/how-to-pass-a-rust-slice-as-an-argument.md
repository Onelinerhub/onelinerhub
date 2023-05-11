# How to pass a Rust slice as an argument?
// plain

Passing a Rust slice as an argument is done by using the `&[T]` syntax. This syntax indicates that a reference to a slice of type `T` is being passed.

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

- `fn print_slice(slice: &[i32])`: This is a function that takes a reference to a slice of type `i32` as an argument.
- `let arr = [1, 2, 3]`: This creates an array of type `i32` with the values `1`, `2`, and `3`.
- `print_slice(&arr)`: This passes a reference to the array `arr` to the function `print_slice`.

## Helpful links
- [Rust Documentation - Slices](https://doc.rust-lang.org/book/ch04-03-slices.html)
- [Rust Documentation - References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-slice