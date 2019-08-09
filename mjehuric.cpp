#include <bits/stdc++.h>

using namespace std;

int main() {
    int a[5];
    for(int i = 0; i < 5; ++i) {
        cin >> a[i];
        b[i] = a[i];
    }
    for(int i = 0; i < 5; ++i) {
        if(a[i] > a[i+1]) swap(a[i], a[i+1]);
        for(int k = 0; k < 5; ++k) cout << a[k] << " ";
        puts("");
    }
}

