#include <stdio.h>

int isPrime(int x){
	if (x==1){
		return 0;
	}else if(x==2){
		return 1;
	}else if(x%2==0){
		return 0;
	}else{
		for(int i=2;i<x;i++){
			if(x%i==0){
				return 0;
			}
		}
		return 1;
	}
}

int main(){
	int m,n;
	scanf("%d %d",&m,&n);
	while(isPrime(m)==0){
		m++;
	}

//	//���������ݣ���ʼ��Ϊ-1 
//	int b[n]; 
//	for(int i=0;i<n;i++){
//		b[i]=-1;
//	}
	
	int c[m]={0};

	//�������� 
	int a[n];
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	} 
	
	//��ʼ��������
	for(int i=0;i<n;i++){
		int r=a[i]%m;
		//printf("%d %d\t",r,b[r]);
		if(c[r]==0){
			printf("%d",r);
			c[r]=1;
		}else{
			int tmp=r;
			int flag=0;
			for(int j=1;j<m;j++){
				tmp=(r+j*j)%m;
				if(c[tmp]==0){
					c[tmp]=1;
					flag=1;
					printf("%d",tmp);
					break;
				}
			}
			if(flag==0){
				printf("-");
			}
		}
		if(i<n-1){
			printf(" ");
		}
	}
	return 0;
}
