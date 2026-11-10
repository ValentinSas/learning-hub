#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int main()
{

    cout << "Hello, World!\n";
    cout<< "This project uses the C++17 language standard version \n"; 
    cout<<"Baga un numar de dusmani\n";
    int d;
    cin>>d;
    int a,b;
    a=10; b=20;
    int c=a+b/(a*b);
    cout<<a<<" "<<b<<"\n";
    cout<<c<<"\n";
    cout<<"Ai "<<d<<" dusmani\n"; 
    string str1="Servus";
    long z=str1.length();
    for(long i=0; i<=z; i++)
    {
        if(i==z) {cout<<"!";}
            else {cout<<str1[i]<<" ";}
        
    }
    cout<<"\n";
    cout<<"Baga aici un sir de caractere \n";
    string str2, str3, str4, str5;
    cin>>str2;
    cout<<"Ai bagat sirul: "<<str2<<"\n";
    int x=str2.length();
    cout<<x<<"\n";
    str5=str2;
    str3=str2.append(" Milbei?");
    str4=str5 + " Milbei?";
    if(str3==str4) 
         {
            cout<<"Sirurile sunt egale\n";
            int h=str3.length();
            cout<<h<<" "<<str3<<"\n";
         }
    else {
            cout<<"Sirurile nu sunt egale\n";
            int j=str3.length();
            int l=str4.length();
            cout<<j<<" "<<str3<<"\n";
            cout<<l<<" "<<str4<<"\n";
         }
    cout<<endl;
    return 0;
}