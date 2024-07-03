#include <stdio.h>
#include <stdlib.h>

int binary_search(int* arr, int size, int element);

int main(int argc, char* argv[]){

    if (argc < 2) {
        printf("Usage: %s <element>\n", argv[0]);
        return 1;
    }
    int arr[] = {12, 13, 24, 25, 36, 44};
    int size = sizeof(arr)/sizeof(arr[0]);
    int element  = atoi(argv[1]);

    int br = binary_search(arr, size, element);
    printf("%d\n", br);

    return 0;
}

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