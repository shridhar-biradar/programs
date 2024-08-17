#include<iostream>
using namespace std;

int sum(int num){

    int result=0;
    for(int i=0;i<=num;i++){
        result+=i;
    }return result;
}

int main(){  
    int num=7;
    cout<< sum(num);
    return 0;
}