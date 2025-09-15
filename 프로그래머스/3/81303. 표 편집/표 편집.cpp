#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

struct node{
    int n;
    node * prev;
    node * next;
    node(int n, node * prev, node * next) : n(n), prev(prev), next(next) {}
};
string solution(int n, int k, vector<string> cmd) {
    string answer(n, 'X');
    int sel = k;
    
    stack<node *> del;
    
    node * header = new node(-1, nullptr, nullptr);
    node * p = header;
    for(int i = 0; i < n; i++){
        p->next = new node(i, p, nullptr);
        p = p->next;
    }
    node * trailer = new node(-1, p, nullptr);
    p->next = trailer;
    
    p = header->next;
    while(k--){
        p = p->next;
    }
    
    for(auto c : cmd){
        if (c[0] == 'C'){
            del.push(p);
            p->prev->next = p->next;
            p->next->prev = p->prev;
            if (p->next == trailer) p = p->prev;
            else p = p->next;
        }
        else if (c[0] == 'Z'){
            node * rec = del.top();
            del.pop();
            rec->prev->next = rec;
            rec->next->prev = rec;
        }
        else{
            int move = stoi(c.substr(2));
            if (c[0] == 'U')
                while(move--)
                    p = p->prev;
            else
                while(move--)
                    p = p->next;
        }
    }
    
    
    for(p = header->next; p != trailer; p = p->next){
        answer[p->n] = 'O';
    }
    
    return answer;
    
}