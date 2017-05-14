//#include "header.h"
/*
  Do not remove the "header.h" file.
*/

//-----Include any additional required headers here-----
#include <iostream>
#include <vector>
using namespace std;
//-----End of additional headers-----

//-----Add new functions here(if any)-----
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(vector<int> &arr, vector<int> &weights, int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    /* create temp arrays */
    vector<int> L, R;
    vector<int> wL, wR;

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
    {
        L.push_back(arr[l + i]);
        wL.push_back(weights[l + i]);
    }
    for (j = 0; j < n2; j++)
    {
        R.push_back(arr[m + 1 + j]);
        wR.push_back(weights[m + 1 + j]);
    }

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (wL[i] > wR[j])
        {
            arr[k] = L[i];
            weights[k] = wL[i];
            i++;
        }
        else if (wL[i] == wR[j])
        {
            if (L[i] >= R[j])
            {
                arr[k] = L[i];
                weights[k] = wL[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                weights[k] = wR[j];
                j++;
            }
        }
        else
        {
            arr[k] = R[j];
            weights[k] = wR[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        weights[k] = wL[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        weights[k] = wR[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(vector<int> &arr, vector<int> &weights, int l, int r)
{
    if (l < r)
    {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, weights, l, m);
        mergeSort(arr, weights, m + 1, r);

        merge(arr, weights, l, m, r);
    }
}

//-----New functions end here-----

/* Question: You need to write the implementation of the given function.
             ( You may write any additional helper functions you want in the specified region only.
               Do not change the signature of the function already given)
               For detailed explanation of the question refer to the description part) 
*/

/*
   The function customSort takes a vector "num" of integers as an input along with the vector "weights" which contains the weights
   of the correponding integers. We wish to sort this vector "num" from the indices start to end based on the fact that numbers 
   with higher weights appear first and in case the weights are equal , we put the greater number first in the list. We check the 
   correctness of your function by calling your function with start index being equal to 0 and end being num.size()-1. Your aim is
   to complete the given function.
	
   We also wish efficient algorithms. We expect an O(n*log(n)) algorithm here instead of a O(n^2) one.
   (Hint : You can think this problem in lines of mergesort !!)

   For graded-test cases:

   The size of the vectors "num" and "weights" lies in the range 10000 to 100000.
   The entries of "num" and "weights" lie in the range 10 to 99.

   If your program takes too much time, you would get a timeout !! 
*/

/*
For example:
    num= {1, 4, 9, 6, 9}
    weights= {2, 9, 5, 9, 8}
    Expected Output = 6 4 9 9 1
*/

void customSort(vector<int> &num, vector<int> &weights, int start, int end)
{
    // Write your code here
    mergeSort(num, weights, start, end);
}

int main()
{
    vector<int> num = {1, 4, 9, 6, 9};
    vector<int> weights = {2, 9, 5, 9, 8};

    customSort(num, weights, 0, num.size() - 1);

    for (int i = 0; i < num.size(); i++)
    {
        cout << num[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < weights.size(); i++)
    {
        cout << weights[i] << " ";
    }
    cout << endl;
    return 0;
}