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

void BFS(vector <int> Graph[], int i){
    //初始化栈
    queue <int> Q;
    Q.push(i);
    flag[i] = 1;
    while (!Q.empty()){
        int u = Q.front();
        res.push_back(u);
        Q.pop();
        //入队
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
            BFS(G, i);
        }
    }
    //输出
    Print(res);

    return 0;
}
