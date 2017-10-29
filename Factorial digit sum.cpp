#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int main()
{
    long n,f=1,s=0;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        f*=i;
    }
    cout<<f<<endl;
    while(f)
    {
        s+=f%10;
        f/=10;
    }
    cout<<s;
    getch();
    return 0;
}
//666
