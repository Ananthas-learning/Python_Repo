# test_dict = {"Queen": "Bohemian Rhapsody",
#              "Bee Gees": "Stayin Alive",
#              "U2": "One",
#              "Michael Jackson": "Billie Jean",
#              "The Beatles": "Hey Jude",
#              "Bob Dylan": "Like A Rolling Stone"}
# test_dict_len = len(test_dict)
# print(test_dict_len)
# print(list(test_dict.keys()))
# print(test_dict.values())
# print(test_dict.items())
# for key in test_dict:
#     print(key)
# for key, value in test_dict.items():
#     print(key, value)
# print(test_dict.get("U1", "The key does not exist"))

# test_dict2 = {}.fromkeys("bcdefghij","consonant")
# print(list(test_dict2.items()))
# for key, value in test_dict2.items():
#     print(key,value)
# test_dict3 = fast_food_items = {"McDonald's": "Big Mac",
#                                 "Burger King": "Whopper",
#                                 "Chick-fil-A": "Original Chicken Sandwich"}
# popped = test_dict3.pop("McDonald's")
# print(popped)
# food_items = test_dict3.popitem()
# print(food_items)
# print(test_dict3)

internet_celebrities = {"DrDisrespect": "YouTube",
                        "ZLaner": "Facebook",
                        "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)
internet_celeb_copy = internet_celebrities.copy()
print(internet_celeb_copy)
internet_celebrities.clear()
print(internet_celebrities)
