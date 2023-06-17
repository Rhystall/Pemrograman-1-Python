def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword '{keyword}' has been found at index {i}")
            return i
    print(f"Keyword '{keyword}' has not been found")
    return -1

data = [23, 3, 4, 10, 32]
keyword = input("Input Keyword: ")
linear_search(keyword, data)
