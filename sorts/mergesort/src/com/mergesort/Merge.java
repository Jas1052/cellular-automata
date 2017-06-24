package com.mergesort;

import java.lang.*;


public class Merge {

   private static void mergeSort(int [] numbers, int left, int mid, int right){
       //sorts numbers in given indices
        int [] temp = new int[25];
        int i, left_end, num_elements, tmp_pos;

        left_end = (mid - 1);
        tmp_pos = left;
        num_elements = (right - left + 1);

        while ((left <= left_end) && (mid <= right)){
            if (numbers[left] <= numbers[mid])
                temp[tmp_pos++] = numbers[left++];
            else
                temp[tmp_pos++] = numbers[mid++];
        }

        while (left <= left_end)
            temp[tmp_pos++] = numbers[left++];

        while (mid <= right)
            temp[tmp_pos++] = numbers[mid++];

        for (i = 0; i < num_elements; i++){
            numbers[right] = temp[right];
            right--;
        }
    }

    // Recursive function that also calls merge

    private static void mergeRecurse(int [] numbers, int left, int right){
        int mid;
        if (right > left){
            mid = (right + left) / 2;
            //Splits into two groups to recurse
            mergeRecurse(numbers, left, mid);
            mergeRecurse(numbers, (mid + 1), right);

            //sorts the given section
            mergeSort(numbers, left, (mid+1), right);
        }
    }


    public static void main(String[] args){
        int[] numbers = { 3, 8, 8, 5, 2, 9, 6, 100 };
        int len = numbers.length;

        System.out.println("MergeSort By Recursive Method");

        mergeRecurse(numbers, 0, len - 1);

        for(int number : numbers) {
            System.out.println(number + " ");
        }
    }
}