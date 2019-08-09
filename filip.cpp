#include <bits/stdc++.h>

using namespace std;
int rev(int n) {
    int ans = 0;
    while(n!=0) {
        int rem = n%10;
        ans = ans*10+rem;
        n/=10;
    }
    return ans;
}
int main() {
    int x, y;

    cin >> x >> y;
    if(rev(x) > rev(y)) cout << rev(x);
    else cout << rev(y);

    return 0;
}

