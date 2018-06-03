#include <stdio.h>

int MaxSubseqSum(int A[],int N);

int main(){
	//获取数组的长度 
	int a;
	scanf("%d",&a);
	
	//将数组存入数组
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
