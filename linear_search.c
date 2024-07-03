#include <stdio.h>
#include <stdlib.h>

int linear_search(int* arr, int size, int element);

int main(int argc, char** argv){
    if (argc < 2) {
        printf("Usage: %s <element>\n", argv[0]);
        return 1;
    }
    
    int arr[] = {12, 22, 34, 2, 33};
    int size = sizeof(arr)/sizeof(arr[0]);
    int element = atoi(argv[1]);
    int index = linear_search(arr, size, element);

    printf("%d\n", index);

    return 0;
}

int linear_search(int* arr, int size, int element){
    int i = 0;
    while(arr[i] != element){
        i++;
    }
    if (i < size) {
        return i;
    }
    else {
        return -1;
    }
}