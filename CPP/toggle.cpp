#include<cstring>
#include<iostream>
using namespace std;
#include <string>

int main(){
    string str="helooH";
    for(int i=0;i<str.length();i++){
        if(islower(str[i])){
            str[i]=toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
    }
    cout<< " toggeled text is " << str; return 0;

}