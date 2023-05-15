# How to use csvkit on Windows?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used on Windows with the help of the Windows Subsystem for Linux (WSL).

To use csvkit on Windows, first install the Windows Subsystem for Linux (WSL) by following the instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Once WSL is installed, open the Linux terminal and install csvkit with the following command:

```
sudo apt-get install csvkit
```

This will install csvkit and its dependencies.

To use csvkit, you can use the command line tools to convert, filter, and manipulate CSV files. For example, to convert a CSV file to a JSON file, you can use the `csvjson` command:

```
csvjson input.csv > output.json
```

This will convert the CSV file `input.csv` to a JSON file `output.json`.

For more information on csvkit and its command line tools, please refer to the [csvkit documentation](https://csvkit.readthedocs.io/en/latest/).

onelinerhub: [How to use csvkit on Windows?](https://onelinerhub.com/csvkit/how-to-use-csvkit-on-windows)