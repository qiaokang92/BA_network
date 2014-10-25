#include <stdio.h>
#include "stdafx.h"
#include "Network.h"
#include <iostream>
#include <algorithm>
#include <iostream>
#include <fstream>
#include "time.h"

using namespace std;

int main()
{
	vector < vector <int> > net;
    net=BAScaleFree(100,2,0.1,2);//ĸֱBAеĽڵN ʼڵm0 Ӹp ÿӸm
    
    for(int i=0; i<100; i++)
    {
        cout << net[0][i] << " ";
    }
    cout << endl;

    Outputfile(net,"BA.txt",2);//D̸Ŀ¼BA磨ڽӶرʽעÿг򶼻Ĩȥ֮ǰtxtµtxt
	
	return 0;
}
