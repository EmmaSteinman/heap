#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <cmath>
#include "heap.h"

using namespace std;

//====================================================
// Implements the insertion sort algorithm
// A is the array to be sorted
// length is the length of the array
//====================================================
void insertion_sort (int A[], int length)
{
	int j, temp;
		
	for (int i = 0; i < length; i++)
	{
		j = i;
		
		while (j > 0 && A[j] < A[j-1])
		{
			  temp = A[j];
			  A[j] = A[j-1];
			  A[j-1] = temp;
			  j--;
		}
	}
}

//====================================================
// merge function of the mergesort algorithm
//====================================================
void merge(int A[], int p, int q, int r)
{
    int a = q - p + 1;
    int b =  r - q;
    int L[a], R[b];
 
    for (int i = 0; i < a; i++)
        L[i] = A[p + i];
    for (int j = 0; j < b; j++)
        R[j] = A[q + j + 1];

    int i = 0;
    int j = 0;
    int k = p;
    while (i < a && j < b)
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < a)
    {
        A[k] = L[i];
        i++;
        k++;
    }
 
    while (j < b)
    {
        A[k] = R[j];
        j++;
        k++;
    }
}

//====================================================
// Implements the mergesort algorithm
// A is the list to be sorted
// in the first recurrence p = 0 and r = the size of
// the list
//====================================================
void merge_sort(int A[], int p, int r)
{
	if (p < r)
	{
		int q = floor((p+r)/2);
		merge_sort(A, p, q);
		merge_sort(A, q+1, r);
		merge(A, p, q, r);
	}
}

//====================================================
//
//====================================================
int partition (int A[], int  p, int r)
{
	int x = A[r];
	int i = p - 1;
	for (int j = p; j <= r-1; j++)
	{
		if (A[j] <= x)
		{
			i++;
			int k = A[i];
			A[i] = A[j];
			A[j] = k;
		}
	}
	int k = A[i+1];
	A[i+1] = A[r];
	A[r] = k;
	return i + 1;

}

void quick_sort (int A[], int p, int r)
{
	if (p < r)
	{
		int q = partition(A, p, r);
		quick_sort(A, p, q-1);
		quick_sort(A, q+1, r);
	}

}

//====================================================
// Uncomment a sorting algorithm to calculate the time
// it takes that algorithm to sort a list of size n.
//
// The time will be printed with a comma after so
// that it will be easy to copy into a python list 
// if printSortTime() is iterated.
//====================================================
void printSortTime ( int n )
{
	
	timeval timeBefore, timeAfter;
	long diffSeconds, diffUSeconds;
	
	int A[n];
	for(int i = 0; i < n; i++)
	{
		/*
		int k = (13 * i + 7) % 11;
		for(int j = i; j < (11*i + 23) % 17; j++)
		{			
			k = (73 * k + 892) % 3712;
		}
		*/
		A[i] = rand();
	}
		
	gettimeofday(&timeBefore, NULL);

	/*
	MinHeap<int> heap(A, n);
	
	gettimeofday(&timeBefore, NULL);
	
	heap.heapSort(A);
	*/

	insertion_sort(A, n);

	//merge_sort(A, 0, n);

	//quick_sort(A, 0, n);

	gettimeofday(&timeAfter, NULL);
	diffSeconds = timeAfter.tv_sec - timeBefore.tv_sec;
	diffUSeconds = timeAfter.tv_usec - timeBefore.tv_usec;
	
	//cout << diffSeconds + diffUSeconds / 1000000.0 << " seconds for a heap of size " << n << endl;
	
	cout << diffSeconds+diffUSeconds /1000000.0 << ",";
}

//====================================================
// main
//====================================================
int main ( void )
{
	
	for (int i = 1; i < 50000; i+=100) //for insertion sort run the loop "for(int i = 0; i < 50000; i+=100)"
	{
		printSortTime(i);
	}
	cout << endl;
	cout << "done" << endl;
	return 0;
}
