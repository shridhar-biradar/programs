#include<iostream>
using namespace std;

int main(){ 
   
   int num=153, temp, rem, reverse=0;
   temp=num;
   while(temp!=0){
    rem=temp%10;
    reverse=reverse+(rem*rem*rem);
    temp=temp/10;
   }
   if(num==reverse){
    cout<<" Armstrong num ";
   }
   else
   cout<<" not Armstrong";
   
}