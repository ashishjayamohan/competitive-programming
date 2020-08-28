#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  int x[n];
  for(int i = 0; i < n; i++) {
    cin >> x[i];
  }
  int ans = 0;
  for(int i = 0; i < n; i++) {
    if(x[i] != x[i + 1]) {
      ans++;
    }
  }
  cout << ans;
}
