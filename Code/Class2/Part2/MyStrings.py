
import string


def remove_punctuation(string):
    string_punc="How does Python deal with this? I actually don't know!! Let's see what comes out."
    nopunc = [char for char in string_punc if char not in string.punctuation]
    nopunc = ''.join(nopunc).lower()
    return nopunc