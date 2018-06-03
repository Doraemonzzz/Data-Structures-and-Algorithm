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
	
	//读入数据 
	int a[n];
	//记录a[i]!=i的元素个数 
	int s=0;
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
		if(a[i]!=i){
			s++;
		}
	}
	
	//交换次数 
	int k=0;
	//首先明确一点，除了0以外，其余元素如果已经在自己的位置,那么就不会再移动了 
	//记录和0交换的元素的开始位置 
	int index=1;
	
	
	while(s>0){
		//0在0上，那么和第一个不在自己位置上元素交换 
		if(a[0]==0){
			while(index<n){
				if(a[index]!=index){
					swap(&a[0],&a[index]);
					break;
				}
				//下一次遍历从后一个元素开始 
				index++;
			}
			//a[i]!=i的元素个数加1 
			s++;
			//交换次数加1 
			k++;
		//0不在0上，不妨设a[0]=k,那么直接交换a[0]和a[k]，使得k在a[k]上 
		}else{
			swap(&a[0],&a[a[0]]);
			//如果a[0]正好为0，a[i]!=i的元素个数减少 2，否则减少1 
			if(a[0]==0){
				s-=2;
			}else{
				s--;
			}
			//交换次数加1 
			k++;
		}
	}
	printf("%d",k);
	return 0;
}

