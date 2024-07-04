#include <stdio.h>

int interpolation_search(int* arr, int size, int element) {
    int start = 0;
    int end = size - 1;

    if (start == end && arr[start] == element){
        return start;
    }

    while(start< end) {
        if(arr[start] == arr[end]){
            if(arr[start] == element){
                return start;
            }
            else{
                return -1;
            }
        }
        int pos = (int)(start+ ((double)(element - arr[start])/(arr[end] - arr[start]))*(end - start));
        if(arr[pos] == element) {
            return pos;
        } else if(arr[pos] < element) {
            start = pos + 1;
        } else if(arr[pos] > element) {
            end = pos - 1;
        }
    }
    return -1;
}
