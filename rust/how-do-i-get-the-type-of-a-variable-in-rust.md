# How do I get the type of a variable in Rust?
// plain

You can get the type of a variable in Rust using the `std::any::type_name` function. This function takes a reference to a variable and returns a string containing the type of the variable.

## Example code

```
let x = 5;
let type_of_x = std::any::type_name(&x);
println!("Type of x is {}", type_of_x);
```

## Output example

```
Type of x is i32
```

## Code explanation

- `let x = 5;`: This declares a variable `x` with the value `5`.
- `let type_of_x = std::any::type_name(&x);`: This calls the `std::any::type_name` function with a reference to the variable `x` and assigns the returned string to the variable `type_of_x`.
- `println!("Type of x is {}", type_of_x);`: This prints the string stored in `type_of_x` to the console.

## Helpful links
- [std::any::type_name](https://doc.rust-lang.org/std/any/fn.type_name.html)

group: rust-variables