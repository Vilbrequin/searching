#include <stdio.h>
#include <stdlib.h>

int binary_search(int* arr, int size, int element){
    int l = 0;
    int h = size - 1;

    while(l <= h){
        int mid = (h+l)/2;
        if(arr[mid] == element){
            return mid;
        }
        else if(arr[mid] < element){
            l = mid + 1;
        }
        else {
            h = mid - 1;
        }
    }
    return -1;
}