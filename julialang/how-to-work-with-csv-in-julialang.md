# How to work with CSV in JuliaLang?
// plain

JuliaLang provides a CSV package to work with CSV files. It provides functions to read and write CSV files.

Example code to read a CSV file:
```
using CSV

csv_file = CSV.File("my_file.csv")

for row in csv_file
    println(row)
end
```

## Output example

```
CSV.Row:
 :name  Some Name
 :email  some@email.com
```

## Code explanation

- `using CSV`: imports the CSV package
- `CSV.File("my_file.csv")`: reads the CSV file
- `for row in csv_file`: iterates over the rows of the CSV file
- `println(row)`: prints the row

## Helpful links
- [JuliaLang CSV package](https://juliadata.github.io/CSV.jl/stable/)
- [JuliaLang CSV tutorial](https://www.tutorialspoint.com/julia_programming/julia_csv.htm)

onelinerhub: [How to work with CSV in JuliaLang?
](https://onelinerhub.com/julialang/how-to-work-with-csv-in-julialang)
