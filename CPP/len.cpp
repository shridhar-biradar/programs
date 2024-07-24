#include<iostream>
#include<cstring>
using namespace std;

 int main(){
    string str1="hello world";
    int length=0;
    for( int i=0; str1[i]!='\0';i++){
        length++;

    }
    cout<<" length of string is: "<< length;
    return 0;

 }