# =========================
# ROOT PROTECTION RULES
# =========================

MIN_ROOT_LENGTH = 3


def protect_root(word, removed_prefixes):
    """
    Prevent over-stripping when root begins.

    Example:
    kimbilia → DO NOT remove 'ki' if it's part of root
    """

    # If word is already short → stop
    if len(word) <= 4:
        return True

    # 🔥 Detect possible root start patterns
    # Swahili roots often start with consonant clusters
    if word.startswith(("ki", "tu", "ji")):
        # if too short → probably root
        if len(word) <= 6:
            return True

    return False