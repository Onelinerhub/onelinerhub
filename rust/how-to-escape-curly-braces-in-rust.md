# How to escape curly braces in Rust
// plain

Curly braces in Rust can be escaped by using a backslash (`\`) before the opening brace. For example, the following code:

```
let x = \{1, 2, 3\};
```

will ### Output

```
let x = {1, 2, 3};
```

The backslash is used to indicate that the curly brace should be treated as a literal character, rather than as a special character. This is useful when you want to include a literal curly brace in a string or other data type.

## Explanation:
- The backslash (`\`) is used to escape special characters in Rust.
- The backslash is placed before the opening curly brace to indicate that it should be treated as a literal character, rather than as a special character.
- This is useful when you want to include a literal curly brace in a string or other data type.

## Helpful links:
- https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html
- https://doc.rust-lang.org/reference/tokens.html