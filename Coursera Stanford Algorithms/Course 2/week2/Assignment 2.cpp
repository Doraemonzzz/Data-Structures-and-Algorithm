#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <sstream>
using namespace std;

const int N = 1e6;
const int INFTY = 1e9;
//����ͼ
vector <int> G[N];
//����߳�
vector <int> G1[N];
//�ڵ�����
int n = 1;
//�ж��Ƿ���ʹ�
int flag[N];
//��������
int dist[N];

int Find_min(){
    int index = -1;
    int min_dist = INFTY;
    for (int i = 1; i <= n; i++){
        if (flag[i] == 0 && dist[i] < min_dist){
            index = i;
            min_dist = dist[i];
        }
    }

    return index;
}

void Dijkstra(int s){
    //��ʼ��
    for (int i = 1; i <= n; i++){
        dist[i] = INFTY;
    }
    for (int i = 0; i < G[s].size(); i++){
        int v = G[s][i];
        dist[v] = G1[s][i];
    }
    flag[s] = 1;
    dist[s] = 0;

    while(1){
        int u = Find_min();
        if (u == -1){
            break;
        }
        flag[u] = 1;
        //����
        for (int i = 0; i < G[u].size(); i++){
            int v = G[u][i];
            if (dist[u] + G1[u][i] < dist[v]){
                dist[v] = dist[u] + G1[u][i];
            }
        }
    }
}

int main(){
    //����
    //�ļ���
    char filename[] = "dijkstraData.txt";
    freopen(filename, "r", stdin);
    int u, v, d;
    string S;
    char c;
    while (getline(cin, S)){
        stringstream ostr(S);
        ostr >> u;
        n = max(n, u);
        while (ostr >> v >> c >> d){
            n = max(n, v);
            G[u].push_back(v);
            G1[u].push_back(d);
        }
    }

    //��ʼ��
    memset(flag, 0, sizeof(flag));
    int s = 1;
    //�����㷨
    Dijkstra(s);
    //��ʾ���
    int m = 10;
    int index[m] = {7, 37, 59, 82, 99, 115, 133, 165, 188, 197};
    for (int i = 0; i < m; i++){
        int u = index[i];
        int d = dist[u];
        printf("%d: %d\n", u, d);
    }

    return 0;
}
