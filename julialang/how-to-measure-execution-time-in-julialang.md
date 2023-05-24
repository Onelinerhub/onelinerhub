# How to measure execution time in JuliaLang?
// plain

Measuring execution time in JuliaLang is easy and straightforward. The `@time` macro can be used to measure the execution time of any expression. For example:

```
@time begin
    x = rand(1000, 1000)
    y = rand(1000, 1000)
    z = x * y
end
```

The output of the above code will be:

```
  0.001445 seconds (1.02 k allocations: 52.906 KiB)
```

The `@time` macro measures the total execution time of the expression, including the time taken for memory allocation. It also prints the number of allocations and the amount of memory allocated.

The `@elapsed` macro can also be used to measure the execution time of an expression. It is similar to `@time` but does not print the number of allocations and the amount of memory allocated.

## Helpful links

- [Julia Documentation - @time](https://docs.julialang.org/en/v1/manual/performance-tips/index.html#Timing-Code-1)
- [Julia Documentation - @elapsed](https://docs.julialang.org/en/v1/manual/performance-tips/index.html#Timing-Code-1)

onelinerhub: [How to measure execution time in JuliaLang?](https://onelinerhub.com/julialang/how-to-measure-execution-time-in-julialang)