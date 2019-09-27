#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

const int N = 1e6;

//定义图
vector <int> G[N], Grev[N];
//判断是否访问过
int flag[N];
//leader数组
int leader[N];
//结束时间
int finish[N];
//结束时间->节点编号
int Index[N];
//leader
int s;
//访问时间
int t;
//节点数量
int n = 1;

bool cmp(int a, int b){
    return a > b;
}

//深度优先搜索（第一轮）
void DFS_v1(vector <int> Graph[], int i){
    //初始化栈
    stack <int> Q;
    Q.push(i);
    flag[i] = 1;
    //记录顺序
    vector <int> tmp;
    while (!Q.empty()){
        int u = Q.top();
        Q.pop();
        leader[u] = s;
        //存储结果
        tmp.push_back(u);
        //入队
        for (int k = 0; k < Graph[u].size(); k++){
            int v = Graph[u][k];
            if (flag[v] == 0){
                flag[v] = 1;
                Q.push(v);
            }
        }
    }
    //计算finish, Index;
    for (int j = tmp.size() - 1; j >= 0; j--){
        int u = tmp[j];
        t++;
        finish[u] = t;
        Index[t] = u;
    }
}

//深度优先搜索（第二轮）
void DFS_v2(vector <int> Graph[], int i, int& cnt){
    //初始化栈
    stack <int> Q;
    Q.push(i);
    flag[i] = 1;
    while (!Q.empty()){
        int u = Q.top();
        Q.pop();
        //入队
        for (int k = 0; k < Graph[u].size(); k++){
            int v = Graph[u][k];
            if (flag[v] == 0){
                flag[v] = 1;
                Q.push(v);
            }
        }
        //更新计数
        cnt++;
    }
}

//递归版本
//void DFS_v1(vector <int> Graph[], int i){
//    flag[i] = 1;
//    leader[i] = s;
//    for (int k = 0; k < Graph[i].size(); k++){
//        int j = Graph[i][k];
//        if (flag[j] == 0){
//            DFS_v1(Graph, j);
//        }
//    }
//    t++;
//    finish[i] = t;
//    //记录时间和索引的关系
//    Index[t] = i;
//}

//void DFS_v2(vector <int> Graph[], int i, int &cnt){
//    flag[i] = 1;
//    cnt++;
//    for (int k = 0; k < Graph[i].size(); k++){
//        int j = Graph[i][k];
//        if (flag[j] == 0){
//            DFS_v2(Graph, j, cnt);
//        }
//    }
//}

int main(){
    //输入
    //文件名
    char filename[] = "SCC.txt";
    freopen(filename, "r", stdin);
    //记录节点数量
    int u, v;
    while (scanf("%d %d", &u, &v) != EOF){
        n = max(n, u);
        n = max(n, v);
        G[u].push_back(v);
        Grev[v].push_back(u);
    }

    //第一轮
    //初始化
    memset(flag, 0, sizeof(flag));
    t = 0;
    for (int i = n; i >= 1; i--){
        if (flag[i] == 0){
            //设置leader
            s = i;
            DFS_v1(Grev, i);
        }
    }

    //第二轮
    memset(flag, 0, sizeof(flag));
    //记录SCC的元素数量
    vector <int> res;
    for (int k = n; k >= 1; k--){
        int i = Index[k];
        int cnt = 0;
        if (flag[i] == 0){
            DFS_v2(G, i, cnt);
            res.push_back(cnt);
        }
    }

    //排序
    sort(res.begin(), res.end(), cmp);
    //输出
    int m = (res.size() > 5)? 5: res.size();
    for (int i = 0; i < m; i++){
        printf("%d", res[i]);
        if (i < m - 1){
            printf(", ");
        }else{
            printf("\n");
        }
    }

    return 0;
}
