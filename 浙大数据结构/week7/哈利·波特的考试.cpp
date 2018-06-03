#include <stdio.h>
#define max 100000
int findmax(int x[],int l);

int main(){
	//读入点和边的个数 
	int n,l;
	scanf("%d%d",&n,&l);
	
	//初始矩阵
	int b[n][n];
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			b[i][j]=max;
		}
	}
	
	//读入数据
	for (int i=0;i<l;i++){
		int x,y,z;
		scanf("%d%d%d",&x,&y,&z);
		b[x-1][y-1]=z;
		b[y-1][x-1]=z;
	}
	
	//弗洛伊德算法
	for (int k=0;k<n;k++){
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (i!=j and b[i][k]+b[k][j]<b[i][j]){
					b[i][j]=b[i][k]+b[k][j];
				}
				if (i==j){
					b[i][i]=0;
				}
			}
		}
	}
	
	//找每行最大值
	int leng[n];
	int flag=0;
	for (int i=0;i<n;i++){
		int l=findmax(b[i],n);
		if (l==max){
			flag=1;
			break;
		}else{
			leng[i]=l;
		}
	}
	
	//输出 
	if (flag==1){
		printf("0");
	}else{
		int l=leng[0];
		int k=0;
		for (int i=0;i<n;i++){
			if (leng[i]<l){
				l=leng[i];
				k=i;
			}
		}
		printf("%d %d",k+1,l);
	}
	return 0;
} 

int findmax(int x[],int l){
	int h=0;
	for (int i=0;i<l;i++){
		if (x[i]>h){
			h=x[i];
		}			
	}
	return h;
}

