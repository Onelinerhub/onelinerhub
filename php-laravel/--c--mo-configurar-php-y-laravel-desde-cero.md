# ¿Cómo configurar PHP y Laravel desde cero?
// plain

Para configurar PHP y Laravel desde cero, deberá seguir los siguientes pasos:

1. Instalar PHP:

Para instalar PHP, primero deberá descargar la versión más reciente de PHP desde el sitio web oficial de PHP. Una vez descargado, deberá instalarlo en su sistema.

2. Instalar el marco de Laravel:

Una vez que haya instalado PHP, deberá descargar la versión más reciente de Laravel desde su sitio web oficial. Una vez descargado, deberá instalar el marco en su sistema.

3. Configurar la base de datos:

Deberá configurar una base de datos para su proyecto. Esto se puede hacer utilizando cualquier motor de base de datos compatible con Laravel, como MySQL, PostgreSQL, etc.

4. Crear un archivo .env:

Deberá crear un archivo .env en la raíz de su proyecto. El archivo .env contendrá todas las variables de entorno necesarias para la configuración de Laravel.

```
APP_NAME=My App
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_LOG_LEVEL=debug
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=my_app
DB_USERNAME=root
DB_PASSWORD=
```

5. Generar una clave de aplicación:

Deberá generar una clave de aplicación para su proyecto. Esto se puede hacer ejecutando el comando `php artisan key:generate` en la consola.

```
Application key [base64:h6yXCzj3VZ4+Vvhb1LX9yGzXyTQ/6pK/VXsIy+X6Mw=] set successfully.
```

6. Configurar el servidor web:

Deberá configurar un servidor web para su proyecto. Esto se puede hacer utilizando Apache, Nginx u otro servidor web compatible con Laravel.

7. Iniciar el servidor:

Una vez que haya configurado el servidor web, deberá iniciar el servidor. Esto se puede hacer ejecutando el comando `php artisan serve` en la consola.

```
Laravel development server started: <http://127.0.0.1:8000>
```

Una vez que haya completado estos pasos, estará listo para comenzar a desarrollar su aplicación con Laravel.

Referencias:

- [Sitio web oficial de PHP](https://www.php.net/)
- [Sitio web oficial de Laravel](https://laravel.com/)
- [Documentación de Laravel](https://laravel.com/docs/7.x)

onelinerhub: [¿Cómo configurar PHP y Laravel desde cero?](https://onelinerhub.com/php-laravel/--c--mo-configurar-php-y-laravel-desde-cero)