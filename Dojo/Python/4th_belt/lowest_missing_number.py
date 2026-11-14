N = int(input())
arr = list(map(int, input().split()))

i = 0
while i < N:
    correct_idx = arr[i] - 1
    if 1 <= arr[i] <= N and arr[i] != arr[correct_idx]:
        arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
    else:
        i += 1

ans = N + 1
for i in range(N):
    if arr[i] != i + 1:
        ans = i + 1
        break

print(ans)
