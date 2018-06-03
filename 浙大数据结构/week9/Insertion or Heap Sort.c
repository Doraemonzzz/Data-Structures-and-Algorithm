#include <stdio.h>
void Swap(int *a,int *b);
void PercDown( int A[], int p, int N );
int compare(int a[],int b[],int n);

int main(){
	int n;
	scanf("%d",&n);
	int a[n],b[n],c[n];
	int i;
	//��ȡ��һ��,a[]��merge sortʹ��,b[]��Insertion Sortʹ�� 
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
		b[i]=a[i];
	}
	//��ȡ�ڶ���
	for (i=0;i<n;i++){
		scanf("%d",&c[i]);
	}
	
	//�ж��Ƿ�Ϊheap sort
	int temp[n];
	int length=1;
	int flag1=0;
	int flag2=0;
	//printf("%d\n",flag1);
	//�����ӽڵ�ĵ㿪ʼ 
	for(i=n/2-1;i>=0;i--){
		PercDown(a,i,n);
	}
	
	for(i=n-1;i>0;i--){
		Swap(&a[0],&a[i]);
		PercDown(a,0,i);
		if(flag1){
			break;
		}
		flag1=compare(a,c,n);
	}
	
	if(flag1){
		printf("Heap Sort\n");
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
//			printf("%d\n",p);
//			for(i=0;i<n;i++){
//				printf("%d ",b[i]);
//			}
//			printf("\n");
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

//���� 
void Swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}

//�������� 
void PercDown( int A[], int p, int N ){
	/* ��N��Ԫ�ص���������A[p]Ϊ�����Ӷѵ���Ϊ���� */
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

/*�ж��Ƿ�����һ��*/
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
