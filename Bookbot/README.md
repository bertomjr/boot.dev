# Bookbot

A command-line text analyzer built with Python as my first [Boot.dev](https://www.boot.dev) project. Bookbot reads a text file, counts its words, and reports how often each letter appears.

Built while following [Boot.dev's Build Bookbot guided project](https://www.boot.dev/courses/build-bookbot-python), this project helped me practice file handling, functions, dictionaries, and sorting.

[Back to my Boot.dev projects](../README.md)

## Features

- Accepts a text file path as a command-line argument.
- Reports the total word count.
- Counts letters without distinguishing uppercase from lowercase.
- Lists letter frequencies from highest to lowest.
- Prints a usage message when the required file path is missing or extra arguments are provided.

## Built with

- **Python 3.9 or newer** — the code uses built-in collection type annotations.
- **Python's standard library** — no third-party packages are required.

## Run locally

With Git and Python installed, clone the collection and open the Bookbot folder:

```bash
git clone https://github.com/bertomjr/boot.dev.git
cd boot.dev/Bookbot
```

Analyze one of the included books:

```bash
python3 main.py books/frankenstein.txt
```

You can also try:

```bash
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

If you already cloned the repository, open its `Bookbot` folder and run one of the commands above. On systems where Python 3 is invoked with `python` instead of `python3`, use that command name.

To analyze your own text file, supply its path. Put paths containing spaces in quotes:

```bash
python3 main.py "/path/to/your book.txt"
```

Relative paths are resolved from the directory where you run the command.

## Example output

The following excerpt comes from running Bookbot on the included `books/frankenstein.txt`:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
```

The report continues with the remaining letters. Counts depend on the exact contents of the input file, including any introductory or closing text.

## How the counting works

- **Words:** the program splits the text on whitespace. Punctuation attached to a word stays part of that word.
- **Letters:** the text is converted to lowercase before characters are counted, so `A` and `a` contribute to the same count.
- **Report:** only characters recognized as alphabetic by Python's `isalpha()` method are displayed, including accented letters. Spaces, digits, and punctuation are omitted from the letter report.

## What I practiced

- Reading text files with `open()` and a context manager.
- Accepting command-line arguments through `sys.argv`.
- Accumulating character frequencies in a dictionary.
- Converting dictionary entries into tuples and sorting them by count.
- Separating text analysis from file handling and report output.
- Adding type annotations to describe function inputs and return values.

## Project structure

| File or folder | Purpose |
| --- | --- |
| [`main.py`](./main.py) | Validates arguments, reads the file, and prints the report |
| [`stats.py`](./stats.py) | Counts words and characters, then sorts the character frequencies |
| [`books/`](./books/) | Included text files for trying the program |

## Current limitations

- The entire file is loaded into memory before analysis.
- Missing, unreadable, or incompatible text files produce Python errors; custom error messages are not implemented yet.

## Credits

Built while following [Boot.dev's Build Bookbot course](https://www.boot.dev/courses/build-bookbot-python). Boot.dev provides the project brief and instruction; this repository contains my work on the guided project.

Project by [Roberto Marcillo Jr.](https://github.com/bertomjr)
