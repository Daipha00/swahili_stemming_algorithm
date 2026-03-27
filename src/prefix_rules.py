from root_rules import protect_root
# =========================
# PREFIX LISTS
# =========================

NEGATION_PREFIXES = ["ha", "si", "hu"]

SUBJECT_PREFIXES = [
    "ni", "tu", "u", "a", "wa",
    "ki", "i", "li", "ya", "vi", "zi", "ja"
]

TENSE_PREFIXES = [
    "na", "me", "li", "ta",
    "ngeli", "ngali", "nge",
    "ka", "sha"
]

OBJECT_PREFIXES = [
    "ni", "ku", "m", "wa",
    "ki", "vi", "li", "ya", "ji", "zi"
]

RELATIVE_PREFIXES = [
    "cho", "po", "vyo", "ye",
    "ko", "lo", "zo", "yo"
]


# =========================
# CORE SETTINGS
# =========================

MIN_ROOT_LENGTH = 3


# =========================
# REMOVE ONE PREFIX
# =========================

def remove_prefix_once(word, prefixes, removed_set):

    for prefix in sorted(prefixes, key=len, reverse=True):

        if prefix in removed_set:
            continue

        if word.startswith(prefix):
            new_word = word[len(prefix):]

            # ROOT PROTECTION (length)
            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            # 🔥 NEW: STOP OVER-STRIPPING
            if len(removed_set) >= 3:
                continue

            return new_word, prefix

    return word, None

    from root_rules import protect_root  # import here (safe)

    for prefix in sorted(prefixes, key=len, reverse=True):

        # avoid removing same prefix twice
        if prefix in removed_set:
            continue

        if word.startswith(prefix):
            new_word = word[len(prefix):]

            # ROOT PROTECTION: do not destroy word
            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            if len(removed_set) >= 3:
               continue

            return new_word, prefix

    return word, None

    for prefix in sorted(prefixes, key=len, reverse=True):

        if prefix in removed_set:
            continue  # avoid duplicate removal

        if word.startswith(prefix):
            new_word = word[len(prefix):]

            # ROOT PROTECTION
            if len(new_word) < MIN_ROOT_LENGTH:
                continue

            # avoid removing prefixes that are actually part of root
            if new_word.startswith(("tu", "ji")) and len(new_word) <= 5:
                continue

            return new_word, prefix

    return word, None


# =========================
# MAIN FUNCTION
# =========================






def strip_prefixes(word):

    removed = []
    changed = True

    while changed:
        changed = False

        for group in [
            NEGATION_PREFIXES,
            SUBJECT_PREFIXES,   # ✅ subject first
            TENSE_PREFIXES,
            RELATIVE_PREFIXES,
            OBJECT_PREFIXES
        ]:
            new_word, p = remove_prefix_once(word, group, removed)

            if p:
                word = new_word
                removed.append(p)
                changed = True
                break  # restart after one removal

    return word, removed
  