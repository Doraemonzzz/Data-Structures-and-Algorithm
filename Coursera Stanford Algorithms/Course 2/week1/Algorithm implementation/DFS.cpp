#include <cstdio>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

const int N = 1e6;

//定义图
vector <int> G[N];
//节点数量
int n = 1;
//判断是否访问过
int flag[N];
//存储结果
vector <int> res;

void DFS(vector <int> Graph[], int i){
    flag[i] = 1;
    res.push_back(i);
    for (int k = 0; k < Graph[i].size(); k++){
        int j = Graph[i][k];
        if (flag[j] == 0){
            DFS(Graph, j);
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
    //文件名
    char filename[] = "test_data.txt";
    freopen(filename, "r", stdin);
    //记录节点数量
    int u, v;
    //构造邻接表
    while (scanf("%d %d", &u, &v) != EOF){
        n = max(n, u);
        n = max(n, v);
        G[u].push_back(v);
    }

    //初始化
    memset(flag, 0, sizeof(flag));
    for (int i = 1; i <= n; i++){
        if (flag[i] == 0){
            DFS(G, i);
        }
    }
    //输出
    Print(res);


    return 0;
}
