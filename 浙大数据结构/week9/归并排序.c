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
	
	//判断是否为merge sort 
	int temp[n];
	int length=1;
	//printf("%d\n",flag1);
	while(length<n){
		//printf("%d %d\n",length,n);
		Merge_pass(a,temp,n,length);
		length*=2;
		//printf("%d %d\n",length,a[0]);
		Merge_pass(temp,a, n, length );
		length*=2;
		//printf("%d %d\n",length,a[0]);
	}
	
	printf("%d",a[0]);
	for(i=1;i<n;i++){
		printf(" %d",a[i]);
	}
	return 0;
}

void Merge( int A[], int TmpA[], int L, int R, int RightEnd ){
	//printf("1\n");
	/* 将有序的A[L]~A[R-1]和A[R]~A[RightEnd]归并成一个有序序列 */
	int LeftEnd,NumElements,Tmp;
	int i;
	
	LeftEnd=R-1;/* 左边终点位置 */
	Tmp=L;	/* 有序序列的起始位置 */
	NumElements=RightEnd-L+1;
	
	while(L<=LeftEnd&&R<=RightEnd){
		if(A[L]<=A[R]){
			TmpA[Tmp++]=A[L++];/* 将左边元素复制到TmpA */
		}else{
			TmpA[Tmp++]=A[R++];/* 将右边元素复制到TmpA */
		}
	}
	while(L<=LeftEnd){
		TmpA[Tmp++]=A[L++];/* 直接复制左边剩下的 */
	}
	while(R<=RightEnd){
		TmpA[Tmp++]=A[R++];/* 直接复制右边剩下的 */
	}
	for(i=0;i<NumElements;i++,RightEnd--){
		A[RightEnd]=TmpA[RightEnd];/* 将有序的TmpA[]复制回A[] */
	}
}

/* 两两归并相邻有序子列 */
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
