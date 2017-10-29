#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;
int a[30000][30000];
int n=1;
void wide(int x)
{
    int i,j,last=a[x-3][x-3];
    for(i=x-2;i>0;i--)
    {
        for(j=x-2;j>0;j--)
        {
            a[i][j]=a[i-1][j-1];
        }
    }
    for(j=x-2;j>=0;j--)
    {
        a[j][x-1]=last+1;
        last++;
    }
    for(i=x-2;i>=0;i--)
    {
        a[0][i]=last+1;
        last++;
    }
    for(j=1;j<x;j++)
    {
        a[j][0]=last+1;
        last++;
    }
    for(i=1;i<x;i++)
    {
        a[x-1][i]=last+1;
        last++;
    }

}
int prime(int t)
{
    int x=1;
    if(t==1)
        x=0;
    for(int k=2;k<t/2;k++)
    {
        if(t%k==0)
        {
            x=0;
            break;
        }
    }
    return x;
}
int per(int x)
{
    int p=0,b,i;
    b=2*x-1;
    for(i=0;i<x;i++)
    {
        if(prime(a[i][i])!=0)
            p++;
    }
    for(i=0;i<x;i++)
    {
        if(prime(a[x-1-i][i])!=0)
            p++;
    }
    cout<<p<<"/"<<b<<endl;
    return (p*100)/b;
}
int main()
{
    int i,j,pr=100;
    a[0][0]=1;
    while(pr>10)
    {
        n+=2;
        wide(n);
        pr=per(n);
        cout<<n<<" - "<<pr<<"%"<<endl<<endl;
    }
    cout<<n;
    getch();
    return 0;
}
