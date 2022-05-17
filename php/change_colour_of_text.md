# How to change color of CLI text

### Please note, this is only usable at the command line.
Foreground colours have alternate codes; they are made by using `1;` rather than `0;`, and change the tone or heaviness of the base `0` colour, depending on the terminal used.

| Colour         | Foreground Code | Background Code |
|----------------|-----------------|-----------------|
| Black	         | 0;30            | 40              |
| Dark Grey	     | 1;30            | n/a             |
| Red	           | 0;31            | 41              |
| Light Red	     | 1;31            | n/a             |
| Green	         | 0;32            | 42              |
| Light Green    | 1;32            | n/a             |
| Brown	         | 0;33            | n/a             |
| Yellow         | 1;33            | 43              |
| Blue           | 0;34            | 44              |
| Light Blue     | 1;34            | n/a             |
| Magenta        | 0;35            | 45              |
| Light Magenta	 | 1;35            | n/a             |
| Cyan	          | 0;36            | 46              |
| Light Cyan     | 1;36            | n/a             |
| Light Grey     | 0;37            | 47              |
| White	         | 1;37            | n/a             |

```php
"\e[0;34;43mYour text here\e[0m"
```

- ``[0;34`` - set the foreground colour to blue
- ``;42`` - set the background colour to yellow (optional)
- ``m`` - close the colour-setting portion
- ``Your text here`` - the text to be outputted
- ``\e[0m"`` - reset the colour to the default


