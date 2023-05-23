# How to use Collection with PHP Symfony?
// plain

Collection is a powerful tool for managing data in PHP Symfony. It allows you to store, manipulate and retrieve data in an efficient and organized way.

## Example code

```
use Symfony\Component\Form\Extension\Core\Type\CollectionType;

$form = $this->createFormBuilder()
    ->add('tags', CollectionType::class, [
        'entry_type' => TextType::class,
        'allow_add' => true,
        'allow_delete' => true,
    ])
    ->getForm();
```

This example code creates a form with a collection field called 'tags'. The 'entry_type' option specifies the type of data that will be stored in the collection. The 'allow_add' and 'allow_delete' options enable users to add and delete entries from the collection.

## Output example

```
Form object
```

## Code explanation

- `use Symfony\Component\Form\Extension\Core\Type\CollectionType;` - imports the CollectionType class from the Symfony Form component
- `$form = $this->createFormBuilder()` - creates a new form builder object
- `->add('tags', CollectionType::class, [` - adds a collection field to the form
- `'entry_type' => TextType::class,` - specifies the type of data that will be stored in the collection
- `'allow_add' => true,` - enables users to add entries to the collection
- `'allow_delete' => true,` - enables users to delete entries from the collection
- `->getForm();` - returns the form object

## Helpful links
- [Symfony Form Component Documentation](https://symfony.com/doc/current/forms.html)
- [CollectionType Class Documentation](https://symfony.com/doc/current/reference/forms/types/collection.html)

onelinerhub: [How to use Collection with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-collection-with-php-symfony)