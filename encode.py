import random

def encode(string):
    output = [str(int(i) ** 3) if i.isdigit() else str(ord(i)) if i.isalpha() and i.islower() else str(
        random.randint(1, 5)) if i.isalpha() and i.isupper() else "-" for i in string]
    # output = [  else i for i in output]
    # output = [ else i for i in output]
    # output = ['-' if not i.isalnum() else i for i in output]
    # output=[]
    # for i in string:
    #     if i.isdigit():
    #         output.append(int(i) ** 3)
    #     elif i.isalpha() and i.islower():
    #         output.append(ord(i))
    #     elif i.isalpha() and i.isupper():
    #         output.append(random.randint(1, 6))
    #     else:
    #         output.append('-')
    # output = list(map(str, output))
    print(';'.join(output))


encode('Asd2#')
