# =========================
# SUFFIX LIST (FROM YOUR TABLE)
# =========================

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
    "w",
    "i",
    "a"
]

# =========================
# SETTINGS
# =========================

MIN_ROOT_LENGTH = 3


# =========================
# REMOVE ONE SUFFIX
# =========================

def remove_suffix_once(word, removed_set):

    # =========================
    # 1. DERIVATIONAL SUFFIXES FIRST
    # =========================
    for suffix in sorted(DERIVATIONAL_SUFFIXES, key=len, reverse=True):

        if suffix in removed_set:
            continue

        if word.endswith(suffix):

            new_word = word[:-len(suffix)]

            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            return new_word, suffix

    # =========================
    # 2. FINAL VOWEL (STRICT CONTROL)
    # =========================
    if word.endswith(("a", "i", "e")):

        # do NOT remove vowel twice
        if any(v in removed_set for v in ["a", "i", "e"]):
            return word, None

        new_word = word[:-1]

        # protect short roots
        if len(new_word) < MIN_ROOT_LENGTH:
            return word, None

        # protect roots ending with vowel pattern (like "kimbi")
        if new_word.endswith(("bi", "ki", "li", "zi")):
            return word, None

        return new_word, word[-1]

    return word, None




    for suffix in sorted(DERIVATIONAL_SUFFIXES, key=len, reverse=True):

        # avoid removing same suffix twice
        if suffix in removed_set:
            continue

        if word.endswith(suffix):

            new_word = word[:-len(suffix)]

            # protect root length
            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            return new_word, suffix

    return word, None


# =========================
# MAIN FUNCTION
# =========================

def strip_suffixes(word):

    removed = []
    changed = True

    while changed:
        changed = False

        new_word, s = remove_suffix_once(word, removed)

        if s:
            word = new_word
            removed.append(s)
            changed = True

    return word, removed