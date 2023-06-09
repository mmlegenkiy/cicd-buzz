import unittest

from buzz import generator


def test_sample_single_word():
    lst = ('foo', 'bar', 'foobar')
    word = generator.sample(lst)
    assert word in lst


def test_sample_multiple_words():
    lst = ('foo', 'bar', 'foobar')
    words = generator.sample(lst, 2)
    assert len(words) == 2
    assert words[0] in lst
    assert words[1] in lst
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
