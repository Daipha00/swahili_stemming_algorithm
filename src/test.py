from prefix_rules import strip_prefixes

print("Enter word (type 'exit' to quit):")

while True:
    word = input(">> ")

    if word.lower() == "exit":
        break

    stem, removed = strip_prefixes(word)

    print("Stem:", stem)
    print("Removed:", removed)
    print("------")