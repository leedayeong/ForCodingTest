n, k = map(int, input().split())
cnt = 0

while(n!=1):
  # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k) * k
  cnt += (n - target)
  n = target
  if n<k: break
  cnt += 1
  n //= k

cnt += (n-1)

print(cnt)