# How can I remove quotes from a Rust string?
// plain

Removing quotes from a Rust string can be done using the `trim_matches` method. This method takes two parameters, the first being the string to be trimmed and the second being the character to be trimmed.

## Example code

```
let my_string = "\"Hello World!\"";
let trimmed_string = my_string.trim_matches('"');
println!("{}", trimmed_string);
```

## Output example

```
Hello World!
```

## Code explanation

- `let my_string = "\"Hello World!\"";`: This line declares a string variable called `my_string` and assigns it the value `"Hello World!"`.
- `let trimmed_string = my_string.trim_matches('"');`: This line calls the `trim_matches` method on the `my_string` variable, passing in the character `"` as the second parameter. This will remove any quotes from the string.
- `println!("{}", trimmed_string);`: This line prints the value of the `trimmed_string` variable to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)