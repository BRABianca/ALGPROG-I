N, L, D = map(int, input().split())
LTotal = (D * N) // (L * 1000) * L

if (D * N) % (L * 1000) > 0:
    LTotal += L

print(int(LTotal))