DERIVATIONAL_SUFFIXES = [
    "liw", "iw",
    "ish", "esh",
    "ik",
    "an",
    "ez",
    "el",
    "iz",
    "lew",
    "ew",
    "il",
    "ek",
    "sh",
    "z",
    "w"
]

FINAL_VOWELS = ["a", "e", "i"]

MIN_ROOT_LENGTH = 3


def remove_derivational_suffix(word, removed):

    for suffix in sorted(DERIVATIONAL_SUFFIXES, key=len, reverse=True):

        if suffix in removed:
            continue

        if word.endswith(suffix):

            new_word = word[:-len(suffix)]

            if len(new_word) < MIN_ROOT_LENGTH:
                continue

           
            if new_word.endswith(("mb", "nd", "ng", "ch", "sh")):
                return new_word, suffix

            if new_word.endswith(("bi", "li", "zi")):
                continue

            return new_word, suffix

    return word, None


def remove_final_vowel(word, removed):

    if word.endswith(tuple(FINAL_VOWELS)):

       
        if any(v in removed for v in FINAL_VOWELS):
            return word, None

        new_word = word[:-1]

        if len(new_word) < MIN_ROOT_LENGTH:
            return word, None

        return new_word, word[-1]

    return word, None

def strip_suffixes(word):

    removed = []
    changed = True

    while changed:
        changed = False

        new_word, s = remove_derivational_suffix(word, removed)

        if s:
            word = new_word
            removed.append(s)
            changed = True
            continue

        new_word, s = remove_final_vowel(word, removed)

        if s:
            word = new_word
            removed.append(s)
            changed = True

    return word, removed