#include <stdio.h> 
typedef int Positon;
struct SNode{
	ElementType *Data;/* �洢Ԫ�ص����� */
	Positon Top;	  /* ջ��ָ�� */
	int MaxSize;	  /* ��ջ������� */
};
typedef struct SNode *Stack;

Stack CreateStack(int MaxSize)
{
	Stack S=(Stack)malloc(sizeof(struct SNode));
	S->Data=(ElementType *)malloc(MaxSize * sizeof(ElementType));
	S->Top=-1;
	S->MaxSize=MaxSize;
	return S;
}

bool IsFull(Stack S)
{
	return (S->Top==S->MaxSize-1);
}

bool Push(Stack S,ElementType X)
{
	if (IsFull(S)){
		printf("��ջ��");
		return false;
	}
	else{
		S->Data[++(S->Top)]=X;
		return true
	}
}

bool IsEmpty(Stack S)
{
	return (S->Top==-1);
}

ElementType Pop(Stack S)
{
	if (IsEmpty(S)){
		printf("��ջ��");
		return ERROR;/* ERROR��ElementType������ֵ����־���� */
	}
	else
		return (S->Data[(S->Top)--]);
}
