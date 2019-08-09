#include <bits/stdc++.h>

using namespace std;

int main() {
    int white = 0, lower = 0, upper = 0, symbol = 0;
    string s;

    cin >> s;
    int len = s.length();
    for(int i = 0; i < len; ++i) {
        if(s[i] == '_') {
            white++;
        }else if(islower(s[i])) {
            lower++;
        }else if(isupper(s[i])) {
            upper++;
        }else {
            symbol++;
        }
    }
    cout << (double)white/len << endl;
    cout << (double)lower/len << endl;
    cout << (double)upper/len << endl;
    cout << (double)symbol/len << endl;
    return 0;
}

