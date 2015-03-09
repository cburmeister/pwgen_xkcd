#!/usr/bin/python

import click
import random


@click.command()
@click.argument('filename', type=click.File('r'))
@click.option('--n', default=10, help='Number of passphrases to generate.')
@click.option('--max_words', default=4, help='Number of words.')
@click.option('--min_word_length', default=4, help='Minimum word length.')
@click.option('--max_word_length', default=8, help='Maxmimum word length.')
def main(filename, n, max_words, min_word_length, max_word_length):
    """
    Generate an xkcd passphrase randomly selected from a list of words.
    """
    def get_words(filename):
        return filename.readlines() 

    def get_candidates(words, min_length, max_length):
        return [x for x in words if min_length <= len(x) <= max_length]

    def get_random_words(words, num_words):
        return random.sample(words, num_words)

    def get_phrase(words):
        return ''.join([x.strip().lower() for x in words])

    words = get_words(filename)
    candidates = get_candidates(words, min_word_length, max_word_length)

    for _ in range(0, n):
        random_words = get_random_words(candidates, max_words)
        click.echo(get_phrase(random_words))


if __name__ == "__main__":
   main()
