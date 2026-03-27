from prefix_rules import strip_prefixes
from suffix_rules import strip_suffixes


print("Enter word (type 'exit' to quit):")

while True:
    word = input(">> ").strip()

    if word.lower() == "exit":
        break

    # STEP 1: PREFIX
    after_prefix, removed_prefix = strip_prefixes(word)

    # STEP 2: SUFFIX
    final_stem, removed_suffix = strip_suffixes(after_prefix)

    # STEP 3: MARKING
    if removed_prefix and removed_suffix:
        mark = "dsf-"
    elif removed_suffix:
        mark = "sdf-"
    else:
        mark = ""

    print("Stem:", mark + final_stem)
    print("Removed:", removed_prefix + removed_suffix)
    print("------")