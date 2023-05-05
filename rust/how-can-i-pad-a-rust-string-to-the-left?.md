# How can I pad a Rust string to the left?
// plain

You can pad a Rust string to the left using the `pad_start` method. This method takes two parameters, the first being the desired length of the string and the second being the character to pad the string with.

For example:
```
let s = "Hello".to_string();
let padded = s.pad_start(10, ' ');
println!("{}", padded);
```

## Output example

```
    Hello
```

The code above pads the string `Hello` with spaces until it reaches a length of 10 characters.

The parts of the code are:
- `let s = "Hello".to_string();`: This creates a string from the literal `Hello`.
- `let padded = s.pad_start(10, ' ');`: This calls the `pad_start` method on the string `s` with the parameters `10` and `' '` (a single space character).
- `println!("{}", padded);`: This prints the padded string to the console.

## Helpful links
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)