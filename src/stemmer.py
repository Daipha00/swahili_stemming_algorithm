import re

NEGATION = ["ha", "si", "hu"]

SUBJECT = ["ni", "u", "a", "tu", "wa", "m"]

TENSE = ["na", "me", "li", "ta", "ka", "nge", "ngeli", "ngali", "sha"]

RELATIVE = ["po", "ko", "mo", "cho", "vyo", "yo", "lo", "zo", "ye"]

OBJECT = ["ni", "ku", "m", "wa", "tu", "ki", "vi", "li", "ya", "ji"]

SUFFIXES = [
    "ish", "esh",
    "iw", "ew", "ea",
    "ik", "ek",
    "il", "ul","ia",
    "an",
    "w"
]

def remove_prefixes(word):
    original_word = word

    # Combine all prefixes
    prefixes = NEGATION + SUBJECT + TENSE

    # Sort by length (longest first)
    prefixes = sorted(prefixes, key=len, reverse=True)

    changed = True

    while changed:
        changed = False
        for prefix in prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]
                changed = True
                break  # restart loop after removing one prefix

    return word



def remove_object(word):
    objects = sorted(OBJECT, key=len, reverse=True)

    # Object lazima iwe karibu mwanzo (after prefix)
    for obj in objects:
        if word.startswith(obj):
            candidate = word[len(obj):]

            # Linda stem (isiwe fupi sana)
            if len(candidate) >= 3:
                return candidate

    return word

def remove_suffixes(word):
    suffixes = sorted(SUFFIXES, key=len, reverse=True)

    changed = True

    while changed:
        changed = False

        for suf in suffixes:
            if word.endswith(suf):
                candidate = word[:-len(suf)]

                if len(candidate) >= 3:
                    word = candidate
                    changed = True
                    break

    # 🔥 clean trailing vowels (extra safety)
    while len(word) > 3 and word[-1] in ["a", "e", "i"]:
        word = word[:-1]

    return word

def remove_final_vowel(word):
    if len(word) > 3 and word[-1] in ["a", "e", "i"]:
        return word[:-1]
    return word

def remove_relative(word):
    relatives = sorted(RELATIVE, key=len, reverse=True)

    for rel in relatives:
        if word.startswith(rel):
            candidate = word[len(rel):]
            if len(candidate) >= 3:
                return candidate

    return word


if __name__ == "__main__":
    test_words = [
        "nimewapikia",
        "atanipigia",
        "tendesheana",
        "walipotendeana"
    ]

for w in test_words:
    step1 = remove_prefixes(w)
    step2 = remove_relative(step1)   # 🔥 NEW
    step3 = remove_object(step2)
    step4 = remove_final_vowel(step3)
    step5 = remove_suffixes(step4)

    print(w, "→", step5)