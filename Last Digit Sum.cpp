#include<iostream>
using namespace std;
int d(int n)
{
    int s=0,c;
    while(n>0)
    {
        c=n%10;
        if(c%2==0)
            s+=c*2;
        else
            s+=c;
        n/=10;
    }
    return s%10;
}
main()
{
    int t,s;
    cin>>t;
    int p[t][2];
    for(int i=0;i<t;i++)
        cin>>p[i][0]>>p[i][1];
    for(int j=0;j<t;j++)
    {
        s=0;
        while(p[j][0]<=p[j][1])
        {
            s+=d(p[j][0]);
            p[j][0]+=1;
        }
        cout<<s<<"\n";
    }
    return 0;
}
