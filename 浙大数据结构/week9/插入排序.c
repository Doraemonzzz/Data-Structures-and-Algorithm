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
2018/5/8 14:15:13	答案正确	25	09-排序1	C (gcc)	5295 ms	蓝色的狸猫
测试点	结果	耗时	内存
0	答案正确	1 ms	256KB
1	答案正确	2 ms	256KB
2	答案正确	2 ms	256KB
3	答案正确	32 ms	276KB
4	答案正确	2662 ms	1172KB
5	答案正确	42 ms	1288KB
6	答案正确	5295 ms	1152KB
7	答案正确	66 ms	1172KB
8	答案正确	2661 ms	904KB
*/ 
