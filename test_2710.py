def recursive_count(nb):
    string_nb = str(nb)
    if len(string_nb) == 1:
        return 1
    else:
        if string_nb[0] == '1' and string_nb[1] != '0':
            if len(string_nb) > 2:
                return recursive_count(int(string_nb[1:])) + recursive_count(int(string_nb[2:]))
            else:
                return 2
        elif string_nb[0] == '2' and string_nb[1] in ['1', '2', '3', '4', '5', '6']:
            if len(string_nb) > 2:
                return recursive_count(int(string_nb[1:])) + recursive_count(int(string_nb[2:]))
            else:
                return 2
        elif string_nb[1] == '0':
            return recursive_count(int(string_nb[2:]))
        else:
            return recursive_count(int(string_nb[1:]))


assert(recursive_count(9) == 1)
assert(recursive_count(12) == 2)
assert(recursive_count(111) == 3)

print(recursive_count(17261))
