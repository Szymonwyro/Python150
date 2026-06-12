def topKFrequent(elements, k):
    grouped = {}
    for i in elements:
        grouped[i] = grouped.get(i, 0) + 1
    sorted_items = sorted(grouped.items(), key = lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_items[:k]]

#slicing first k elements with [:k]
#using sorted(), then reversed = True for descending order
