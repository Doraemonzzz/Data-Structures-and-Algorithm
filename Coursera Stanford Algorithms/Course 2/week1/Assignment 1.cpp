#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

const int N = 1e6;

//����ͼ
vector <int> G[N], Grev[N];
//�ж��Ƿ���ʹ�
int flag[N];
//leader����
int leader[N];
//����ʱ��
int finish[N];
//����ʱ��->�ڵ���
int Index[N];
//leader
int s;
//����ʱ��
int t;
//�ڵ�����
int n = 1;

bool cmp(int a, int b){
    return a > b;
}

//���������������һ�֣�
void DFS_v1(vector <int> Graph[], int i){
    //��ʼ��ջ
    stack <int> Q;
    Q.push(i);
    flag[i] = 1;
    //��¼˳��
    vector <int> tmp;
    while (!Q.empty()){
        int u = Q.top();
        Q.pop();
        leader[u] = s;
        //�洢���
        tmp.push_back(u);
        //���
        for (int k = 0; k < Graph[u].size(); k++){
            int v = Graph[u][k];
            if (flag[v] == 0){
                flag[v] = 1;
                Q.push(v);
            }
        }
    }
    //����finish, Index;
    for (int j = tmp.size() - 1; j >= 0; j--){
        int u = tmp[j];
        t++;
        finish[u] = t;
        Index[t] = u;
    }
}

//��������������ڶ��֣�
void DFS_v2(vector <int> Graph[], int i, int& cnt){
    //��ʼ��ջ
    stack <int> Q;
    Q.push(i);
    flag[i] = 1;
    while (!Q.empty()){
        int u = Q.top();
        Q.pop();
        //���
        for (int k = 0; k < Graph[u].size(); k++){
            int v = Graph[u][k];
            if (flag[v] == 0){
                flag[v] = 1;
                Q.push(v);
            }
        }
        //���¼���
        cnt++;
    }
}

//�ݹ�汾
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
//    //��¼ʱ��������Ĺ�ϵ
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
    //����
    //�ļ���
    char filename[] = "SCC.txt";
    freopen(filename, "r", stdin);
    //��¼�ڵ�����
    int u, v;
    while (scanf("%d %d", &u, &v) != EOF){
        n = max(n, u);
        n = max(n, v);
        G[u].push_back(v);
        Grev[v].push_back(u);
    }

    //��һ��
    //��ʼ��
    memset(flag, 0, sizeof(flag));
    t = 0;
    for (int i = n; i >= 1; i--){
        if (flag[i] == 0){
            //����leader
            s = i;
            DFS_v1(Grev, i);
        }
    }

    //�ڶ���
    memset(flag, 0, sizeof(flag));
    //��¼SCC��Ԫ������
    vector <int> res;
    for (int k = n; k >= 1; k--){
        int i = Index[k];
        int cnt = 0;
        if (flag[i] == 0){
            DFS_v2(G, i, cnt);
            res.push_back(cnt);
        }
    }

    //����
    sort(res.begin(), res.end(), cmp);
    //���
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
