def palindromic(ar):
    """
    type ar: string
    return type: int
    """
    size = len(ar)
    if size <= 1:
        return size
    p = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        p[i][i] = 1
    for i in range(size - 1):
        for j in range(i + 1, size):
            if ar[i] == ar[j]:
                p[i][j] = 2 + p[i + 1][j - 1]
            else:
                p[i][j] = max(p[i + 1][j], p[i][j - 1])
    return p[0][size - 1]
def longest_palindromic(ar):
    """
    type ar: string
    return type : string
    """
    size = len(ar)
    if size <= 1:
        return ar
    p = [["" for i in range(size)] for i in range(size)]
    for i in range(size):
        p[i][i] = p[i][i] + ar[i]
    for i in range(size - 1):
        for j in range(i + 1, size):
            if ar[i] == ar[j]:
                p[i][j] = ar[i] + p[i + 1][j - 1] + ar[j]
            else:
                if len(p[i + 1][j]) < len(p[i][j - 1]):
                    p[i][j] = p[i][j - 1]
                else:
                    p[i][j] = p[i + 1][j]
    return p[0][size - 1]
