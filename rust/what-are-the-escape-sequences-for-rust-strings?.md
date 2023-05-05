# What are the escape sequences for Rust strings?
// plain

Rust strings support a variety of escape sequences to represent special characters. The following are the escape sequences for Rust strings:

1. `\n`: This is used to represent a new line.

## Example code

```
let s = "Hello\nWorld";
println!("{}", s);
```

## Output example

```
Hello
World
```

2. `\t`: This is used to represent a tab character.

## Example code

```
let s = "Hello\tWorld";
println!("{}", s);
```

## Output example

```
Hello	World
```

3. `\r`: This is used to represent a carriage return.

## Example code

```
let s = "Hello\rWorld";
println!("{}", s);
```

## Output example

```
World
```

4. `\0`: This is used to represent the null character.

## Example code

```
let s = "Hello\0World";
println!("{}", s);
```

## Output example

```
Hello
```

5. `\\`: This is used to represent a backslash character.

## Example code

```
let s = "Hello\\World";
println!("{}", s);
```

## Output example

```
Hello\World
```

## Helpful links
- [Rust Strings](https://doc.rust-lang.org/book/ch08-02-strings.html)
- [Rust Escape Sequences](https://doc.rust-lang.org/reference/tokens.html#escape-sequences)