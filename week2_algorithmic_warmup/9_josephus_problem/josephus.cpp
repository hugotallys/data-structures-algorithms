#include <iostream>

#define MAX_N 20

int v[MAX_N] = { 0 };

void print_v(int n) {
  for (int i = 0; i < n; i++) {
    std::cout << "|" << v[i] << "|";
  }
  std::cout << std::endl;
}

// Ad-hoc solution
int _josephus(int n, int k) {
	int current = 0;
	int total = 1;
	
  while (total <= n - 1) {
    
    print_v(n);

		for (int j = 0; j < k; j++) {
			current = (current + 1) % n;
      if (v[current]) {
				j -= 1;
			}
		}
    
    current -= 1;

    while(v[current]) {
      current = (current + 1) % n;
    }

    v[current] = 1;
    
    print_v(n);	
  
    while(v[current]) {
      current = (current + 1) % n;
    }
    total++;
	}

  for (int j = 0; j < n; j++) {
    if (v[j] == 0) {
      return j;
    }
  }

  return -1;
}


// Recursive solution (after noticing the ad-hoc table of results)
int josephus(int n, int k) {
  if (n == 1) {
    return 1;
  }
  return (( josephus(n-1, k) + k - 1 ) % n) + 1; 
}

int main() {
	int n, k;
	std::cout << "Enter parameters of josephus(n, k)" << std::endl;
	std::cin >> n >> k;
	std::cout << "josephus(" << n << "," << k << ")=" << josephus(n,k) << std::endl;
	return 0;
}
