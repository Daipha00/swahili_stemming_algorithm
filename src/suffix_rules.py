# =========================
# SUFFIX LISTS (FROM YOUR DATA)
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
    "w"
]

FINAL_VOWELS = ["a", "e", "i"]

MIN_ROOT_LENGTH = 3


# =========================
# REMOVE DERIVATIONAL SUFFIX
# =========================

def remove_derivational_suffix(word, removed):

    for suffix in sorted(DERIVATIONAL_SUFFIXES, key=len, reverse=True):

        if suffix in removed:
            continue

        if word.endswith(suffix):

            new_word = word[:-len(suffix)]

            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            # protect real stems
            if new_word.endswith(("mb", "nd", "ng", "ch", "sh")):
                return new_word, suffix

            # prevent over-cutting like kimbi → kimb ❌
            if new_word.endswith(("bi", "li", "zi")):
                continue

            return new_word, suffix

    return word, None


# =========================
# REMOVE FINAL VOWEL (STRICT)
# =========================

def remove_final_vowel(word, removed):

    if word.endswith(tuple(FINAL_VOWELS)):

        # do not remove twice
        if any(v in removed for v in FINAL_VOWELS):
            return word, None

        new_word = word[:-1]

        if len(new_word) < MIN_ROOT_LENGTH:
            return word, None

        # 🔥 VERY IMPORTANT PROTECTION
        # do NOT break valid Swahili roots
        # if new_word.endswith(("bi", "li", "zi")):
        #     return word, None

        return new_word, word[-1]

    return word, None


# =========================
# MAIN FUNCTION
# =========================

def strip_suffixes(word):

    removed = []
    changed = True

    while changed:
        changed = False

        # 1️⃣ DERIVATIONAL FIRST
        new_word, s = remove_derivational_suffix(word, removed)

        if s:
            word = new_word
            removed.append(s)
            changed = True
            continue

        # 2️⃣ FINAL VOWEL LAST
        new_word, s = remove_final_vowel(word, removed)

        if s:
            word = new_word
            removed.append(s)
            changed = True

    return word, removed