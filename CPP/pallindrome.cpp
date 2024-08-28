#include<iostream>
using namespace std;

int main()
{
   int num=12321, temp,reverse=0,rem;
   temp=num;
   while(temp!=0){
    rem=temp%10;
    reverse=reverse*10 + rem;  
    temp=temp/10; 
   }

   if(num==reverse)
   { 
    cout<<" pallindrome";
   }
   else
   cout<< " not pallindrome";
   return 0;
}