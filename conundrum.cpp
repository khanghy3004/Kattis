#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    int sum = 0;
    cin >> s;
    for(int i = 0; i < s.length(); ++i) {
        if (i%3 == 0 && s[i] != 'P') sum++;
        if (i%3 == 1 && s[i] != 'E') sum++;
        if (i%3 == 2 && s[i] != 'R') sum++;
    }
    cout << sum;
    return 0;
}
