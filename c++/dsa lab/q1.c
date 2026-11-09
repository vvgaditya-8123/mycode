#include <iostream>
using namespace std;

// Function for iterative linear search
int linearSearch(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            return i;
        }
    }

    return -1;
}

// Main function
int main()
{
    int n, key;

    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter the array elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Enter the element to search: ";
    cin >> key;

    int result = linearSearch(arr, n, key);

    if (result != -1)
    {
        cout << "Element found at position: " << result + 1 << endl;
    }
    else
    {
        cout << "Element not found." << endl;
    }

    return 0;
}