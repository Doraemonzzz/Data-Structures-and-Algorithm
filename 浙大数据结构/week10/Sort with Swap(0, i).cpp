#include <stdio.h>
void swap(int *a,int *b){
	//printf("%d %d\n",*a,*b);
	int temp=*a;
	*a=*b;
	*b=temp;
	//printf("%d %d\n",*a,*b);
}

int main(){
	int n;
	scanf("%d",&n);
	
	//�������� 
	int a[n];
	//��¼a[i]!=i��Ԫ�ظ��� 
	int s=0;
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
		if(a[i]!=i){
			s++;
		}
	}
	
	//�������� 
	int k=0;
	//������ȷһ�㣬����0���⣬����Ԫ������Ѿ����Լ���λ��,��ô�Ͳ������ƶ��� 
	//��¼��0������Ԫ�صĿ�ʼλ�� 
	int index=1;
	
	
	while(s>0){
		//0��0�ϣ���ô�͵�һ�������Լ�λ����Ԫ�ؽ��� 
		if(a[0]==0){
			while(index<n){
				if(a[index]!=index){
					swap(&a[0],&a[index]);
					break;
				}
				//��һ�α����Ӻ�һ��Ԫ�ؿ�ʼ 
				index++;
			}
			//a[i]!=i��Ԫ�ظ�����1 
			s++;
			//����������1 
			k++;
		//0����0�ϣ�������a[0]=k,��ôֱ�ӽ���a[0]��a[k]��ʹ��k��a[k]�� 
		}else{
			swap(&a[0],&a[a[0]]);
			//���a[0]����Ϊ0��a[i]!=i��Ԫ�ظ������� 2���������1 
			if(a[0]==0){
				s-=2;
			}else{
				s--;
			}
			//����������1 
			k++;
		}
	}
	printf("%d",k);
	return 0;
}

