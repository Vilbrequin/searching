#include <stdio.h>
#include <stdlib.h>

int binary_search(int* arr, int low, int high, int element);

int main(int argc, char** argv){
    if (argc < 2) {
        printf("Usage: %s <element>\n", argv[0]);
        return 1;
    }
    
    int arr[] = {12, 13, 24, 25, 36, 44};
    int low = 0;
    int high = (sizeof(arr)/sizeof(arr[0])) - 1;
    int element  = atoi(argv[1]);

    int br = binary_search(arr, low, high, element);
    printf("%d\n", br);

    return 0;
}

int binary_search(int* arr, int low, int high, int element) {
    if(low > high){
        return -1;
    }

    int mid = (high + low)/2;

    if (arr[mid] == element){
        return mid;
    }
    else {
        if(arr[mid] < element){
            low = mid + 1;
            binary_search(arr, low, high, element);
        }
        else {
            high = mid - 1;
            binary_search(arr, low, high, element);
        }
    }
}