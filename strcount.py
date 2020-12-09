vow = 'aeiouAEIOU'


def strcount(s):
    vowel = 0
    vowel_str = ""
    consonant = 0
    consonant_str = ""
    odd_ascii = 0
    odd_str = ""
    non_alpha = 0
    non_str = ""
    up_case = 0
    up_str = ""
    even_ascii = 0
    even_str = ""
    count = {}
    alpha_count = {}
    for i in s:
        if i.isalpha():
            if i in vow:
                vowel += 1
                if i not in vowel_str:
                    vowel_str += i

            else:
                consonant += 1
                if i not in consonant_str:
                    consonant_str += i
            if i in alpha_count.keys():
                alpha_count[i] += 1
            else:
                alpha_count[i] = 1
        else:
            non_alpha += 1
            if i not in non_str:
                non_str += i
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        if i.isupper():
            up_case += 1
            if i not in up_str:
                up_str += i
        if ord(i) % 2 == 1:
            odd_ascii += 1
            if i not in odd_str:
                odd_str += i
        else:
            even_ascii += 1
            if i not in even_str:
                even_str += i

    print("Number of Vowels:", vowel)
    print("vowels that are present:", vowel_str)
    print("Number of Consonants:", consonant)
    print("consonants that are present:", consonant_str)
    print("Number of Odd ASCII characters:", odd_ascii)
    print("odd ascii character that are present:", odd_str)
    print("Number of Even ASCII characters:", even_ascii)
    print("even ascii characters that are present:", even_str)
    print("Number of Non alphabet characters:", non_alpha)
    print("non alphabetical characters that are present:", non_str)
    print("Number of Uppercase characters:", up_case)
    print("upper case characters that are present:", up_str)
    i=0
    while i<3 and i<len(count) and i<len(alpha_count):
        print("Number of Character most repeated(Case insensitive):", max(count, key=count.get), max(list(count.values())), "times")
        print("Number of Alphabet most repeated(Case insensitive):", max(alpha_count, key=alpha_count.get),max(list(alpha_count.values())), "times")
        del count[max(count, key=count.get)]
        del alpha_count[max(alpha_count, key=alpha_count.get)]

strcount("Hello and Welcome to Datopic...$$$")
