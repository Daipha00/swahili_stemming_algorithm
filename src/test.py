from prefix_rules import strip_prefixes
from suffix_rules import strip_suffixes

print("Enter word (type 'exit' to quit):")

while True:
    word = input(">> ")

    if word.lower() == "exit":
        break

    # STEP 1: PREFIX REMOVAL
    word_after_prefix, removed_prefixes = strip_prefixes(word)

    # STEP 2: SUFFIX REMOVAL
    final_stem, removed_suffixes = strip_suffixes(word_after_prefix)

    # COMBINE REMOVED
    all_removed = removed_prefixes + removed_suffixes

    # STEP 3: MARKING SYSTEM
    if removed_prefixes and removed_suffixes:
        mark = "dsf-"   # prefix + suffix removed
    elif removed_suffixes:
        mark = "sdf-"   # suffix only
    else:
        mark = ""       # no suffix removed

    print("Stem:", mark + final_stem)
    print("Removed:", all_removed)
    print("------")