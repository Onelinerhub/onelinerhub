# Check Hex Colors

```dart
RegExp hexColor = RegExp(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$');
hexColor.hasMatch('#4gh');     // true
hexColor.hasMatch('#FFFFFF');  // true
hexColor.hasMatch('#0001100z'); // false
```
- It will check is given input is proper hex color or not
