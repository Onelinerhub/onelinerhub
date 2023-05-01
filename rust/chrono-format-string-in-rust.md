# Chrono format string in Rust
// plain

The chrono crate in Rust provides a powerful set of tools for working with dates and times. It also provides a formatting system for displaying dates and times in a variety of formats. The format string is used to specify the format of the output.

The following ## Code example shows how to use the chrono format string to display the current date and time in the format "YYYY-MM-DD HH:MM:SS":

```rust
use chrono::{Local, DateTime};

let now: DateTime<Local> = Local::now();
let formatted_date_time = now.format("%Y-%m-%d %H:%M:%S").to_string();

println!("The current date and time is: {}", formatted_date_time);
```

### Output

The current date and time is: 2020-09-17 15:45:02

## Explanation of code parts:

1. `use chrono::{Local, DateTime};` - This imports the Local and DateTime modules from the chrono crate.

2. `let now: DateTime<Local> = Local::now();` - This creates a DateTime object representing the current date and time using the Local timezone.

3. `let formatted_date_time = now.format("%Y-%m-%d %H:%M:%S").to_string();` - This uses the chrono format string to format the DateTime object into a string in the format "YYYY-MM-DD HH:MM:SS".

4. `println!("The current date and time is: {}", formatted_date_time);` - This prints the formatted date and time string to the console.

## Helpful links:

1. [Chrono crate documentation](https://docs.rs/chrono/0.4.11/chrono/)
2. [Chrono format string reference](https://docs.rs/chrono/0.4.11/chrono/format/strftime/index.html)