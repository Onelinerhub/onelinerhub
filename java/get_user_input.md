# Method to get user input

```java
public String getUserInput()
{
  Scanner s = new Scanner(System.in);
  String input = s.nextLine();
  return input;
}
```

- Scanner s = new Scanner(System.in) - Instance to read user input
- String input = s.nextLine() - Blocking code which waits for a user input
