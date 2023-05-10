# How do I create a class variable in Rust?
// plain

Class variables in Rust are called `static` variables. They are declared using the `static` keyword and can be accessed from anywhere in the code.

## Example code

```
static MY_VAR: i32 = 5;

fn main() {
    println!("The value of MY_VAR is: {}", MY_VAR);
}
```

## Output example

```
The value of MY_VAR is: 5
```

## Code explanation

- `static`: keyword used to declare a static variable
- `MY_VAR`: name of the static variable
- `i32`: type of the static variable
- `5`: value of the static variable
- `println!`: macro used to print the value of the static variable

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables)
- [Rust Documentation - Statics](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#statics)

group: rust-variables