#include "Network.h"

int out[655][655];
int in [655][655];

int indeg[655];
int outdeg[655];

using namespace std;

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
        indeg[i]=(int) indeg[i]/v;
        v=((double) rand())/RAND_MAX;
        outdeg[i]=(int) outdeg[i]/v;
    }
	return net;
}

vector <vector<int> > ERRandom(int N, double p)
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
