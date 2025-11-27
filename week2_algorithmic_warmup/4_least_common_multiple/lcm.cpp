#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long euclid(long a, long b) {

  if (a == b) return a;

  if (b > a) {
    int tmp = a;
    a = b;
    b = tmp;
  }

  if (b == 1) { return 1 };

  return euclid(a - b, b);
}

long long lcm(long a, long b) {
  return (a*b) / euclid(a, b);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
