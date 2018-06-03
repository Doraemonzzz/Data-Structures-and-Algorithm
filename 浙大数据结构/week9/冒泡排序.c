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
	for(p=n-1;p>=0;p--){
		int flag=0;
		for(j=0;j<p;j++){
			if(a[j]>a[j+1]){
				int temp=a[j+1];
				a[j+1]=a[j];
				a[j]=temp;
				flag=1;
			}
		}
		if(flag==0){
			break;
		}
	}
	printf("%d",a[0]);
	for(i=1;i<n;i++){
		printf(" %d",a[i]);
	}
	return 0;	
}
/*
提交时间	状态	分数	题目	编译器	耗时	用户
2018/5/8 14:07:54	部分正确	19	09-排序1	C (gcc)	420 ms	蓝色的狸猫
测试点	结果	耗时	内存
0	答案正确	1 ms	256KB
1	答案正确	1 ms	256KB
2	答案正确	4 ms	256KB
3	答案正确	213 ms	268KB
4	运行超时	0 ms	0KB
5	答案正确	42 ms	1276KB
6	运行超时	0 ms	0KB
7	答案正确	420 ms	1288KB
8	运行超时	0 ms	0KB
*/
