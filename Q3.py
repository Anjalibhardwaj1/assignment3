def userdef_set(seq):
    unique = []
    [unique.append(e) for e in seq if e not in unique]
    return unique

if __name__ == "__main__":
    print(userdef_set([1, 2, 2, 2, 7, 8, 5, 2]))