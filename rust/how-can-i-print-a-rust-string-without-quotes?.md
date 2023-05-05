# How can I print a Rust string without quotes?
// plain

You can print a Rust string without quotes by using the `print!` macro. This macro will print the string without any quotation marks.

## Example code

```
let my_string = "Hello World!";
print!("{}", my_string);
```

## Output example

```
Hello World!
```

The code above consists of two parts:

1. `let my_string = "Hello World!";` - This line declares a variable called `my_string` and assigns it the value of the string `"Hello World!"`.

2. `print!("{}", my_string);` - This line uses the `print!` macro to print the value of the `my_string` variable without any quotation marks. The `{}` is a placeholder for the value of `my_string`.

## Helpful links

- [Rust Documentation - print! macro](https://doc.rust-lang.org/std/macro.print.html)