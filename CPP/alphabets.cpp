#include<iostream>
#include<cstring>
using namespace std; 

string remove_nonchar(string str){
    string result;
    for(char c:str){
        if(isalpha(c)){
            result +=c;
        }
    }
    return result;
}
int main(){
    string str="snjjhdjsh26365265#@#$%$";
    cout<< remove_nonchar(str);
    return 0;
}