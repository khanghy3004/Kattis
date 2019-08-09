#include <bits/stdc++.h>

using namespace std;

int main() {
    int day, month;
    string days[] = {"Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"};
    int months[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    cin >> day >> month;
    for (int i = 0; i < month - 1; i++) {
        day += months[i];
    }
    cout << days[day % 7];

    return 0;
}

