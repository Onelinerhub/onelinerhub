# Get unique values from array

```javascript
function listUnique(lista) {
            unique = [...new Set(lista)];
            console.log(unique);
        }
        listUnique([1, 2, 3, 4, 5, 5]);
```

-  O objeto Set permite que você armazene valores únicos de qualquer tipo, desde valores primitivos a referências a objetos.
- Sintaxe  
- new Set([iterable]);
-  Se um objeto iterável é passado, todos os seus elementos serão adicionados ao novo Set.
-  Se tal parâmetro não for específicado, ou se seu valor for null, o novo Set estará vazio.
