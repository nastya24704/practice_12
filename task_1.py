def spaces(text):
    max_count = 0
    count = 0
    for ch in text:
        if ch == " ":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count
