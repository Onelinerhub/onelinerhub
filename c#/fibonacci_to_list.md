# How to retrieve numeric fibonacci list up to 10

``` C#
List<long> Fib = new List<long>(); Enumerable.Range(0,10).ToList().ForEach(n => (Fib).Add(n <= 1 ? 1 : Fib[n-2] + Fib[n-1]));
```
- new List<long>(); - create an empty list of large integers
- Enumerable.Range(0,10) - get an enumerable list populated with integers from 0 to 10
- .ToList() - convert the enumerable list to a standard list
- .ForEach - apply a specific arrow function for each and every one item in the list
- n => (Fib).Add - arrow function used to add an item n to enumerable list Fib based on a condition for every one item in the list
- n <= 1 ? 1 : Fib[n-2] + Fib[n-1] - check if n less or equal to 1 then return 1, if n is larger then return addition of elements [n-2] and [n-1] in Fib list for every n
