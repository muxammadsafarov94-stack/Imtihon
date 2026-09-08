def count_vowels_and_consonants(s):
    unlilar = set("aeiouAEIOU")
    unli_soni = 0
    undosh_soni = 0

    for belgi in s:
        if belgi.isalpha():
            if belgi in unlilar:
                unli_soni += 1
            else:
                undosh_soni += 1

    return {"unli": unli_soni, "undosh": undosh_soni}


print(count_vowels_and_consonants("Salom Dunyo!"))