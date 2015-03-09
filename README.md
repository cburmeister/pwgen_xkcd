pwgen_xkcd
===========

Generate an xkcd passphrase randomly selected from a list of words.

---

## Install

```bash
$ python setup.py install
```

## Usage

Check out the help for all available arguments:

```
Usage: pwgen_xkcd [OPTIONS] FILENAME

    Generate an xkcd passphrase randomly selected from a list of words.

Options:
    --n INTEGER                Number of passphrases to generate.
    --max_words INTEGER        Number of words.
    --min_word_length INTEGER  Minimum word length.
    --max_word_length INTEGER  Maxmimum word length.
    --help                     Show this message and exit.
```

## Example

Using a local dictionary:

```bash
$ pwgen_xkcd --n 1 /usr/share/dict/words
juicycoffeespoilenigma
```
