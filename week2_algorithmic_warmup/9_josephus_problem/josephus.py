def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n-1,k) + k) % n


n = input("Enter the value of n:\n")
k = input("Enter the value of k:\n")

n, k = int(n), int(k)

print(f"josephus({n},{k}) = {josephus(n,k)}")
