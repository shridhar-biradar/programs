#include<iostream>
using namespace std;

bool isLeep(int year){
    if(year%400==0 || year%4==0){
        return true;
    }
    else
    return false;
}
int main(){
    int year=2022;
    if(isLeep(year)){
        cout<< " leep year";
    }
    else
    cout<< " not leep year";
    return 0;
}