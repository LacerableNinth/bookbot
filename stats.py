def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    output = {}

    text = text.lower()

    for word in text.split():
        for char in word:
            if char not in output:
                output[char] = 0
            output[char] += 1

    return output

def sort_on(items):
    return items["num"]


def get_report(char_dict):
    output = []
    for char in char_dict:
        if char.isalpha():
            output.append({"char" : char , "num" : char_dict[char]})
    output.sort(reverse=True, key=sort_on)

    #print(f"\n\n{output}\n\n")
    return output

