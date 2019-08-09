#include <bits/stdc++.h>

using namespace std;

void diff(string s1, string s2) {
    for(int i = 0; i < s1.length(); ++i) {
        if(s1[i] != s2[i]) printf("*");
        else printf(".");
    }
}
int main() {
    string s1, s2;
    int n;
    cin >> n;
    while(n--) {
        cin >> s1;
        cin >> s2;
        cout << s1 << endl;
        cout << s2 << endl;
        diff(s1, s2);
        puts("");
    }
    return 0;
}
