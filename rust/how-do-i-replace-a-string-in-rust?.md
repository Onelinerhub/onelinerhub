# How do I replace a string in Rust?
// plain

Replacing a string in Rust is a simple task that can be accomplished using the `replace` method. This method takes two parameters, the first being the string to be replaced and the second being the string to replace it with.

## Example

```
let my_string = "Hello World!";
let new_string = my_string.replace("World", "Rust");
println!("{}", new_string);
```
## Output example

```
Hello Rust!
```

The code above replaces the string "World" with "Rust" in the variable `my_string`. The `replace` method returns a new string with the replaced value.

## Code explanation

- `let my_string = "Hello World!";`: This line declares a variable `my_string` and assigns it the value "Hello World!".
- `let new_string = my_string.replace("World", "Rust");`: This line calls the `replace` method on the `my_string` variable, replacing the string "World" with "Rust".
- `println!("{}", new_string);`: This line prints the new string with the replaced value to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)