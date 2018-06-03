#include <stdio.h>
void Merge( int A[], int TmpA[], int L, int R, int RightEnd );
void Merge_pass(int A[],int TmpA[], int N, int length );
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
	
	//�ж��Ƿ�Ϊmerge sort 
	int temp[n];
	int length=1;
	int flag1=0;
	int flag2=0;
	//printf("%d\n",flag1);
	while(length<n){
		Merge_pass(a,temp,n,length);
		length*=2;
		//�ж��Ƿ����Ŀ��ȣ������ȣ������һ�� 
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
		//�ж��Ƿ����Ŀ��ȣ������ȣ������һ�� 
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
	/* �������A[L]~A[R-1]��A[R]~A[RightEnd]�鲢��һ���������� */
	int LeftEnd,NumElements,Tmp;
	int i;
	
	LeftEnd=R-1;/* ����յ�λ�� */
	Tmp=L;	/* �������е���ʼλ�� */
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
