#include <stdio.h>

int findmin(long long a[],int b[],int n);

int main(){
	int n,m,s,d;
	scanf("%d %d %d %d",&n,&m,&s,&d);
	
	long long v[n][n];
	//��ʼ��
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			v[i][j]=0;
		}
	} 
	
	//��������,���߳���һ���ܴ��Ȩ�أ�����һ�����򼴿ɡ� 
	int a,b,c,e;
	for (int i=0;i<m;i++){
		scanf("%d %d %d %d",&a,&b,&c,&e);
		v[a][b]=c*10000000000+e;
		v[b][a]=c*10000000000+e;
	}
	
	//��¼�Ƿ���ʹ�
	int y[n]={0};

	//��¼dist
	long long p[n];
	for (int i=0;i<n;i++){
		p[i]=1000000000000000;
	}
	p[s]=0;
	
	while (1){
		int k=findmin(p,y,n);
		if (k==-1){
			break;
		}
		y[k]=1;
		for (int j=0;j<n;j++){
			//δ�������б����� 
			if (y[j]==0&&v[k][j]>0){
				if (p[k]+v[k][j]<p[j]){
					p[j]=p[k]+v[k][j];
				}
			}
		}
	}
	printf("%d %d",p[d]/10000000000,p[d]%10000000000);
}

int findmin(long long a[],int b[],int n){
	long long l=1000000000000000;
	int m=-1;
	for (int i=0;i<n;i++){
		if (b[i]==0 && a[i]<l){
			l=a[i];
			m=i;
		}
	}
	return m;
}
