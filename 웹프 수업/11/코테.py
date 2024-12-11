H, M, S = map(int,input().split())
timer = int(input())
S += timer
if S >= 60:
  T1 = S // 60
  M += T1
  S -= (T1 * 60)
if M >= 60:
  T2 = M // 60
  M -= (T2 * 60)
  H += T2
if H >= 24:
  H -= 24
print(H, M, S)