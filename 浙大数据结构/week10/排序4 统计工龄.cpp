#include <stdio.h>

int main(){
	//�����Ͱ 
	int a[51]={0};
	
	//��¼ѭ������ 
	int n;
	scanf("%d",&n);
	
	//��¼���� 
	int x;
	for(int i=0;i<n;i++){
		scanf("%d",&x);
		a[x]++;
	}
	
	for(int i=0;i<51;i++){
		if(a[i]!=0){
			printf("%d:%d\n",i,a[i]);
		}
	}
	
	return 0;
}
