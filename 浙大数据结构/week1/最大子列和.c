#include <stdio.h>

int MaxSubseqSum(int A[],int N);

int main(){
	//��ȡ����ĳ��� 
	int a;
	scanf("%d",&a);
	
	//�������������
	int b[a];
	int i;
	for (i=0;i<a;i++){
		scanf("%d",&b[i]);
	}
	
	int sum;
	sum=MaxSubseqSum(b,a);
	
	printf("%d",sum);

}
int MaxSubseqSum(int A[],int N){
	int sum=0;
	int maxsum=0;
	int i;
	for (i=0;i<N;i++){
		sum+=A[i];
		if (sum<0){
			sum=0;
		}else if(sum>maxsum){
			maxsum=sum;
		}
	}
	return maxsum;
} 
