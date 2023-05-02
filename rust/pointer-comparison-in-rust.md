# Pointer comparison in Rust
// plain

In Rust, pointer comparison is done using the PartialEq trait. This trait allows two pointers to be compared for equality, and it is implemented for all types of pointers. To compare two pointers, the == operator is used. For example, the following code compares two pointers of type i32:
```rust
let ptr1 = &10;
let ptr2 = &20;

if ptr1 == ptr2 {
    println!("The pointers are equal");
} else {
    println!("The pointers are not equal");
}
```
The output of this code will be "The pointers are not equal". This is because the two pointers point to different values.

It is also possible to compare two pointers of different types. For example, the following code compares two pointers of type i32 and i64:

```rust
let ptr1 = &10i32;
let ptr2 = &20i64;

if ptr1 == ptr2 {
    println!("The pointers are equal");
} else {
    println!("The pointers are not equal");
}
```
The output of this code will be "The pointers are not equal". This is because the two pointers point to different types of values.

In summary, pointer comparison in Rust is done using the PartialEq trait and the == operator. It is possible to compare two pointers of different types, but they must point to the same type of value in order for them to be considered equal.

## Helpful links
- [Rust Documentation - PartialEq](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- [Rust Documentation - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Documentation - Operators](https://doc.rust-lang.org/book/ch03-02-operators-and-overloading.html)

group: rust-pointers