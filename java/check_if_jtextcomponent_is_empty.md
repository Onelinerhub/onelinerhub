# Method to check if a JTextComponent is empty

```java
public static <T extends JTextComponent> boolean isFieldEmpty (T field)
    {
        return field.getText().trim().isEmpty();
    }
```

- <T extends JTextComponent> - a generic expression, means the data type T that method takes should be a child of JTextComponent class.
- field.getText().trim().isEmpty() - gets the text inside field, trims the whitespace around, returns true if it is an empty string else false.
