#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, b;
    double p, temp, bpm;
    cin >> n;
    while(n--) {
        cin >> b >> p;
        temp = 60/p;
        bpm = 60*b/p;
        printf("%.4f %.4f %.4f\n", bpm-temp, bpm, bpm+temp);
    }
    return 0;
}


