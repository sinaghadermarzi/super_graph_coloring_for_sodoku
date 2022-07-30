// Super_Graph_Coloring.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <string>


// A C++ program to implement greedy algorithm for graph coloring
#include <iostream>
#include <list>
using namespace std;

// A class that represents an undirected graph
class Graph
{
	int V;    // No. of vertices
	list<int> *adj;    // A dynamic array of adjacency lists
public: int* current_colors;

public: int next_color;
public:
	// Constructor and destructor
	Graph(int V) { this->V = V; adj = new list<int>[V]; current_colors = new int[V]; next_color = 0; }
	~Graph() { delete[] adj; }

	// function to add an edge to graph
	void addEdge(int v, int w);

	// Prints greedy coloring of the vertices
	void greedyColoring();
};

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v);  // Note: the graph is undirected
}

// Assigns colors (starting from 0) to all vertices and prints
// the assignment of colors
void Graph::greedyColoring()
{
	int begining_next_color = next_color;
	// Assign the first color to first vertex
	bool found;
	int i;
	bool *used_by_neighbours;
	used_by_neighbours = new bool[V];

	for (int cr = 0; cr < V; cr++)
		used_by_neighbours[cr] = false;

	// Assign colors to remaining V-1 vertices
	for (int u = 0; u < V; u++)
	{
		if (current_colors[u] == -1)
		{
			// Process all adjacent vertices and flag their colors
			// as unavailable
			list<int>::iterator i;
			for (i = adj[u].begin(); i != adj[u].end(); ++i)
				if (current_colors[*i] != -1)
					used_by_neighbours[current_colors[*i]] = true;

			// Find the first available color
			found = false;
			int cr;
			for (cr = 0; cr < next_color; cr++)
				if (used_by_neighbours[cr] == false)
				{
					found = true;
					break;
				}
			if (!found)
			{
				current_colors[u] = next_color;
				next_color++;
			}
			else
			{
				current_colors[u] = cr; // Assign the found color
			}



			// Reset the values back to false for the next iteration
			for (i = adj[u].begin(); i != adj[u].end(); ++i)
				if (current_colors[*i] != -1)
					used_by_neighbours[current_colors[*i]] = false;

		}
	}

	// print the result
	int extra_colors_used = next_color - begining_next_color;
	cout << extra_colors_used <<endl;
	for (int u = 0; u < V; u++)
		cout <<(current_colors[u]+1) << " ";
	cout<<endl;
}

// Driver program to test above function
int main()
{
	std::string str;
	int v1, v2;
	int num_vertex, num_edge;
	std::list<int> colors;
	Graph *g1;
	if (!(cin >> num_vertex >> num_edge)){
		cerr << "Problem with input file! couldn't successfuly parse graph size from first line";
		getchar();
		return 1;
	}
	g1 = new Graph(num_vertex);
	for (int i = 0; i < num_edge; i++)
	{
		if (!(cin >> v1 >> v2)) {
			cerr << "Problem with input file! couldn't successfuly parse all the edges";
			getchar();
			return 1;
		}
		else
		{
			g1->addEdge(v1-1, v2-1);
		}
	}
	
	for (int u = 0; u < num_vertex; u++)
	{
		int col;
		cin >> col;
		col--;
		g1->current_colors[u] = col;
		if ((col+1) > g1->next_color)
			g1->next_color = col+1;
		
	}
	g1->greedyColoring();
	return 0;
}




