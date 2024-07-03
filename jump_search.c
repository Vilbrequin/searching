#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int jump_search(int* arr, int size, int element);
int compare(int* arr, int l, int h, int element);
int main(int argc, char* argv[]){
    if (argc < 2) {
        printf("Usage: %s <element>\n", argv[0]);
        return 1;
    }
    int arr[] = {12, 13, 24, 25, 36, 44, 88, 122, 233, 322};
    int size = sizeof(arr)/sizeof(arr[0]);
    int element  = atoi(argv[1]);

    int br = jump_search(arr, size, element);
    printf("index = %d\n", br);
    return 0;
}

int jump_search(int* arr, int size, int element){
    int bloc_size = (int)sqrt((double)size);
    printf("bl_size = %d\n", bloc_size);
    int l = 0;
    int h = bloc_size - 1;

    while(h < size){
        printf("arr[h] = %d\n", arr[h]);
        if(arr[h] < element){
            printf("1\n");
            l += bloc_size;
            h += bloc_size;
            if(h >= size){
                h = size - 1;
            }
        }
        else if(arr[l] <= element && element < arr[h]){
            printf("2\n");
            return compare(arr, l, h, element);
        }
        else if (arr[h] == element) {
            return h;
        }
    }
}

int compare(int* arr, int l, int h, int element){
    for(int i = l; i < h; i++){
        if(arr[i] == element){
            return i;
        }
    }
    return -1;
}