# How to add day to date in Rust
// plain

Adding a day to a date in Rust can be done using the `add_days` method from the `chrono` crate. This method takes a `NaiveDate` and an `i64` as parameters and returns a new `NaiveDate` with the added days.

## Example code

```rust
use chrono::NaiveDate;

let date = NaiveDate::from_ymd(2020, 1, 1);
let new_date = date.add_days(1);

println!("{}", new_date);
```

## Output example

```
2020-01-02
```

## Code explanation

- `use chrono::NaiveDate`: imports the `NaiveDate` type from the `chrono` crate.
- `let date = NaiveDate::from_ymd(2020, 1, 1)`: creates a `NaiveDate` from the given year, month and day.
- `let new_date = date.add_days(1)`: adds one day to the given `NaiveDate`.
- `println!("{}", new_date)`: prints the new `NaiveDate` to the console.

## Helpful links
- [chrono crate documentation](https://docs.rs/chrono/0.4.11/chrono/)

group: rust-datetime