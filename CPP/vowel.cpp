#include<iostream>
using namespace std;

int main(){ 
    char ch='B';
    if(isalpha(ch)){
        if(ch=='a' || ch=='e' || ch=='i' || ch== 'o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U'){
            cout<< ch<< " is vowel";
        }
        else
        cout<< ch << " is consonents";
    }
    else
    cout<< " not an alphabets";
 return 0;
}