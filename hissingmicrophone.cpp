#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    int cnt = 0;
    cin >> s;
    int len = s.length();
    for(int i = 0; i < len; ++i) {
        if(s[i] == 's' && s[i+1] == 's') ++cnt;
    }
    if(cnt > 0) cout << "hiss"; else cout << "no hiss";

    return 0;
}

