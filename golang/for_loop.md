# Basic Go For Loop

### **Please note:**
- The totals shown here are for demonstrative purposes only and are not necessary for the loop to function.
- `i := 0;` is only executed before the loop starts.
- `i < 10;` is executed before each loop (to check that the condition is being met.)
- `i++` is executed at the end of each loop.

```golang
total := 0
itotal := 0
for i := 0; i < 10; i++ {
    total += 1
    i_total += i
}
fmt.Println(total)
fmt.Println(itotal)
```

- ``total := 0`` - define the loop total (optional)
- ``itotal := 0`` - define the cumulative total (optional)
- ``for`` - open the definition of the loop
- ``i := 0;`` - define the variable (`i`) that will be looped over (does not have to be 0)
- ``i < 10;`` - define the condition the loop will run on (could be `<=`, `>`, or `>=`)
- ``i++`` - define how much to increment `i` on each run of the loop
- ``{`` - close the definition of the loop, start the logic within it
- ``total += 1`` - increment the loop total by one (optional)
- ``itotal += i`` - add the current `i` to the cumulative total (optional)
- ``fmt.Println(total)`` - print the loop total, which is 10 (optional)
- ``fmt.Println(itotal)`` - print the cumulative total, which is 45 (optional)


