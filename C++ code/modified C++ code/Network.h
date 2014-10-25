///////////////////////////////////////////////////////
//network library
//include common network tools and functions
//By Sen Pei at LMIB, BUAA
//////////////////////////////////////////////////////


#ifndef _NETWORK_H
#define _NETWORK_H

//#pragma once

#include<time.h>
#include<stdlib.h>
#include<iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <ctime>

using namespace std;

vector < vector <int> > BAScaleFree( int N, int m0, double p, int m);
vector < vector <int> > ERRandom( int N, double p);

#endif