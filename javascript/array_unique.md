# Get unique values from array

```javascript
function listUnique(lista) {
            unique = [...new Set(lista)];
            console.log(unique);
        }
        listUnique([1, 2, 3, 4, 5, 5]);
```

- The Set object lets you store unique values ​​of any type, from primitive values ​​to object references.
- Syntax  
- new Set([iterable]);
- If an iterable object is passed, all its elements will be added to the new Set.
- If such parameter is not specified, or if its value is null, the new Set will be empty.
