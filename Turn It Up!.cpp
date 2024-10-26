#include <iostream>

using namespace std;

int main() {
    int n, vol = 7;
    string words;
    cin >> n;
    getchar();
    for (int i = 0; i < n; i++) {
        getline(cin, words);
        if (words == "Skru op!" && vol < 10) vol++;
        else if (words == "Skru ned!" && vol > 0) vol--;
    }
    cout << vol << endl;
    return 0;
}