#include<iostream>
using namespace std;
int main(){
    int a=0,b=1,n=7,c;
    cout<<a <<" "<<b<<" ";
    for(int i=2;i<=n;i++){
        c=a+b;
        cout<<" "<<c;
        a=b;
        b=c;
    }
    // cout<< c;
}