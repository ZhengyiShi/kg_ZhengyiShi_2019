# one-to-one character mapping
import sys


def check_mapping(str1, str2):
    # if length of two strings are different, then one-to-one mapping doesn't existed.
    if len(str1) != len(str2):
        return False
    
    # We can create a map using dict or list.
    # list costs less memory, but also costs more time with the increasing length of input string.
    # dict costs more memory, but are more efficient.
    map1 = {}
    for i in range(len(str1)):
        val = map1.get(str1[i], '0')
        if val == '0':
            map1[str1[i]] = str2[i]
        elif val != str2[i]:
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Wrong number of arguments")
    else:
        print(check_mapping(sys.argv[1], sys.argv[2]))

