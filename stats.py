def get_num_words(text):
    splitted_text = text.split()
    return f"Found {len(splitted_text)} total words"

def char_instance_counter(text):
    lowered_text = text.lower()
    dickie = dict()
    for char in lowered_text:
        if char in dickie:
            dickie[char] += 1
        elif char not in dickie:
            dickie[char] = 1
        else:
            raise Exception("oh no hermano")
    
    return dickie

def sort_on(items):
    return items["num"]

# returns a sorted list of dictionaries. Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
def sorted_dicts(text):
    dictionary = char_instance_counter(text)
    sorted_dicts_list = []
    for k,v in dictionary.items():
        # print(f"key:{k}, value: {v}")
        sorted_dicts_list.append({"char": k, "num": v})
    
    
    sorted_dicts_list.sort(reverse=True, key=sort_on)
    return sorted_dicts_list

