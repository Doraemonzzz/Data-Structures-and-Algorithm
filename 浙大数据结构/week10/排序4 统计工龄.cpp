#include <stdio.h>

int main(){
	//年龄的桶 
	int a[51]={0};
	
	//记录循环次数 
	int n;
	scanf("%d",&n);
	
	//记录年龄 
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
