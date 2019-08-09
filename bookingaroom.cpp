#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, r, a;
    bool b[105];
    bool check = false;
    cin >> n >> r;
    for(int i = 1; i <= r; ++i) {
        cin >> a;
        b[a] = true;
    }
    for(int i = 1; i <= n; ++i) {
        if(b[i] == false) {
            cout << i;
            check = true;
            return 0;
        }
    }
    if(!check) cout << "too late";
    return 0;
}


