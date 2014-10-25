#include <stdio.h>
#include "Network.h"
#include <iostream>
#include <algorithm>
#include <iostream>
#include <fstream>
#include "time.h"
#include <vector>

using namespace std;

int main()
{
    int i;
    vector < vector <int> > net;
    net=BAScaleFree(100,2,0.1,2);
    
    //Outputfile(net,"BA.txt",2);

    //for (int i=0; i<100; i++)
    {
        cout << i << "="  << net[1][1] << " "; 
    }
 
    return 0;
}
