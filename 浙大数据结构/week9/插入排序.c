#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	int a[n];
	int i;
	for (i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	int p,j;
	for(p=1;p<n;p++){
		int temp=a[p];
		for(j=p;j>0&&a[j-1]>temp;j--){
			a[j]=a[j-1];
		}
		a[j]=temp;
	}
	printf("%d",a[0]);
	for(i=1;i<n;i++){
		printf(" %d",a[i]);
	}
	return 0;	
}
/*
2018/5/8 14:15:13	����ȷ	25	09-����1	C (gcc)	5295 ms	��ɫ����è
���Ե�	���	��ʱ	�ڴ�
0	����ȷ	1 ms	256KB
1	����ȷ	2 ms	256KB
2	����ȷ	2 ms	256KB
3	����ȷ	32 ms	276KB
4	����ȷ	2662 ms	1172KB
5	����ȷ	42 ms	1288KB
6	����ȷ	5295 ms	1152KB
7	����ȷ	66 ms	1172KB
8	����ȷ	2661 ms	904KB
*/ 
