#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int main()
{
    double x;
    int d,sum=0;
    x = pow(2,1000);
    while (x>0){
        d = int(fmod(x,10));
        sum+= d;
        x = x / 10;
    }
    cout<<sum;
    getch();
    return 0;
}
//
