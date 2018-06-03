#include <stdio.h>
int main(){
	/* 希尔排序 - 用Sedgewick增量序列 */
	int n;
	scanf("%d",&n);
	int a[n];
	int i;
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	int Sedgewick[] = {929, 505, 209, 109, 41, 19, 5, 1, 0};
	
	int s;
	for(s=0;Sedgewick[s]>=n;s++);
	
	int D;
	for(D=Sedgewick[s];D>0;D=Sedgewick[++s]){
		int p,j;
		for(p=D;p<n;p++){
			int temp=a[p];
			for(j=p;j>=D&&a[j-D]>temp;j-=D){
				a[j]=a[j-D];
			}
		a[j]=temp;
		}
	}
	printf("%d",a[0]);
	for(i=1;i<n;i++){
		printf(" %d",a[i]);
	}
	return 0;	
}
