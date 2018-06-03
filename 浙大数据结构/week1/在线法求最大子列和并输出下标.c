#include <stdio.h>

int MaxSubseqSum(int A[],int N);

int main(){
	//获取数组的长度 
	int a;
	scanf("%d",&a);
	
	//判断是否全为0,如果全为负数，则输出0 
	int flag=1; 
	
	//将数组存入数组
	int b[a];
	int i;
	for (i=0;i<a;i++){
		scanf("%d",&b[i]);
	}
	
	int sum=0;
	int maxsum=0;
	int x=0;
	int y=0;
	int z=0;
	
	for (i=0;i<a;i++){
		if (b[i]>=0){
			//如果有非负数，flag变为0 
			flag*=0;
		}
		sum+=b[i];
		if(sum>maxsum){
			maxsum=sum;
			x=z;
			y=i;
		}else if (sum<0){
			sum=0;
			z=i+1;
		}
	}
	if (maxsum<=0){
		if (flag){
			printf("%d %d %d",0,b[0],b[a-1]);
		}
		else{
			//flag为1表示存在非负数，而此时maxsum<=0,所以表示全为0 
			printf("%d %d %d",maxsum,0,0);
		}
	}else{
		printf("%d %d %d",maxsum,b[x],b[y]);
	}
	return 0;
}

