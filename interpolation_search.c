#include <stdio.h>
#include <stdlib.h>

int interpolation_search(int* arr, int size, int element);

int main(int argc, char* argv[]){
    if (argc < 2) {
            printf("Usage: %s <element>\n", argv[0]);
            return 1;
    }
    int arr[] = {12, 13, 24, 25, 36, 44, 88, 122, 233, 322};
    int size = sizeof(arr)/sizeof(arr[0]);
    int element  = atoi(argv[1]);

    int br = interpolation_search(arr, size, element);
    printf("index = %d\n", br);
    return 0;
}

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
