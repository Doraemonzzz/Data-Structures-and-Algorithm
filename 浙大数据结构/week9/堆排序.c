#include <stdio.h>
void Swap(int *a,int *b);
void PercDown( int A[], int p, int N );
void HeapSort( int A[], int N );

int main(){
	int n;
	scanf("%d",&n);
	int a[n];
	int i;
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	HeapSort(a,n);
	printf("%d",a[0]);
	for(i=1;i<n;i++){
		printf(" %d",a[i]);
	}
	return 0;	
}

//交换 
void Swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}

//最大堆下滤 
void PercDown( int A[], int p, int N ){
	/* 将N个元素的数组中以A[p]为根的子堆调整为最大堆 */
	int Parent,Child,x;
	x=A[p];
	
	for(Parent=p;(2*Parent+1)<N;Parent=Child){
		Child=Parent*2+1;
		if((Child<N-1)&&(A[Child]<A[Child+1])){
			Child++;
		}
		if(x>=A[Child]){
			break;
		}else{
			A[Parent]=A[Child];
		}
	}	
	A[Parent]=x;
}

//堆排序 
void HeapSort( int A[], int N ){
	int i;
	
	//从有子节点的点开始 
	for(i=N/2-1;i>=0;i--){
		PercDown(A,i,N);
	}

	for(i=N-1;i>0;i--){
		Swap(&A[0],&A[i]);
		PercDown(A,0,i);
	}
}
 
