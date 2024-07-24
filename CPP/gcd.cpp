#include <iostream>

using namespace std;

int gcd1(int a, int b){
    while(b!=0){
        int rem=a%b;
        a=b;
        b=rem;
    }
    return a;
}

int main(){
    int a=24,b=42;
    cout<<gcd1(a,b);
}