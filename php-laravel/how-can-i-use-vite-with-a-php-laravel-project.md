# How can I use Vite with a PHP Laravel project?
// plain

Using Vite with a PHP Laravel project is a simple process.

1. Install Vite globally with `npm install -g @vitejs/cli`.
2. Create a `vite.config.js` file in your project root directory.
```js
// vite.config.js
module.exports = {
  // ...
  build: {
    vueCompiler: true,
    rollupOptions: {
      plugins: [
        require('rollup-plugin-php-laravel')()
      ]
    }
  }
}
```
3. Run `vite` in the project root directory.
4. Add your Laravel project files to the `src` directory.
5. Vite will automatically detect and compile your Laravel files.
6. Access your Laravel project in the browser at `http://localhost:3000`.
7. To build for production, run `vite build`.

For more information on using Vite with Laravel, see the [Vite documentation](https://github.com/vitejs/vite/blob/master/README.md#php-laravel).

onelinerhub: [How can I use Vite with a PHP Laravel project?](https://onelinerhub.com/php-laravel/how-can-i-use-vite-with-a-php-laravel-project)