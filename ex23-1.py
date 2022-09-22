import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file#.readline()

    if line:
        print_line(line, encoding, errors)
#        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors)

    print(cooked_string, "<======>", raw_bytes)

#languages = open("languages-1.txt", encoding="utf-8")
languages = b'\xd9\xbe\xd9\x86\xd8\xac\xd8\xa7\xd8\xa8\xdb\x8c'

main(languages, input_encoding, error)
