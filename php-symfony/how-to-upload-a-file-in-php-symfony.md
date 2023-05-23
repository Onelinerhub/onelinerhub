# How to upload a file in PHP Symfony?
// plain

Uploading a file in PHP Symfony is a simple process.

1. Create a form with a file input field:
```
$form = $this->createFormBuilder()
    ->add('file', FileType::class)
    ->getForm();
```

2. Handle the form submission:
```
$form->handleRequest($request);

if ($form->isSubmitted() && $form->isValid()) {
    // ...
}
```

3. Get the file from the request:
```
$file = $form->get('file')->getData();
```

4. Move the file to the desired location:
```
$fileName = $this->generateUniqueFileName().'.'.$file->guessExtension();

try {
    $file->move(
        $this->getParameter('files_directory'),
        $fileName
    );
} catch (FileException $e) {
    // ...
}
```

5. Save the file name to the database:
```
$entity->setFileName($fileName);
$entityManager->persist($entity);
$entityManager->flush();
```

For more information, please refer to the [Symfony documentation](https://symfony.com/doc/current/controller/upload_file.html).

onelinerhub: [How to upload a file in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-upload-a-file-in-php-symfony)