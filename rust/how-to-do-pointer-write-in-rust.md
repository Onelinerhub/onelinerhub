# How to do pointer write in Rust
// plain

In Rust, pointers are used to refer to a memory location and can be dereferenced to access the data stored at that location. To write a pointer in Rust, you need to use the asterisk (*) operator. For example, to declare a pointer to an integer, you would write:
```
let x = 5;
let ptr = &x;
```
Here, `ptr` is a pointer to the integer `x`. To dereference the pointer, you can use the asterisk operator:
```
let y = *ptr;
```
This will assign the value of `x` to `y`.

Output example:
```
let x = 5;
let ptr = &x;
let y = *ptr;
```

## Explanation
 In the first line, we declare an integer `x` with the value of 5. In the second line, we declare a pointer `ptr` to the integer `x` using the `&` operator. Finally, in the third line, we dereference the pointer `ptr` using the asterisk operator `*` and assign the value of `x` to `y`.

## Helpful links
- [Rust Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Reference](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-reference-operator)
- [Rust Dereference](https://doc.rust-lang.org/book/ch19-02-mutability.html#dereferencing-references)

group: rust-pointers