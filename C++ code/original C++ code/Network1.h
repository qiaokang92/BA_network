///////////////////////////////////////////////////////
//network library
//include common network tools and functions
//By Sen Pei at LMIB, BUAA
//////////////////////////////////////////////////////


#ifndef _NETWORK_H
#define _NETWORK_H

#pragma once

#include<time.h>
#include<iomanip>
#include<stdlib.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <ctime>

using namespace std;

int qqq=655
int out[qqq][qqq];
int in [qqq][qqq];
//入度和出度记录
int indeg[qqq];
int outdeg[qqq];
//计算边的值
////////////////////////////////////////////
//input and output
///////////////////////////////////////////

vector < vector <int> > GetIntData_v(string filename);
//Get an integer vector<vector<int>> from a txt file. Result is a vector<vector<int>> type structure.
template <typename T>
int Outputfile(const vector<T> &outputf, string filename, int prec);
//Output a T-vector to a txt file, precision can be adjusted.
template <typename T>
int Outputfile(const vector<vector<T> > &outputf, string filename, int prec);
void Outputfin(string filename,int prec,int N);
void Outputfout(string filename,int prec,int N);
void Opfoutdeg(string filename, int prec,int N);
void Opfindeg(string filename, int prec,int N);
//Output a vector<vector<T>> structure to a txt file, precision can be adjusted.
vector<vector<int> > NetworkData_link_uduw(string filename);
//get the adjacency list of an undirected and unweighted network, data should be the links in the network, the index of nodes begins from 0.

/////////////////////////////////////////
//common used operations
//calculation of network properties
////////////////////////////////////////

vector < vector <int> >  ToSparseMatrix_v(const vector < vector <int> > &a);
//Transform a full matrix to a sparse matrix. Full matrix is stored in a vector<vector<int>> structure, element only 0 or 1.
vector < vector <int> >  MatToLinkvector(const vector < vector <int> > &A);
//transform a full adjacent matrix to adjacency list.
template <typename T>
double sum_array(const vector<T> &vec);
//sum the vector
template <typename T>
double sum_array(const vector<T> &vec, int m, int n);
//sum the vector from m to n
double EdgeCluster( vector<vector<int> > &LV, int m, int n);
//calculate the edge cluster coefficient of the edge connect node m and n. LV is a adjacency list.
vector<int> degree( vector < vector <int> > net);
//get the degree of net

////////////////////////////////////////////
//network generation
///////////////////////////////////////////

vector < vector <int> > ERRandom( int N, double p);
//Create an ER random network with N vertexes. Link probability is p. One need to use srand((unsigned)time(NULL)) in the main function. Result is a adjacency list.
vector < vector <int> > FastERRandom( int N, double p);
//creat an ER random network with N vertexes. Link probability is p. One need to use srand((unsigned)time(NULL)) in the main function. Result is a adjacency list. Add exact N(N-1)p/2 links
vector < vector <int> > BAScaleFree( int N, int m0, double p, int m);
//creat a BA scale free network with  N vertexes. Initial random network vertex m0, probability p, each time add one vertex, link to m existing vertexes. Result is adjacency list. One need to use srand((unsigned)time(NULL)) in the main function.
//int indegree(int N);
//int outdegree(int N);
//计算每条边的值
vector<int> counting_sort_inc(vector<int> sequence);
//counting sort an integer sequence, non-decreasing, stable sorting
vector<int> powerlaw(double gamma, int N, int kmax);
//generate degree sequence containing N integers obeying power law distribution, exponent is gamma, k<=kmax, need to use srand((unsigned)time(NULL)) in the main function.
vector<int> fast_powerlaw(double gamma, int N);
//use transfer function to get powerlaw sequence, size N, exponent gamma
int graphical_check(vector<int> sequence);
//check if a degree sequence is graphical, return 1 if it is graphical, 0 else.
vector < vector <int> > configuration(vector<int> sequence);
//create a network with a given degree sequence, maximal try time can be adjusted, assume the sequence is graphical, maybe unconnected
vector < vector <int> > ExtendedBA(int N, double p, double q, int m0, int m);
//extended BA model, N: node number; p: probability of adding links; q: probability of rewiring; m0: initial isolated nodes; m: operation for each step.
vector < vector <int> > powerlaw_network(int N, double gamma);
//use extended BA model to get network, gamma should between 2 and 3


///////////////////////////////////////////////////
///Connect Component
//////////////////////////////////////////////////

void DFS(const vector<vector<int> > &Lv, vector<int> &visited, int nod, int ccnum);
//deep first search, Lv is adjacency list, L[i] contains the node which is connected to node i. visited is visiting-record, ccnum is the number of connected component.
vector<int> ConnectComp( const vector<vector<int> > &Lv, int nod);
//calculate the connect component in which node nod locates. Lv is adjacency list, L[i] contains the node which is connected to node i. result is the node number vector of the connect component.
int ConnectCompNum( const vector<vector<int> > &Lv);
//calculate the whole connect component number in the network. Lv is adjacency list, L[i] contains the node which is connected to node i.
int maxCCsize( const vector<vector<int> > &Lv);
//return the size of largest connected component
vector < vector <int> > CCvec(const vector<vector<int> > &Lv);
//return the connected component vector



////////////////////////////////////////////
//input and output
///////////////////////////////////////////

vector < vector <int> > GetIntData_v(string filename)
{
	ifstream infile(filename.c_str());
	if (!infile)
	{
		cerr<<"error: unable to open input file."<<endl;
	}
	vector < vector <int> > a;
	istringstream istr;
	string str;
	vector<int> tmpvec;
	while(getline(infile,str))
	{
		istr.str(str);
		int tmp;
		while(istr>>tmp)
		{
			tmpvec.push_back(tmp);
		}
		a.push_back(tmpvec);
		tmpvec.clear();
		istr.clear();
	}
	return a;
}

template <typename T>
int Outputfile(const vector<T> &outputf, string filename, int prec)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;
		return 0;
	}
	for (int i=0; i!=outputf.size(); i++)
	{
		outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<outputf[i]<<"\n";
	}
	outfile.close();
	return 1;
}

template <typename T>
int Outputfile(const vector<vector<T> > &outputf, string filename, int prec)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	int N=outputf.size();
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;
		return 0;
	}
	for (int i=0; i!=outputf.size(); i++)
	{
        outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||";
		for( int j=0; j!=outputf[i].size(); j++)
			outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<outputf[i][j]<<" ";
		outfile<<"\n";
	}
	Outputfin("in.txt",prec,N);
	Outputfout("out.txt",prec,N);
	Opfoutdeg("outdeg.txt",prec,N);
	Opfindeg("indeg.txt",prec,N);
	return 1;
}
void Outputfin(string filename, int prec,int N)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;

	}
	outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<"in:"<<endl;
	for (int i=0; i!=N; i++)
	{
        outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||";
		for( int j=0; j!=N; j++)
            if(in[i][j]==1)
                outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<j<<" ";
		outfile<<"\n";
	}
}
void Outputfout(string filename, int prec,int N)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;

	}
    outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<"out:"<<endl;
	for (int i=0; i!=N; i++)
	{
	    outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||";
		for( int j=0; j!=N; j++)
            if(out[i][j]==1)
                outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<j<<" ";
		outfile<<"\n";
	}

}
void Opfoutdeg(string filename, int prec,int N)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;

	}
    outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<"outdegree:"<<endl;
	for (int i=0; i!=N; i++)
	{
	    if (outdeg[i]!=0)
    	        outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||"<<outdeg[i];
	    else
		outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||";
	    outfile<<"\n";
	}
}
void Opfindeg(string filename, int prec,int N)
{
	ofstream outfile;
	outfile.open(filename.c_str());
	if (!outfile)
	{
		cerr<<"error: unable to open input file."<<endl;

	}
    outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<"indegree:"<<endl;
	for (int i=0; i!=N; i++)
	{
	    if (indeg[i]!=0)
	    	outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||"<<indeg[i];
	    else
		outfile<<setiosflags(ios::scientific)<<setprecision(prec)<<i<<"||";
	    outfile<<"\n";
	}
}



vector <vector <int> > NetworkData_link_uduw(string filename)
{
	vector < vector <int> > net_link=GetIntData_v(filename);
	int maxindex=0;
	for (int i=0; i!=net_link.size(); i++)
		if (maxindex<net_link[i][0]||maxindex<net_link[i][1])
			maxindex=max(net_link[i][0], net_link[i][1]);
	vector < vector <int> > net(maxindex+1);
	for (int i=0; i!=net_link.size(); i++)
	{
		net[net_link[i][0]].push_back(net_link[i][1]);
		net[net_link[i][1]].push_back(net_link[i][0]);
	}
	return net;
}


/////////////////////////////////////////
//common used operations
//calculation of network properties
////////////////////////////////////////

vector < vector <int> > ToSparseMatrix_v(const vector < vector <int> > &a)
{
	vector<vector<int> > sp;
	int N=a.size();
	for (int i=0; i!=N; i++)
		for ( int j=i+1; j!=a[i].size(); j++)
		{
			if (a[i][j])
			{
				vector<int> temp;
				temp.push_back(i);
				temp.push_back(j);
				sp.push_back(temp);
			}
		}
		return sp;
}

vector < vector <int> > MatToLinkvector(const vector < vector <int> > &A)
{
	int N=A.size();
	vector < vector <int > > lv(N);
	for (int i=0; i!=N; i++)
		for (int j=i; j!=N; j++)
		{
			if (A[i][j])
			{
				lv[i].push_back(j);
				lv[j].push_back(i);
			}
		}
		return lv;
}

template <typename T>
double sum_array(const vector<T> &vec)
{
	double sum=0;
	for ( int i=0; i!=vec.size(); i++)
		sum+=vec[i];
	return sum;
}

template <typename T>
double sum_array(const vector<T> &vec, int m, int n)
{
	assert(m<=n);
	assert(n<vec.size());
	double sum=0;
	for ( int i=m; i!=n+1; i++)
		sum+=vec[i];
	return sum;
}

double EdgeCluster( vector<vector<int> > &LV, int m, int n)
{
	double c=0;
	int km=LV[m].size(),kn=LV[n].size();
	for ( int i=0; i!=km; i++)
		for ( int j=0; j!=kn; j++)
			if (LV[m][i]==LV[n][j])
				c+=1;
	c=(c+1)/(km<kn?km-1:kn-1);
	return c;
}

vector <int> degree( vector < vector <int> > net)
{
	vector<int> deg(net.size());
	for (int i=0; i!=net.size(); i++)
		deg[i]=net[i].size();
	return deg;
}

////////////////////////////////////////////
//network generation
///////////////////////////////////////////


vector<vector<int> > ERRandom(int N, double p)
{
	assert(p>=0&&p<=1);
	vector < vector <int> > er(N);
	for ( int i=0; i!=N; i++)
	{
	    for ( int j=i+1; j!=N; j++)
		{
			double v=((double) rand())/RAND_MAX;
			if (v>=0&&v<=p)
			{
				er[i].push_back(j);
				er[j].push_back(i);
				out[i][j]=1;
				in[j][i]=1;
			}
		}
	}

    return er;
}

vector<vector<int> > FastERRandom( int N, double p)
{
	vector < vector <int> > ER(N);
	int link=N*p*(N-1)/2;
	for (int i=0; i!=link; i++)
	{
		int existlink=0,  flag=0;//if flag=0, fail to add link; else, succeed to add link
		while (flag!=1)
		{
			int node1=(rand()*RAND_MAX+rand())%N, node2=(rand()*RAND_MAX+rand())%N;
			existlink=0;
			flag=0;
			for (int j=0; j!=ER[node1].size(); j++)//check if there exists a link already
			{
				if (ER[node1][j]==node2)
				{
					existlink=1;
					break;
				}
			}
			if (existlink!=1&&node1!=node2)
			{
				ER[node1].push_back(node2);
				ER[node2].push_back(node1);
				flag=1;
			}
		}
	}
	return ER;
}

vector < vector <int> > BAScaleFree( int N, int m0, double p, int m)
{
	assert(p>=0&&p<=1);
	assert(m<=m0);
	vector < vector <int> > net=ERRandom(m0,p);
	vector<int> deg;
	vector<int> criterion;
	for (int i=0; i!=net.size(); i++)
	{
		deg.push_back(net[i].size());
		for (int j=0; j!=net[i].size(); j++)
			criterion.push_back(i);
	}
	while (net.size()<N)
	{
		double v=(double)rand()/RAND_MAX;
		vector<int> temp;
		net.push_back(temp);
		int addlink=0, node1=net.size()-1;
		while (addlink<m)
		{
			int islink=0;
			int node2=criterion[(rand()*RAND_MAX+rand())%criterion.size()];
			for (int i=0; i!=net[node1].size(); i++)
			{
				if (net[node1][i]==node2)
				{
					islink=1;
					out[node1][node2]=1;
					in[node2][node1]=1;
                    outdeg[node1]+=1;
                    indeg[node2]+=1;
					break;
				}
			}
			if (islink==0)
			{
			    double v=((double)rand())/RAND_MAX;
			    if (v>0.5)
			    {
			        net[node1].push_back(node2);
                    net[node2].push_back(node1);
                    out[node1][node2]=1;
                    in[node2][node1]=1;
                    outdeg[node1]+=1;
                    indeg[node2]+=1;
                    deg[node2]++;
                    criterion.push_back(node2);
                    addlink++;
			    }
				else
				{
                    net[node2].push_back(node1);
                    net[node1].push_back(node2);
                    out[node2][node1]=1;
                    in[node1][node2]=1;
                    outdeg[node2]+=1;
                    indeg[node1]+=1;
                    deg[node2]++;
                    criterion.push_back(node2);
                    addlink++;
				}
			}
		}
		deg.push_back(m);
		for (int i=0; i!=m+1; i++)
			criterion.push_back(node1);
	}
    for (int i=0;i<N;i++)
    {
        double v=((double) rand())/RAND_MAX;
	if (indeg[i]!=0)
		indeg[i]=(int) v/indeg[i];
        v=((double) rand())/RAND_MAX;
	if (outdeg[i]!=0)
        	outdeg[i]=(int) v/outdeg[i];
    }
	return net;
}

/*int indegree(int N)
{
    for (int i=0;i<N;i++)
    {
        int a=0;
        for (int j=0;j<N;j++)
        {
            if (in[i][j]==1)
                a+=1;
        }
        double v=(double) rand()/RAND_MAX;
        a=(int) v/a;
        indeg[i]=a;
    }
    return 1;
}
int outdegree(int N)
{
    for (int i=0;i<N;i++)
    {
        int a=0;
        for (int j=0;j<N;j++)
        {
            if (out[i][j]==1)
                a+=1;
        }
        double v=(double) rand()/RAND_MAX;
        a=(int) v/a;
        outdeg[i]=a;
    }
    return 1;
}*/
vector<int> counting_sort_inc(vector<int> sequence)
{
	vector<int> sorted_seq(sequence.size());
	int kmax=0;
	for (int i=0; i!=sequence.size(); i++)
		if ( kmax<sequence[i])
			kmax=sequence[i];
	vector<int> C(kmax);
	for (int i=0; i!=sequence.size(); i++)
		C[sequence[i]-1]++;
	for (int i=1; i!=kmax; i++)
		C[i]=C[i]+C[i-1];
	for (int i=sequence.size()-1; i>=0; i--)
	{
		sorted_seq[C[sequence[i]-1]-1]=sequence[i];
		C[sequence[i]-1]--;
	}
	return sorted_seq;
}

vector<int> powerlaw(double gamma, int N, int kmax)
{
	vector<double> criterion;
	vector<int> sequence;
	double temp=0;
	criterion.push_back(temp);
	for ( int i=0; i!=kmax; i++)
	{
		temp=temp+pow(i+1,-gamma);
		criterion.push_back(temp);
	}
	for (int i=0; i!=criterion.size(); i++)
		criterion[i]=criterion[i]/temp;
	for ( int i=0; i!=N; i++)
	{
		double v=(double)rand()/RAND_MAX;
		int num=1;
		for ( int j=0; j!=criterion.size()-1; j++)
			if (v>=criterion[j]&&v<criterion[j+1])
			{
				num=j+1;
				break;
			}
			sequence.push_back(num);
	}
	return sequence;
}

vector<int> fast_powerlaw(double gamma, int N)
{
	vector<int> sequence;
	for ( int i=0; i!=N; i++)
	{
		int temp=0;
		while (temp<=0)
		{
			double v=(double)rand()/RAND_MAX;
			temp=floor(pow(v,1/(1-gamma)));
		}
		sequence.push_back(temp);
	}
	return sequence;
}

int graphical_check(vector<int> sequence)
{
	int N=sequence.size();
	//check if sum sequence is even
	int sum=0;
	for (int i=0; i!=N; i++)
		sum+=sequence[i];
	if (sum%2==1)
		return 0;
	else
	{
		//counting sort, non-increasing
		vector<int> sort_inc,d(N);
		sort_inc=counting_sort_inc(sequence);
		for (int i=0; i!=N; i++)
			d[i]=sort_inc[N-1-i];
		//computing L sequence
		vector<int> Lseq(N);
		Lseq[0]=d[0];
		for (int i=1; i!=N; i++)
			Lseq[i]=Lseq[i-1]+d[i];
		//computing R sequence
		vector<int> x(N), Rseq(N);
		for (int i=0; i!=N; i++)
			x[i]=N-1;
		for (int i=0; i!=N; i++)
		{
			for (int j=0; j!=N; j++)
			{
				if (d[j]<i+1)
				{
					x[i]=j;
					break;
				}
			}
		}
		int kstar;
		for (int i=0; i!=N; i++)
		{
			if (x[i]<i+1)
			{
				kstar=i;
				break;
			}
		}
		Rseq[0]=N-1;
		for (int i=1; i!=N; i++)
		{
			if (i<kstar)
				Rseq[i]=Rseq[i-1]+x[i]-1;
			else
				Rseq[i]=Rseq[i-1]+2*i-d[i];
		}
		int flag=1;
		for (int i=0; i!=N-1; i++)
		{
			if (Lseq[i]>Rseq[i])
			{
				flag=0;
				break;
			}
		}
		return flag;
	}
}

vector < vector <int> > configuration(vector<int> sequence)
{
	int N=sequence.size();
	int maxtrytime=N*10;
	vector<int> Lset;
	for (int i=0; i!=N; i++)
		for (int j=0; j!=sequence[i]; j++)
			Lset.push_back(i);
	int ksum=Lset.size();
	vector < vector <int> > net(N);
	vector<int> state(N);//state 0: unexposed; state 1: partially exposed or entirely exposed
	vector<int>::iterator iter=Lset.begin();
	vector<int> pexposed;
	vector<int>::iterator iter1=pexposed.begin();
	int penum=pexposed.size();
	//
	int node1=0, node2=0, v1=0, v2=0;
	int trytime=0;
	while((ksum!=0)&&(trytime<=maxtrytime))
	{
		trytime++;
		v1=(rand()*RAND_MAX+rand())%ksum;
		v2=(rand()*RAND_MAX+rand())%ksum;
		node1=Lset[v1];
		node2=Lset[v2];
		if (node1==node2)
		{
			continue;
		}
		else
		{
			net[node1].push_back(node2);
			net[node2].push_back(node1);
			state[node1]=1;
			state[node2]=1;
			//remove node1 and node2 from Lset
			iter=Lset.begin();
			Lset.erase(iter+max(v1,v2));
			iter=Lset.begin();
			Lset.erase(iter+min(v1,v2));
			ksum=ksum-2;
			//add node1 and node2 to partially exposed set
			for (int i=0; i!=sequence[node1]-1; i++)
				pexposed.push_back(node1);
			for (int i=0; i!=sequence[node2]-1; i++)
				pexposed.push_back(node2);
			penum=pexposed.size();
			//
			int trytime1=0;
			while (penum!=0&&trytime1<=maxtrytime)
			{
				trytime++;
				v1=(rand()*RAND_MAX+rand())%penum;
				node1=pexposed[v1];
				v2=(rand()*RAND_MAX+rand())%ksum;
				node2=Lset[v2];
				//check if there exist a link
				int islinked=0;
				for (int i=0; i!=net[node1].size(); i++)
				{
					if (net[node1][i]==node2)
					{
						islinked=1;
						break;
					}
				}
				if (islinked==0&&node1!=node2)
				{
					net[node1].push_back(node2);
					net[node2].push_back(node1);
					//remove node1 and node2 from Lset
					iter=Lset.begin();
					Lset.erase(iter+v2);
					ksum--;
					for (int i=0; i!=ksum; i++)
					{
						if (Lset[i]==node1)
						{
							iter=Lset.begin();
							Lset.erase(iter+i);
							ksum--;
							break;
						}
					}
					//remove node1 from pexposed, check state of node2
					iter1=pexposed.begin();
					pexposed.erase(iter1+v1);
					penum--;
					if (state[node2]==0)//add node2 to pexposed
					{
						for (int i=0; i!=sequence[node2]-1; i++)
							pexposed.push_back(node2);
						penum=penum+sequence[node2]-1;
						state[node2]=1;
					}
					else//node2 is in pexposed, remove it
					{
						for (int i=0; i!=penum; i++)
						{
							if (pexposed[i]==node2)
							{
								iter1=pexposed.begin();
								pexposed.erase(iter1+i);
								penum--;
								break;
							}
						}
					}
				}
			}
			if (trytime>=maxtrytime)
			{
				net.clear();
				cout<<"cannot construct network, try again!"<<endl;
				return net;
			}
		}
	}
	if (trytime>=maxtrytime)
	{
		net.clear();
		cout<<"cannot construct network, try again!"<<endl;
		return net;
	}
	return net;
}

vector < vector <int> > ExtendedBA(int N, double p, double q, int m0, int m)
{
	assert(p>=0&&q>=0&&p+q<1&&m<=m0);
	vector < vector <int> > net(m0);
	vector <int> criterion;
	for ( int i=0; i!=m0; i++)
		criterion.push_back(i);
	double v=0;
	int node1=0, node2=0, newnode2=0;
	while (net.size()<N)
	{
		v=(double)rand()/RAND_MAX;
		if (v<p)
		{
			int addlink=0;
			while (addlink<m)
			{
				node1=(rand()*RAND_MAX+rand())%net.size();
				node2=criterion[(rand()*RAND_MAX+rand())%criterion.size()];
				int islink=0;
				for (int i=0; i!=net[node1].size(); i++)
				{
					if ( net[node1][i]==node2)
					{
						islink=1;
						break;
					}
				}
				if (node1!=node2&&islink==0)
				{
					net[node1].push_back(node2);
					net[node2].push_back(node1);
					criterion.push_back(node1);
					criterion.push_back(node2);
					addlink++;
				}
			}
		}
		else if (v<p+q)
		{
			int rewire=0;
			while (rewire<m&&net.size()>m0)
			{
				node1=(rand()*RAND_MAX+rand())%net.size();
				if (net[node1].size()>0)
				{
					node2=net[node1][(rand()*RAND_MAX+rand())%net[node1].size()];
					newnode2=criterion[(rand()*RAND_MAX+rand())%criterion.size()];
					int islink=0;
					for (int i=0; i!=net[node1].size(); i++)
					{
						if (net[node1][i]==newnode2)
						{
							islink=1;
							break;
						}
					}
					if (node2==newnode2)
					{
						rewire++;
					}
					else if (islink==0)
					{
						for (int i=0; i!=net[node1].size(); i++)
						{
							if (net[node1][i]==node2)
							{
								net[node1][i]=newnode2;
								break;
							}
						}
						vector<int>::iterator iter=net[node2].begin();
						for (int i=0; i!=net[node2].size(); i++)
						{
							if (net[node2][i]==node1)
							{
								iter=net[node2].begin();
								net[node2].erase(iter+i);
								break;
							}
						}
						net[newnode2].push_back(node1);
						for (int i=0; i!=criterion.size(); i++)
						{
							if (criterion[i]==node2)
							{
								criterion[i]=newnode2;
								break;
							}
						}
						rewire++;
					}
				}
			}
		}
		else
		{
			vector<int> temp;
			net.push_back(temp);
			node1=net.size()-1;
			int addlink=0;
			while (addlink<m)
			{
				node2=criterion[(rand()*RAND_MAX+rand())%criterion.size()];
				int islink=0;
				for ( int i=0; i!=net[node1].size(); i++)
				{
					if (net[node1][i]==node2)
					{
						islink=1;
						break;
					}
				}
				if ( islink==0)
				{
					net[node1].push_back(node2);
					net[node2].push_back(node1);
					criterion.push_back(node2);
					addlink++;
				}
			}
			for (int i=0; i!=m+1; i++)
				criterion.push_back(node1);
		}
	}
	return net;
}

vector < vector <int> > powerlaw_network(int N, double gamma)
{
	int m=2, m0=50;
	assert(gamma>=2&&gamma<=3);
	double K=(double)(3-gamma)/(gamma-1);
	double p=2*m*K/((1+K)*(1-K+2*m)), q=1-(2*m/((1+K)*(1-K+2*m)));
	vector < vector <int> > net;
	net=ExtendedBA(N,p,q,m0,m);
	return net;
}

///////////////////////////////////////////////////
///Connect Component
//////////////////////////////////////////////////

void DFS(const vector<vector<int> > &Lv, vector<int> &visited, int nod, int ccnum)
{
	visited[nod]=ccnum;
	for ( int i=0; i!=Lv[nod].size(); i++)
		if (visited[Lv[nod][i]]==0)
			DFS(Lv, visited,Lv[nod][i], ccnum);
}

vector<int> ConnectComp( const vector<vector<int> > &Lv, int nod)
{
	int N=Lv.size(), ccnum=1;
	vector<int> visited(N,0);
	DFS(Lv, visited, nod, ccnum);
	vector<int> CC;
	for (int i=0; i!=N; i++)
		if (visited[i])
			CC.push_back(i);
	return CC;
}

int ConnectCompNum( const vector<vector<int> > &Lv)
{
	int N=Lv.size(), ccnum=0;
	vector<int> visited(N,0);
	for ( int i=0; i!=N; i++)
		if ( visited[i]==0)
		{
			ccnum++;
			DFS(Lv,visited,i,ccnum);
		}
		return ccnum;
}

int maxCCsize( const vector<vector<int> > &Lv)
{
	int N=Lv.size();
	vector<int> state(N),ccsize;
	for (int i=0; i!=N; i++)
	{
		if (state[i]==0)
		{
			vector<int> tempcc=ConnectComp(Lv,i);
			for (int j=0; j!=tempcc.size(); j++)
				state[tempcc[j]]=1;
			ccsize.push_back(tempcc.size());
		}
	}
	int maxsize=0;
	for (int i=0; i!=ccsize.size(); i++)
		if (maxsize<ccsize[i])
			maxsize=ccsize[i];
	return maxsize;
}

vector < vector <int> > CCvec(const vector < vector<int> > &Lv)
{
	int N=Lv.size(), ccnum=0;
	vector<int> state(N);
	vector < vector <int> > ccvec;
	for (int i=0; i!=N; i++)
	{
		if (state[i]==0)
		{
			vector<int> tempcc=ConnectComp(Lv,i);
			vector<int> temp;
			ccvec.push_back(temp);
			for (int j=0; j!=tempcc.size(); j++)
			{
				state[tempcc[j]]=1;
				ccvec[ccnum].push_back(tempcc[j]);
			}
			ccnum++;
		}
	}
	return ccvec;
}

#endif
