#include <stdio.h>
#include <math.h>

int linear_search(int* arr, int l, int h, int element);

int jump_search(int* arr, int size, int element){
    int block_size = (int)sqrt((double)size);
    int start = 0;
    int end= block_size - 1;

    if(size == 0){
        return -1;
    }

    while (start < size) {
        if (element <= arr[end]) {
            return linear_search(arr, start, end, element);
        }

        start += block_size;
        end += block_size;
        if (end >= size) {
            end = size - 1;
        }
    }

    return -1;
}

int linear_search(int* arr, int l, int h, int element){
    for(int i = l; i <= h; i++){
        if(arr[i] == element){
            return i;
        }
    }
    return -1;
}