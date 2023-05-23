# How to use the Process component in PHP Symfony?
// plain

The Process component in PHP Symfony is used to execute commands in sub-processes. It provides a simple API to run commands in sub-processes and to manage their input and output.

## Example code

```
use Symfony\Component\Process\Process;

$process = new Process('ls -lsa');
$process->run();

// executes after the command finishes
if ($process->isSuccessful()) {
    echo $process->getOutput();
}
```

## Output example

```
total 8
drwxr-xr-x  3 user  staff   96  8 Jul 16:17 .
drwxr-xr-x  8 user  staff  256  8 Jul 16:17 ..
-rw-r--r--  1 user  staff    0  8 Jul 16:17 test.txt
```

## Code explanation


1. `use Symfony\Component\Process\Process;` - This imports the Process class from the Symfony Process component.

2. `$process = new Process('ls -lsa');` - This creates a new Process object with the command `ls -lsa` as an argument.

3. `$process->run();` - This runs the command in a sub-process.

4. `if ($process->isSuccessful()) {` - This checks if the command was executed successfully.

5. `echo $process->getOutput();` - This prints the output of the command.

## Helpful links

- [Symfony Process Component Documentation](https://symfony.com/doc/current/components/process.html)

onelinerhub: [How to use the Process component in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-the-process-component-in-php-symfony)