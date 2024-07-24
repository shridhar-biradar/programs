// C++ program to
// Find LCM of two numbers
#include <iostream>
using namespace std;

 int gcd(  int a,   int b)
{
    if (b == 0)
        return a;
    return gcd( b,a % b);
}

// Function to return LCM of two numbers
 int lcm(int a, int b)
{
    int  result = (a / gcd(a, b)) * b;
    return result;
}

int main()
{
    int a = 24, b = 12;
    cout << "LCM : " << lcm(a, b);
    return 0;
}
