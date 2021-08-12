# Convert any ArrayList to Array

You can convert any reference typed `ArrayList` to array using `toArray` method of `ArrayList` class.

```java
T[] typedArray = typedList.toArray(T[]::new);
```

- T[] - is an array of reference type T.
- typedList - is an ArrayList of type T.
- toArray - is a method of ArrayList to convert ArrayList to an Array.
- T[]::new - is a method reference of IntFunction<T[]> generator.

## Example
```java
// initialization of ArrayList
ArrayList<Integer> typedList=new ArrayList<>();
// Adding 1 and 2 to ArrayList
typedList.add(1);
typedList.add(2);
//converting to Integer typed array
Integer[] typedArray = typedList.toArray(Integer[]::new);
// printing array to console
System.out.println(Arrays.toString(typedArray));
```
```text
[1, 2]
```
