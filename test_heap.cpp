#include <iostream>
#include <cassert>
#include "heap.h"

using namespace std;

void test_constructor()
{
	MinHeap<int> heap(0);
	string str = heap.toString();
	assert(str == "[ ]");
}

void test_array_constructor()
{
	int a[5] = {1,2,3,4,5};
	MinHeap<int> heap(a, 5);
	string str = heap.toString();
	assert(str == "[1, 2, 3, 4, 5 | ]");
}
void test_copy_constructor()
{
	int a[5] = {1,2,3,4,5};
	MinHeap<int> heap(a, 5);
	MinHeap<int> heap2(heap);
	string str = heap2.toString();
	assert(str == "[1, 2, 3, 4, 5 | ]");
}
void test_heapSort()
{
	int a[5] = {3, 2, 4, 1, 5};
	MinHeap<int> heap(a, 5);
	int b[5];
	heap.heapSort(b);
	MinHeap<int> heap2(b, 5);
	string str = heap2.toString();
	assert(str == "[1, 2, 3, 4, 5 | ]");
}
void test_assignment()
{
	int a[6] = {1,2,3,4,5,6};
	MinHeap<int> heap(a, 6);
	MinHeap<int> heap2 = heap;
	string str = heap2.toString();
	assert(str == "[1, 2, 3, 4, 5, 6 | ]");
}

void test_heapify()
{
	int a[3] = {3,1,2};
	MinHeap<int> heap(a, 3);
	heap.heapify(0);
	string str = heap.toString();
	assert(str == "[1, 3, 2 | ]");
}
/*
void test_buildHeap()
{
	int a[5] = {2,1,4,5,3};
	MinHeap<int> heap(a,5);
	heap.buildHeap();
	string str = heap.toString();
	cout << str << endl;
}
*/
void test_swap()
{
	int a[7] = {1, 2, 3, 4, 5, 6, 7};
	MinHeap<int> heap(a, 7);
	heap.swap(0, 1);
	string str = heap.toString();
	assert(str == "[2, 1, 3, 4, 5, 6, 7 | ]");
}


int main ( void )
{
	test_constructor();
	test_array_constructor();
	test_copy_constructor();
	test_heapSort();
	test_assignment();
	test_heapify();
	//test_buildHeap();
	test_swap();
	
}
