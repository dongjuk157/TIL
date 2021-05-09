[toc]

# SWEA Programming Intermediate

Python 및 C 사용

## List 1

### 01 알고리즘

슈도코드(Pseudo Code), 순서도

시간복잡도(Big-O Notation)



### 02 배열 List

리스트의 개념과 필요성: 한번의 선언으로 여러 변수를 사용할수있음

1차원 배열 생성 및 활용

```python
arr = list() # arr = []
```

```C
int arr[4];
```



### 03 Exhaustive Search

완전 검색의 개념: 모든 경우의 수를 나열해보고 확인하는 기법

Brute-Force/ Generate-and-test

수행속도는 느리지만 해답은 찾을수 있음.

ex) 부분 집합 구하기



### 04 Greedy Algorithm

탐욕 알고리즘: 최적해를 구하는데 사용되는 방법

결정 순간마다 최적이라고 생각하는 것을 선택해 최종적인 답을 찾는 방식

부분마다 최적일순 있으나 최종 답까지 최적은 아님.(해답을 못찾을수도 있음)

동작과정: 해 선택 -> 실행 가능성 검사 -> 해 검사

1. 해 선택: 현재 상태에서 부분 문제의 최적해를 구한뒤 부분해 집합에 추가
2. 실행 가능성 검사: 새로운 부분해 집합이 실행가능한지 확인. 문제의 제약조건을 위반하지 않는지 검사
3. 해 검사: 부분해 집합이 문제의 해가 되는지 확인

ex) 거스름돈 구하기, babygin



### 05 Sort

정렬: 기준을 잡아 값을 순서대로 배열하는것

종류: 버블, 카운팅, 선택, 퀵, 삽입, 병합 등

#### 1) 버블 정렬 O(n^2)

인접한 두개의 원소를 비교하며 자리를 교환하는 방식

```python
def bubble(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
```

```C
void BubbleSort(a[], n){ // a: list, n: size
    for(int i=n-1; i>0; i--){
        for(int j=0; j<i; j++){
            if(a[j]>a[j+1]){
                tmp = a[j];
                a[j] = a[i];
                a[i] = tmp;
            }
        }
    }
}
```



#### 2) 카운팅 정렬 O(n + k)

선형 시간에 정렬가능한 알고리즘

항목이 몇개씩 있는지 세는 작업을 사용하여 정렬.

정수나 정수로 표현할수 있는 자료에 대해서 적용가능(발생 회수를 기록해야함)

카운트를 위한 공간을 할당하려면 가장 큰 정수를 알아야함.=> k: 정수의 최대값

정렬하는 배열의 카운팅하는 정수의 크기가 작을때 사용(범위가 작을때도 사용가능할 듯)



```python
# arr: 정렬할 배열, n: 배열의 크기, k: 배열의 최대값
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
def countingSort(arr, n, k):
    sorted_arr = [0] * n
    # 1 카운팅
    count = [0] * (k + 1) 
    for i in range(len(a)):
        count[a[i]] += 1
    # 2 카운팅 누적 합 
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 3 정렬
    for i in range(len(a)-1, -1, -1):
        sorted_arr[count[a[i]]] = a[i]
        count[a[i]] -= 1
    return sorted_arr
```

```C
void CountingSort(arr[], int n, int k){
    int sorted_arr[n];
    int count[k+1];
    for(int i=0; i<n; i++)
        count[a[i]] += 1;
    for(int i=1; i<=k;i++)
    	count[i] += count[i - 1];
    for(int i=n-1;i>0;i--){
        sorted_arr[count[a[i]]] = a[i];
        count[a[i]] -= 1;
    }
    return sorted_arr;
}
```



## List 2

### 01 이차원 배열 생성

```python
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# 행렬 중첩 가능
```

```c
int arr[2][4] = {{0,1,2,3},{4,5,6,7}};
// arr[행][열]
```



### 02 이차원 배열의 순회 

행우선, 열우선, 지그재그 등등

델타 탐색

전치행렬



### 03 부분집합 알고리즘

반복문, 재귀, 비트연산

```C
#include <stdio.h>
void main(void){
    int i, j;
    int arr[] = {3,6,7,1,5,4};
    int n = sizeof(arr)/sizeof(arr[0]); 
    
    for (int i=0; i<(1<<n); i++){
        for (int j=0; j< n; j++){
            if i & (1<<j){
                print("%d, ", arr[j]);
            }
        }
        print("\n");
    }
}
```



### 04 순차검색

검색의 종류: 순차검색, 이진검색, 해쉬

#### 순차검색

간단하고 직관적인 방법, 배열이나 연결리스트 등의 순차 구조로 구현된 자료구조에서 유용함

구현은 쉽지만 수행시간이 오래걸림. O(n)

정렬이 되어있는 경우: 첫번째 원소부터 탐색하되 찾는 값보다 큰(작은) 경우 탐색 종료

정렬이 되어있지 않은 경우:  첫번째 원소부터 마지막 원소까지 찾는 값(키)과 같은 원소가 있는지 비교

```C
// 정렬 되어있는 경우
int sequentialSearch(int *a, int n, int key){
    for (int i=0; i<n; i++){
        if (a[i]==key) //탐색 성공
            return i;
        if (a[i]> key) // 탐색 실패
            break;
    }
    return -1;
}
```



#### 이진검색

자료 가운데에 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정

동작 과정:

1. 자료 중앙에 있는 원소 선택.
2. 중앙 원소값과 찾는 목표값 비교
3. 목표값이 원소값보다 작으면 중앙원소값의 왼쪽, 크면 오른쪽에 대해서 새로 검색

```python
# 재귀함수
def binarySearch(a, s, e, key):
    if s > e:
        return -1
    else:
        m = (s + e) // 2
        if key == a[m]:
            return m
        elif key < a[m]:
            return binary(a, s, m-1, key)
        else:  # key > a[m]
            return binary(a, m+1, e, key)
```

```C
int binarySearch(int a*, int n, int key){
    int s, e, m;
    s = 0;
    e = n - 1; 
    while (s <= e){
        m = (s + e) / 2;
        if (m==key)
            return m;
        else if (m < key)
            s = m + 1; 
        else
            e = m - 1; 
    }
    return -1;
}
```



### 05 선택 정렬

순차검색을 사용한 정렬

동작 과정:

1. 정렬 알고리즘을 이용하여 자료 정렬
2. 원하는 순서에 있는 원소 가져오기

```python
def selectionSort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
```

```C
void SelectionSort(int *a, int size){
    int i, j, t, min_ind, tmp;
    for(i=0; i<size-2;i++){
        min = i;
        for(j=i+1; j<size-1;j++){
            if (a[j]<a[min])
                min = j;
        }
        tmp = a[i];
        a[i] = a[min];
        a[min] = tmp;
    }
}
```



## String 문자열

ASCII Code 

```python
# python
string = 'ABC'
```

```c
// C
char string[] = "ABC"; // char string[] ={'a','b','c','/0'}
char *name = 'Ko';
```

### 01 문자열 처리

문자열 복사, 뒤집기(역 순회), 문자열 비교(C: `strcmp()`, python: `str1 == str2`)

문자열 정수변환(C: ascii로 저장되어있음, `%d`, `%c`로 사용, python: `ord`, `chr`)

### 02 패턴매칭

#### 01 고지식한 패턴검색 알고리즘(Brute-Force) O(MN)

일일이 비교하는 방식. 



#### 02 KMP알고리즘 O(M+N)

패턴을 전처리하여 불일치가 발생한 부분에 대해 비교를 최소화함

매칭이 실패한 상황에서 돌아갈곳을 계산 -> 실패하기직전까지는 성공했다는 것을 사용함

pattern에 대하여 접두사(prefix)와 접미사(suffix)가 같아질수 있는 것 중에서 가장 긴 것의 길이를 구함


```python
# string = 'abcdabcdabcdabcdabcef'
# pattern = 'abcdabcef'

def maketable(p, table):
    i = 1 # always table[0]==0
    j = 0
    while i < len(p)
    	if p[i] == p[j]: # 비교했을 때 같은 패턴이 있는 경우
            j += 1
            table[i] = j
            i += 1
       	else:            # p[i] != p[j]
            if j != 0:   
                j = table[j - 1]
            else:        # j == 0
                table[i] = 0 # 0으로 초기화했으니 굳이 필요없음
                i += 1   # 다음 문자열 확인
    # table = [0, 0, 0, 0, 1, 2, 3, 0, 0]

def kmp_algorithm(s, p):
    index_list = []
    M, N = len(p), len(s)
    table = [0] * M
    maketable(p, table)
    i, j = 0, 0
	while i < N:
        if p[j] == s[i]: # 문자열이 같은 경우
            i += 1
            j += 1
        else:          # p[j] != s[i]:
            if j != 0: # 이전의 성공한 부분으로 돌아감
                j = table[j - 1]
            else: 
                i += 1
        if j == M: # pattern 을 찾은 경우
            index_list.append(i - j) # 문자열 처음 나오는 부분 저장
            j = table[j - 1]         # 이전 인덱스만큼 이동해서 계속 검색
            # i += M, j = 0 으로 해도되지않을까
```



#### 03 보이어무어 알고리즘

패턴의 오른쪽에서 부터 비교하며 문자가 불일치하는경우 스킵함

```python
# string = 'abcdabcdabcdabcdabcef'
# pattern = 'abcdabcef'
def boyer_moore(s, p):
    M, N = len(p), len(s)
    i = 0
    while i <= N - M:
        j = M - 1
        while j >= 0:
            if p[j] != s[i + j]:
               move = skip(p, s[i + M - 1])
               break
            j -= 1
        if j == -1:
            return True
        else:
            i += move
    return False

def skip(p, ch):
    for i in range(len(pattern)-2, -1, -1):
        if p[i] == ch:
            return len(p) - i - 1
    return len(p)
```



#### 04 카프 라빈(라빈 카프) 알고리즘

해시 사용. O(N)



## Stack1 스택

### 01 스택

LIFO / FILO

선형구조: 자료간의 관계가 1:1의 관계 -> 연결리스트 생각하면 될듯

```C
#define MAX_STACK_SIZE 100
int stack[MAX_STACK_SIZE];
int top=-1;
int IsEmpty(){
    if(top < 0)
        return 1;
    else
        return 0;
}
int IsFull(){
    if(top >= MAX_STACK_SIZE-1)
        return 1;
    else
        return 0;
} 
void push(int value){
    if(IsFull())
        printf("Stack is full!\n");
    else
        stack[++top]=value; 
}
 
int pop(){
    if(IsEmpty())
        printf("Stack is empty!\n");
    else 
        return stack[top--];
}
```



### 02 재귀호출 

시스템 stack을 사용하는 방법

top-down 

### 03 DP, Memoization

매우 많은 중복 호출을 줄이는 방법 

bottom up 방식



### 04 DFS

깊이 우선 탐색

비선형적인 그래프 구조에서 모든 자료를 빠짐없이 검색하는 방법

갈림길을 기억해야하므로 stack 사용, 방문확인으로 중복되지않게 순회



## Stack2 스택

### 01 계산기

괄호확인, 전위표기, 중위표기, 후위표기



### 02 백트래킹

DFS 와다른점? 모든 노드를 순회하는 것이 아니고 유망한지 확인하면서 가지치기 사용



### 03 분할정복

작은 문제로 나누어서 해결하는 방법

Top down방식



### 04 퀵정렬

```C
// C
void quickSort(int *arr, int s, int e){
    if (s < end){
        p = partition(*arr, s, e);
        quickSort(*a, s, p - 1);
        quickSort(*a, p + 1, e);
    }
}
// Hoare-partition
void partition(int *arr, int l, int r){
    int pivot, i, j, tmp;
    pivot = (l + r)/2;
    i = l;
    j = r;
    while (i <= j){
        while (arr[i] <= pivot) i++;
        while (arr[j] >= pivot) j--;
        if (i< j){
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    tmp = arr[l];
    arr[l] = arr[j];
    arr[j] = tmp;
    return j
}

// Lomuto
void partition(int *arr, int l, int r){
    int i, x;
    x = arr[r]
    i = l - 1;
    for (int j=l; j<r; j++){
        if (arr[j] <= x){
            i++;
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;

        }
    }
    tmp = arr[i + 1];
    arr[i + 1] = arr[r];
    arr[r] = tmp;
    return j
}
```



## Queue 큐

FIFO

선형구조: 자료간의 관계가 1:1의 관계 

### 01 선형 큐, 원형 큐, 연결 큐

차이?



### 02 우선순위 큐

시간복잡도

배열 : 삭제는 O(1), 삽입은 O(n)

연결리스트 : 삭제는 O(1), 삽입은 O(n)

힙: 삭제는 O(logn), 삽입은 O(logn)



### 03 BFS

최소 거리 탐색할때 유용함



## Linked List 연결리스트

### 01 리스트

- 선형/ 순차 리스트: 배열을 사용했을때 중간부분에 데이터를 삽입,삭제하려면 모든 데이터를 옮겨야하는 상황이 발생함
- 연결리스트: 구조체로 만들어놓고 data와 주소를 받아서 연결시킴
  - 삽입 삭제시에도 이전 노드의 주소만 바꿔주면 됨
  - 단일 연결: 뒤 노드의 주소 기억, 이중 연결: 앞뒤 노드 주소 기억



### 02 삽입정렬

S: 정렬된 원소를 저장할 리스트, U: 정렬되지 않은 원소가 있는 리스트 필요

U에서 원소를 하나씩 꺼내서 S의 뒷부분부터 위치를 찾아 삽입함.



### 03 병합정렬

분할 정복

```python
# python
def merge_sort(arr):
    if len(arr) == 1: return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    N = len(left)
    M = len(right)
    result = []
    i, j = 0, 0
    while i < N  or j < M:
        if i < N  and j < M:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(left[j])
                j += 1
        elif i < N:
            result.append(left[i])
            i += 1
        elif j < M:
            result.append(left[j])
            j += 1
    return result
```



### 04 리스트를 이용한 스택

```C
// 스택 구현

// 구조체 선언
typedef struct stack{
    char data; //들어갈 데이터, int나 long이나 상관 없음
    struct stack* link; // 다음 노드의 주소값을 저장할 포인터 변수
} stack;
stack* top; // 맨위 노드 주소를 저장 

// isfull 은 필요없음
int isEmpty() {
	if(top == NULL) {
		printf("Stack is Empty!\n");
		return 1;
	}
	return 0;
}

void push(data) {
    // 새로운 노드 newnode 동적 할당
	stack* newnode = (stack *)malloc(sizeof(stack));
    // newnode의 data에 값 저장
	newnode -> data = data;     
    // newnode의 link에 맨 위의 노드 주소 저장, 이전 값을 연결함
	newnode -> link = top;      
    // top 주소 갱신
	top = newnode;
}
char pop() {//  Stack data 자료형에 맞게 수정해서 사용
	if(!isEmpty()) {
        // temp 포인터 변수를 선언해 맨 위 노드의 주소값을 저장
		stack* temp = top;
        // data 변수를 새로 선언하여 맨 위 노드의 데이터 저장
		char data = temp -> data;
        // top을 연결된 주소값으로 갱신
		top = temp -> link;
        // 맨 위 노드 제거. 동적 할당했으므로 free사용
		free(temp);           
		return data;
	}
}
char peek() {      // 스택의 맨 위의 원소를 반환하는 함수
	if(!isEmpty) {
		return top -> data;
	}
}
```



###  05 우선순위 큐

연결리스트를 이용하여 자료 저장

원소를 삽입하는 과정에서 원소들과 비교하여 삽입



## Tree 트리

비선형 구조

### 01 이진 트리

포화이진트리, 완전이진트리, 편향 이진트리 등



### 02 트리 순회

노드를 방문하고 처리하는 순서에 따라 순회 방법이 나뉨.(LR)

전위 순회: VLR

중위 순회: LVR

후위 순회: LRV



### 03 이진 탐색 트리

중위 순회하면 오름차순으로 정렬된 값을 얻을수 있음

조건: 왼쪽 서브트리< 루트노드< 오른쪽 서브트리 

삽입, 삭제 시 위 조건이 항상 성립해야됨



### 04 힙

완전 이진트리 사용

루트 노드의 값에 따라 최대, 최소 힙이 됨

조건: 부모노드> 자식 노드 or 부모노드 < 자식노드

삭제 - 루트 노드 삭제 후 가장 끝부분의 노드를 루트노드에 두고 정렬

삽입 - 완전 이진트리를 만족하는 끝부분에 놓고 정렬