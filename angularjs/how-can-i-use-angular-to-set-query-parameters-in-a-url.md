# How can I use Angular to set query parameters in a URL?
// plain

Angular provides a built-in service called the `HttpParams` class which can be used to set query parameters in a URL. The `HttpParams` class is part of the `@angular/common/http` package and can be imported like so:

```typescript
import { HttpParams } from '@angular/common/http';
```

The `HttpParams` class provides several methods for creating and manipulating query parameters. For example, to create a new query parameter you can use the `set` method like so:

```typescript
const params = new HttpParams().set('key', 'value');
```

To add additional query parameters, you can use the `append` method like so:

```typescript
const params = new HttpParams().set('key', 'value').append('key2', 'value2');
```

The query parameters can then be used to create a URL like so:

```typescript
const url = `http://example.com/?${params.toString()}`;
// http://example.com/?key=value&key2=value2
```

The `HttpParams` class also provides several other useful methods for manipulating query parameters, including `delete`, `setAll`, `has`, `keys`, `get`, `getAll`, and `appendAll`.

For more information, see the official [Angular documentation](https://angular.io/guide/http#query-parameters).

onelinerhub: [How can I use Angular to set query parameters in a URL?](https://onelinerhub.com/angularjs/how-can-i-use-angular-to-set-query-parameters-in-a-url)