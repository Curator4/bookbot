def count_words(content):
    list_of_words = content.split()
    return len(list_of_words)
def count_characters(content):
    character_count = {}
    for character in content:
        if character.lower() not in character_count:
            character_count[character.lower()] = 1
        else:
            character_count[character.lower()] += 1
    return character_count
def sort_on(dict):
    return dict["count"]
def sort_dictionaries(character_dictionary):
    dictionary_list = []
    for character in character_dictionary:
        new_dict = {
            "character": character,
            "count": character_dictionary[character]
        }
        dictionary_list.append(new_dict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
        