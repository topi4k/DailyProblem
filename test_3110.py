def simple_autocomplete(search, lst):
    n = len(search)
    sol = []
    for k in lst:
        if search == k[:n]:
            sol += [k]
    return sol


list_test = ['hello', 'hallo', 'echo', 'halloween']
search_term = 'ha'
print(simple_autocomplete(search_term, list_test))




