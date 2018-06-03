#include <stdio.h>
void Merge( int A[], int TmpA[], int L, int R, int RightEnd );
void Merge_pass(int A[],int TmpA[], int N, int length );
int compare(int a[],int b[],int n);

int main(){
	int n;
	scanf("%d",&n);
	int a[n],b[n],c[n];
	int i;
	//读取第一行,a[]给merge sort使用,b[]给Insertion Sort使用 
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
		b[i]=a[i];
	}
	//读取第二行
	for (i=0;i<n;i++){
		scanf("%d",&c[i]);
	}
	
	//判断是否为merge sort 
	int temp[n];
	int length=1;
	int flag1=0;
	int flag2=0;
	//printf("%d\n",flag1);
	while(length<n){
		Merge_pass(a,temp,n,length);
		length*=2;
		//判断是否和题目相等，如果相等，再完成一遍 
		if(flag1==0){
			flag1=compare(temp,c,n);
		}else{
			int k;
			for(k=0;k<n;k++){
				a[k]=temp[k];
			}
			break;
		}

		Merge_pass( temp, a, n, length );
		length*=2;
		//判断是否和题目相等，如果相等，再完成一遍 
		if(flag1==0){
			flag1=compare(a,c,n);
		}else{
			break;
		}
	}
	
	//printf("%d\n",flag1);
	if(flag1){
		printf("Merge Sort\n");
		printf("%d",a[0]);
		int i;
		for(i=1;i<n;i++){
			printf(" %d",a[i]);
		}
	}else{
		int p,j;
		for(p=1;p<n;p++){
			int temp=b[p];
			for(j=p;j>0&&b[j-1]>temp;j--){
				b[j]=b[j-1];
			}
			b[j]=temp;
			if(flag2){
				break;
			}
			flag2=compare(b,c,n);			
		}
		printf("Insertion Sort\n");
		printf("%d",b[0]);
		int i;
		for(i=1;i<n;i++){
			printf(" %d",b[i]);
		}
	}
}

void Merge( int A[], int TmpA[], int L, int R, int RightEnd ){
	/* 将有序的A[L]~A[R-1]和A[R]~A[RightEnd]归并成一个有序序列 */
	int LeftEnd,NumElements,Tmp;
	int i;
	
	LeftEnd=R-1;/* 左边终点位置 */
	Tmp=L;	/* 有序序列的起始位置 */
	NumElements=RightEnd-L+1;
	
	while(L<=LeftEnd&&R<=RightEnd){
		if(A[L]<=A[R]){
			TmpA[Tmp++]=A[L++];
		}else{
			TmpA[Tmp++]=A[R++];
		}
	}
	while(L<=LeftEnd){
		TmpA[Tmp++]=A[L++];
	}
	while(R<=RightEnd){
		TmpA[Tmp++]=A[R++];
	}
	
	for(i=0;i<NumElements;i++,RightEnd--){
		A[RightEnd]=TmpA[RightEnd];
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

/*判断是否和输出一样*/
int compare(int a[],int b[],int n){
	int flag=1;
	int i;
	for(i=0;i<n;i++){
		if (a[i]!=b[i]){
			flag=0;
			break;
		}
	}
	return flag;
} 
