#include <bits/stdc++.h>

using namespace std;

int main() {
    int a[4][4];
    cin >> a[0][0] >> a[1][0] >> a[0][1] >> a[1][1] >> a[0][2] >> a[1][2];
    for (int i = 0; i < 2; i++){
        int first = a[i][0];
        if (a[i][1] == first)
            cout << a[i][2] << " ";
        else if (a[i][2] == first){
            cout << a[i][1] << " ";
        }
        else cout << first << " ";
    }
    return 0;
}
