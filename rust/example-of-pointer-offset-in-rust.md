# Example of pointer offset in Rust
// plain

Pointer offset in Rust is a way to access a specific element in a data structure. It is done by adding an offset to a pointer. For example, if we have a pointer to the beginning of an array, we can add an offset to it to access a specific element in the array. To do this, we use the offset operator, which is written as `&[offset]`. For example, if we have an array of integers, we can access the third element by writing `&[2]`. The ## Code example below shows how to use pointer offset in Rust.

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
    let ptr = &arr[0];
    let third_element = &ptr[2];
    println!("Third element is {}", third_element);
}
```

Output example:
```
Third element is 3
```

## Explanation

In the ## Code example, we first create an array of integers called `arr`. Then, we create a pointer to the beginning of the array using the `&` operator. We then use the offset operator `&[offset]` to access the third element in the array. Finally, we print out the third element using the `println!` macro.

## Helpful links
- [Rust Pointer Offset](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#using-the-offset-operator)
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-02-pointers.html)
- [Rust Arrays](https://doc.rust-lang.org/book/ch08-03-arrays.html)

group: rust-pointers