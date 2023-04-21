# How to format dates and times in Rust?
// plain

Rust has a library called chrono which provides functions for formatting dates and times.

The following example shows how to format a date and time using chrono:

```rust
use chrono::{DateTime, Utc};

fn main() {
    // Create a DateTime object
    let dt = Utc::now();
    println!("Current date and time: {}", dt);

    // Format the DateTime object
    let formatted_dt = dt.format("%Y-%m-%d %H:%M:%S").to_string();
    println!("Formatted date and time: {}", formatted_dt);
}
```

The output of the above code would be:

```
Current date and time: 2020-11-09 11:55:06.874117 UTC
Formatted date and time: 2020-11-09 11:55:06
```