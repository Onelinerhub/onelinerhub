# Array pointer example in Rust
// plain

An array pointer in Rust is a pointer that points to the first element of an array. This allows us to access the elements of the array without having to pass the entire array. An example of an array pointer in Rust is shown below:
```rust
let arr = [1, 2, 3, 4];
let ptr = &arr[0];
```
Here, `ptr` is a pointer to the first element of the array `arr`. We can then access the elements of the array using the pointer, as shown below:
```rust
println!("{}", *ptr); // prints 1
println!("{}", *(ptr + 1)); // prints 2
println!("{}", *(ptr + 2)); // prints 3
println!("{}", *(ptr + 3)); // prints 4
```
The output of the above code will be:
```
1
2
3
4
```
In the code, the `*` operator is used to dereference the pointer and access the value of the element it points to. The `ptr + n` expression is used to access the nth element of the array.

## Helpful links
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-02-pointers.html)
- [Rust Arrays](https://doc.rust-lang.org/book/ch08-03-arrays.html)
- [Rust Dereferencing](https://doc.rust-lang.org/book/ch15-02-deref.html)

group: rust-pointers