# How to use Sonata with Symfony and PHP?
// plain

Sonata is a bundle for Symfony and PHP that provides an admin generator and a set of useful features for developers. To use Sonata, you need to install the bundle and configure it in your Symfony project.

```
composer require sonata-project/admin-bundle
```

Once installed, you need to enable the bundle in your `app/AppKernel.php` file:

```
// app/AppKernel.php

public function registerBundles()
{
    $bundles = array(
        // ...
        new Sonata\AdminBundle\SonataAdminBundle(),
    );
}
```

You can then configure the bundle in your `config.yml` file:

```
# app/config/config.yml

sonata_admin:
    title:      My Admin
    title_logo: bundles/acmedemo/img/logo.png
    templates:
        layout:  AcmeDemoBundle::standard_layout.html.twig
```

Finally, you can create your admin classes and configure them in your `routing.yml` file:

```
# app/config/routing.yml

admin_acme_demo_post:
    resource: "@AcmeDemoBundle/Resources/config/admin_post.yml"
    prefix:   /admin
```

## Helpful links

- [SonataAdminBundle Documentation](https://sonata-project.org/bundles/admin/master/doc/index.html)
- [SonataAdminBundle GitHub Repository](https://github.com/sonata-project/SonataAdminBundle)

onelinerhub: [How to use Sonata with Symfony and PHP?](https://onelinerhub.com/php-symfony/how-to-use-sonata-with-symfony-and-php)