#include<iostream>
using namespace std;
 bool isEven(int n){
    return(n%2==0);
 }
 int main(){
    int n=34;
    if(isEven(n)==true){
        cout<< n<< "is even ";
    }
    else
    cout<< n<<" is odd";
    return 0;
 }