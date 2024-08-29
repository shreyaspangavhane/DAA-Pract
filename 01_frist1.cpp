#include <iostream>
using namespace std;

int main() {
    int n, key = 0, count = 0;

    cout << "Enter the array size: ";
    cin >> n;

    int a[n];

    cout << "Enter array elements (1/0): ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            key=i;
            key++;
            if (key == 1) {
                cout << "Wrong Input...." << endl;
            }
            count++;
        }
    }

    cout << "The number of zeros is: " << count << endl;

    return 0;
}
