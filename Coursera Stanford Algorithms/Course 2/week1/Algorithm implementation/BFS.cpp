#include <cstdio>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

const int N = 1e6;

//����ͼ
vector <int> G[N];
//�ڵ�����
int n = 1;
//�ж��Ƿ���ʹ�
int flag[N];
//�洢���
vector <int> res;

void BFS(vector <int> Graph[], int i){
    //��ʼ��ջ
    queue <int> Q;
    Q.push(i);
    flag[i] = 1;
    while (!Q.empty()){
        int u = Q.front();
        res.push_back(u);
        Q.pop();
        //���
        for (int k = 0; k < Graph[u].size(); k++){
            int v = Graph[u][k];
            if (flag[v] == 0){
                flag[v] = 1;
                Q.push(v);
            }
        }
    }
}

void Print(vector <int> res){
    int m = res.size();
    for (int i = 0; i < m; i++){
        printf("%d", res[i]);
        if (i < m - 1){
            printf("->");
        }else{
            printf("\n");
        }
    }
}

int main(){
    //�ļ���
    char filename[] = "test_data.txt";
    freopen(filename, "r", stdin);
    //��¼�ڵ�����
    int u, v;
    //�����ڽӱ�
    while (scanf("%d %d", &u, &v) != EOF){
        n = max(n, u);
        n = max(n, v);
        G[u].push_back(v);
    }

    //��ʼ��
    memset(flag, 0, sizeof(flag));
    for (int i = 1; i <= n; i++){
        if (flag[i] == 0){
            BFS(G, i);
        }
    }
    //���
    Print(res);

    return 0;
}
