#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int main()
{
    long l,i;
    long double x,n=0,mod=10000000000;
    cin>>l;
    for(i=1;i<=l;i++)
    {
        x=pow(i,i);
        if(x>=mod)
            x=fmod(x,mod);
        cout<<x<<endl;
        n+=x;
    }
    cout<<fmod(n,mod);
    getch();
    return 0;
}
//9110846700
