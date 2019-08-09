#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, bats, sum = 0, cnt = 0;
    cin >> n;
    while(n--) {
        cin >> bats;
        if(bats >= 0) {
            ++cnt;
            sum += bats;
        }
    }
    cout << (double)sum/cnt;
    return 0;
}
