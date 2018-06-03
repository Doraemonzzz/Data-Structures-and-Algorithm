#include <stdio.h>
void Swap(int *a,int *b);
void PercDown( int A[], int p, int N );
void HeapSort( int A[], int N );

int main(){
	const int n1=1000000;
	const int n2=100000;
	
	int n,k,m;
	scanf("%d %d %d",&n,&k,&m);
	//读入分值,第一个元素为0 
	int p[k+1]={0};
	for(int i=1;i<k+1;i++){
		scanf("%d",&p[i]);
	}
	
	//读入数据,增加一个维度方便后续处理 
	int a[n+1][k+1]={0};
	//判断有没有交,如果交了则为1 
	int flag[n+1]={0};
	
	for(int i=1;i<n+1;i++){
		for(int j=1;j<k+1;j++){
			a[i][j]=-2;
		}
	}
	
	for (int i=0;i<m;i++){
		int x,y,z;
		scanf("%d %d %d",&x,&y,&z);
		if(z>=-1){
			flag[x]=1;
		}
		if(z>a[x][y]){
			a[x][y]=z;
		}
	}
	
//	for (int i=0;i<n+1;i++){
//		printf("%d\n",flag[i]);
//	}
	
	//记录总分
	int b[n]={0};
	for (int i=1;i<n+1;i++){
		//记录满分个数 
		int s=0;

		for (int j=1;j<k+1;j++){
			if(a[i][j]>0){
				b[i-1]+=n1*a[i][j];
			}
			if(a[i][j]==p[j]){
				s++;
			}
		}
		b[i-1]+=n2*s+(n+1-i);
	}
	HeapSort(b,n);
	
	int index=1;
	int j=1;
	int start=n-1;
	int temp=b[n-1]/n1;
	int s=0;
	
	while(index<=k && j<=n){
		int i=n+1-b[n-j]%n2;
		//printf("%d\n",i);
		int score=b[n-j]/n1;
		
		if (score!=temp){
			index+=s;
			temp=score;
			s=1;
		}else{
			s++;
		}
		if(flag[i]>0){
			printf("%d ",index);
			if(i>=10000){
				printf("%d",i);
			}else if(i>=1000){
				printf("0%d",i);
			}else if(i>=100){
				printf("00%d",i);
			}else if(i>=10){
				printf("000%d",i);
			}else{
				printf("0000%d",i);
			}
			printf(" %d",score);
			for(int p=1;p<=k;p++){
				if(a[i][p]>=0){
					printf(" %d",a[i][p]);
				}else if (a[i][p]==-1){
					printf(" 0");
				}else{
					printf(" -");
				}
			}
			printf("\n");
			}
		j++;
	}
	return 0;
		
}

//交换 
void Swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}

//最大堆下滤 
void PercDown( int A[], int p, int N ){
	/* 将N个元素的数组中以A[p]为根的子堆调整为最大堆 */
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

//堆排序 
void HeapSort( int A[], int N ){
	int i;
	
	//从有子节点的点开始 
	for(i=N/2-1;i>=0;i--){
		PercDown(A,i,N);
	}

	for(i=N-1;i>0;i--){
		Swap(&A[0],&A[i]);
		PercDown(A,0,i);
	}
}
