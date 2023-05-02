# How to copy pointer in Rust
// plain

In Rust, pointers can be copied by using the `.clone()` method. This method creates a deep copy of the pointer, meaning that the new pointer will point to the same memory address as the original pointer. To demonstrate this, consider the following ## Code example:
```rust
let mut x = 5;
let mut y = &mut x;
let z = y.clone();

*y = 10;

println!("x = {}", x);
println!("y = {}", *y);
println!("z = {}", *z);
```

### Output example
```
x = 10
y = 10
z = 5
```

### Explanation
In this example, `x` is a mutable variable with an initial value of `5`. `y` is a mutable pointer to `x`, and `z` is a clone of `y`. The value of `x` is then changed to `10` using the `*y` syntax, which dereferences `y` and assigns the new value to `x`. The output of the code shows that `x` and `y` have the same value of `10`, while `z` still has the original value of `5`. This demonstrates that `z` is a deep copy of `y`, and that the two pointers point to the same memory address.

### Relevant links
- [Rust Documentation - Pointers](https://doc.rust-lang.org/book/ch19-02-pointers.html)
- [Rust Documentation - Cloning](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Rust by Example - Pointers](https://doc.rust-lang.org/rust-by-example/scope/borrow/ref.html)

group: rust-pointers