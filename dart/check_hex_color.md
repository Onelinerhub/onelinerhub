# Validate Hex Colors in dart

```dart
RegExp hexColor = RegExp(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$');
```
- Check wether the given valse is correct Hex color or not
- Given regex will match an arbitrary hexadecimal color value that can be used in CSS
- hasMatch() is built in function to compare value in dart.

## Example
```dart
void main() {
  RegExp hexColor = RegExp(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$');
  print(hexColor.hasMatch('#4gh'));     
  print(hexColor.hasMatch('#FFFFFF'));  
  print(hexColor.hasMatch('#0001100z')); 
}

```
```
false
true
false
```
