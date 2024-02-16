def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #print(count_words(text))
    #print(count_characters(text))
    print_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
def print_report(text):
    print(count_words(text), " words found in the document\n\n")

    chars = count_characters(text)
    sorted_chars_values = sorted(chars.items(), key = lambda x:x[1], reverse=True)
    chars_sorted = dict(sorted_chars_values)
    for c in chars_sorted:
        if c.isalpha():
            print(f"The {c} character was found {chars_sorted[c]} times")
    print("--- End report ---")

main()