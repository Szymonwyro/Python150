def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups


# can sort strings alphabetically
# create new group at each key
# append the words at each key group