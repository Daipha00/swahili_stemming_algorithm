import re

NEGATION = ["ha", "si", "hu"]

SUBJECT = ["ni", "u", "a", "tu", "wa", "m"]

TENSE = ["na", "me", "li", "ta", "ka", "nge", "ngeli", "ngali", "sha"]

OBJECT = ["ni", "ku", "m", "wa", "tu", "ki", "vi", "li", "ya", "ji"]

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


if __name__ == "__main__":
    test_words = [
        "nimewapikia",
        "tutampiga",
        "atanipigia",
        "walimpiga"
    ]

    for w in test_words:
        step1 = remove_prefixes(w)
        step2 = remove_object(step1)

        print(w, "→", step2)