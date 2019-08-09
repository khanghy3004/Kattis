#include <bits/stdc++.h>

using namespace std;

int main() {
    int l, x, p, sum = 0, cnt = 0;
    string event;
    cin >> l >> x;

    while(x--) {
        cin >> event >> p;
        if(event == "enter") sum += p;
        if(event == "leave") sum -= p;
        if(sum > l) {
            sum -= p;
            ++cnt;
        }
    }
    cout << cnt;
    return 0;
}
