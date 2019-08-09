#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, t, sum = 0;
    cin >> n;
    while(n--) {
        cin >> t;
        if(t < 0) ++sum;
    }
    cout << sum;
    return 0;
}
