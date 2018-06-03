#include <stdio.h>
void Merge( int A[], int TmpA[], int L, int R, int RightEnd );
void Merge_pass(int A[],int TmpA[], int N, int length );

int main(){
	int n;
	scanf("%d",&n);
	int a[n];
	int i;
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	
	//�ж��Ƿ�Ϊmerge sort 
	int temp[n];
	int length=1;
	while(length<n){
		Merge_pass(a,temp,n,length);
		length*=2;
		Merge_pass(temp,a, n, length );
		length*=2;
	}
	
	int min=a[0];
	int max=a[n-1];
	int b[max+1];
	for(i=0;i<max+1;i++){
		b[i]=0;
	}
	for (i=0;i<n;i++){
		b[a[i]]++;
	}
	for (i=min;i<max+1;i++){
		if(b[i]>0){
			printf("%d:%d\n",i,b[i]);
		}
	}
	return 0;
}

void Merge( int A[], int TmpA[], int L, int R, int RightEnd ){
	//printf("1\n");
	/* �������A[L]~A[R-1]��A[R]~A[RightEnd]�鲢��һ���������� */
	int LeftEnd,NumElements,Tmp;
	int i;
	
	LeftEnd=R-1;/* ����յ�λ�� */
	Tmp=L;	/* �������е���ʼλ�� */
	NumElements=RightEnd-L+1;
	
	while(L<=LeftEnd&&R<=RightEnd){
		if(A[L]<=A[R]){
			TmpA[Tmp++]=A[L++];/* �����Ԫ�ظ��Ƶ�TmpA */
		}else{
			TmpA[Tmp++]=A[R++];/* ���ұ�Ԫ�ظ��Ƶ�TmpA */
		}
	}
	while(L<=LeftEnd){
		TmpA[Tmp++]=A[L++];/* ֱ�Ӹ������ʣ�µ� */
	}
	while(R<=RightEnd){
		TmpA[Tmp++]=A[R++];/* ֱ�Ӹ����ұ�ʣ�µ� */
	}
	for(i=0;i<NumElements;i++,RightEnd--){
		A[RightEnd]=TmpA[RightEnd];/* �������TmpA[]���ƻ�A[] */
	}
}

/* �����鲢������������ */
void Merge_pass(int A[],int TmpA[], int N, int length ){
	int i,j;
	for(i=0;i<=N-2*length;i+=2*length){
		Merge(A,TmpA,i,i+length,i+2*length-1);
	}
	if(i+length<N){
		Merge(A,TmpA,i,i+length,N-1);
	}else{
		for(j=i;j<N;j++){
			TmpA[j]=A[j];
		}
	}
}
