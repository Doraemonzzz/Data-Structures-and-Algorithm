//½¨AVLÊ÷  
#include <stdio.h>  
#include <stdlib.h>  
  
typedef struct AVLNode *AVLTree;  
typedef struct AVLNode *Position;  
struct AVLNode {  
    int Data;  
    int Height;  
    AVLTree Left;  
    AVLTree Right;  
};  
  
AVLTree Insert(int X, AVLTree T);  
int GetHeight(Position T);  
int Max(int a, int b);  
Position SingleLeft(Position K);  
Position SingleRight(Position K);  
Position DoubleLeft(Position K);  
Position DoubleRight(Position K);  
  
int main(void) {  
    AVLTree T = NULL;  
    int n;  
    scanf("%d", &n);  
    while (n--) {  
        int x;  
        scanf("%d", &x);  
        T=Insert(x, T);  
    }  
    if (T)  
        printf("%d", T->Data);  
    return 0;  
}  
  
AVLTree Insert(int X, AVLTree T) {  
    if (T == NULL) {  
        T = (AVLTree)malloc(sizeof(struct AVLNode));  
        T->Data = X;  
        T->Height = 0;  
        T->Left = T->Right = NULL;  
    }  
    else if (X < T->Data) {  
        T->Left = Insert(X, T->Left);  
        if (GetHeight(T->Left) - GetHeight(T->Right) == 2) {  
            if (X < T->Left->Data)  
                T = SingleLeft(T);  
            else  
                T = DoubleLeft(T);  
        }  
    }  
    else if (X > T->Data) {  
        T->Right = Insert(X, T->Right);  
        if (GetHeight(T->Right) - GetHeight(T->Left) == 2) {  
            if (X > T->Right->Data)  
                T = SingleRight(T);  
            else  
                T = DoubleRight(T);  
        }  
    }  
    T->Height = Max(GetHeight(T->Left), GetHeight(T->Right)) + 1;  
    return T;  
}  
  
int GetHeight(Position T) {  
    if (!T)  
        return -1;  
    else  
        return T->Height;  
}  
  
int Max(int a, int b) {  
    return (a > b) ? a : b;  
}  
  
Position SingleLeft(Position K) {  
    Position Tmp;  
    Tmp = K;  
    K = K->Left;  
    Tmp->Left = K->Right;  
    K->Right = Tmp;  
    Tmp->Height = Max(GetHeight(Tmp->Left), GetHeight(Tmp->Right)) + 1;  
    K->Height = Max(GetHeight(K->Left), GetHeight(K->Right)) + 1;  
    return K;  
}  
  
Position SingleRight(Position K) {  
    Position Tmp;  
    Tmp = K;  
    K = K->Right;  
    Tmp->Right = K->Left;  
    K->Left = Tmp;  
    Tmp->Height = Max(GetHeight(Tmp->Left), GetHeight(Tmp->Right)) + 1;  
    K->Height = Max(GetHeight(K->Left), GetHeight(K->Right)) + 1;  
    return K;  
}  
  
Position DoubleLeft(Position K) {  
    K->Left = SingleRight(K->Left);   
    return SingleLeft(K);  
}  
  
Position DoubleRight(Position K) {  
    K->Right = SingleLeft(K->Right);  
    return SingleRight(K);  
}  
