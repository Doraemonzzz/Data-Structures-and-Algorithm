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
�ύʱ��	״̬	����	��Ŀ	������	��ʱ	�û�
2018/5/8 14:07:54	������ȷ	19	09-����1	C (gcc)	420 ms	��ɫ����è
���Ե�	���	��ʱ	�ڴ�
0	����ȷ	1 ms	256KB
1	����ȷ	1 ms	256KB
2	����ȷ	4 ms	256KB
3	����ȷ	213 ms	268KB
4	���г�ʱ	0 ms	0KB
5	����ȷ	42 ms	1276KB
6	���г�ʱ	0 ms	0KB
7	����ȷ	420 ms	1288KB
8	���г�ʱ	0 ms	0KB
*/
