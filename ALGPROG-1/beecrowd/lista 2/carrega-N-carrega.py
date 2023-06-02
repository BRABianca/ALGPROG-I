while True:
    try:
        a, b = map(int, input().split())
        res = (a + b) % (2**32)
        print(res)
    except EOFError:
        break