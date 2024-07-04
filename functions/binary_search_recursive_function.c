#include <stdio.h>
#include <stdlib.h>

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