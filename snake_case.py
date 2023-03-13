def to_snake_case(words):
    return words.replace(" ", "_")


words = input("Enter words: ")
snake_cased_words = to_snake_case(words.strip())
print("Result: ", snake_cased_words)
