# How to get pointer to variable in Rust
// plain

In Rust, you can get a pointer to a variable by using the `&` operator. For example, if you have a variable `x` of type `i32`, you can get a pointer to it by writing `let x_ptr = &x`. The `&` operator returns a pointer to the variable, which can then be used to access the value of the variable. Additionally, you can use the `*` operator to dereference a pointer and access the value of the variable it points to. For example, if `x_ptr` is a pointer to `x`, you can access the value of `x` by writing `*x_ptr`.

group: rust-pointers