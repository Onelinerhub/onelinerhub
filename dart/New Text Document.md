RegExp hexColor = RegExp(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$');
hexColor.hasMatch('#4gh');     // true
hexColor.hasMatch('#FFFFFF');  // true
hexColor.hasMatch('#0001100z'); // false