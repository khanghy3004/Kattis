#include <bits/stdc++.h>

using namespace std;

int main() {
    double c, a, b, sum = 0;
    int t;
    cin >> c >> t;
    while(t--) {
        cin >> a >> b;
        sum += a*b*c;
    }
    printf("%.7f", sum);
    return 0;
}
