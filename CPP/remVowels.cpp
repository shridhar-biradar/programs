#include<bits/stdc++.h>
#include<iostream>
#include<cstring>
using namespace std;

string remVowel(string str){
    regex r("[aeoiuAEIOU]");
    return regex_replace(str,r,"");
}
int main(){
    string str="hellodea";
    cout<< remVowel(str);
    return 0;
}