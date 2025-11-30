def first_non_repeating_character(s):
    for c in s:
        if s.count(c) == 1:
            return c

    return None

print(first_non_repeating_character("swiss"))