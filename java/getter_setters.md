# Getter and setter methods in java

When you start a class in java, you usually don't make properties of class publicly available to set a couple of rules for them to be edited.
This is called encapsulation in java.
Let's

```java
public class Example
{
  private int exampleProperty;

  public Example(int exampleProperty)
  {
      if (this.exampleProperty < 0) this.exampleProperty = 0;
      else this.exampleProperty = exampleProperty;
  }

  public int getExampleProperty()
  {
      return exampleProperty;
  }

  public void setExampleProperty(int exampleProperty)
  {
      if (this.exampleProperty < 0) this.exampleProperty = 0;
      else this.exampleProperty = exampleProperty;
  }

}
```

- public Example(int exampleProperty) - Constructor for Example class
- public int getExampleProperty() - Getter method which returns the property exampleProperty
- public void setExampleProperty(int exampleProperty) - Setter method which sets the exampleProperty to integer it is passed to if it is a positive number
