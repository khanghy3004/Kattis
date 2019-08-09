#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n;
    string s;
    string str[105];

    cin >> t;
    while(t--) {
        int cnt = 0;
        cin >> n;
        for(int i = 0; i < n; ++i) {
            cin >> s;
            str[i] = s;
        }
        sort(str, str+n);
        for(int i = 0; i < n; ++i) {
            if(str[i] != str[i+1]) ++cnt;
        }
        cout << cnt <<endl;
    }
    return 0;
}
