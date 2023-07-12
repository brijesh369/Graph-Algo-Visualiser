# Graph-Algo-Visualiser
The project is a web-based graph algorithms visualizer that allows users to interactively observe the working of three different graph algorithms: Dijkstra's Algorithm, Floyd-Warshall Algorithm, and Prim's Algorithm.

The visualizer is implemented using HTML, CSS, and JavaScript. It consists of three sections, each dedicated to one of the algorithms. In each section, there is a canvas where the graph and algorithm visualization are displayed, along with buttons for generating a random graph and running the respective algorithm.

Here is a summary of each algorithm and its functionality:

1. Dijkstra's Algorithm:
   - Generates a random graph with nodes and edges.
   - Uses Dijkstra's algorithm to find the shortest path from a source node to all other nodes in the graph.
   - The visualization shows the process step by step, highlighting the visited nodes and edges.
   - After running the algorithm, it displays the shortest path from the source node to each node in the result section.

2. Floyd-Warshall Algorithm:
   - Generates a random graph with nodes and edges.
   - Applies the Floyd-Warshall algorithm to find the shortest path between all pairs of nodes in the graph.
   - The visualization displays the intermediate steps of the algorithm, updating the canvas to show the progress.
   - After running the algorithm, it shows the shortest paths and their weights for all pairs of nodes in the result section.

3. Prim's Algorithm:
   - Generates a random graph with nodes and edges.
   - Executes Prim's algorithm to find the minimum spanning tree of the graph.
   - The visualization highlights the visited edges, gradually growing the minimum spanning tree.
   - After running the algorithm, it displays the visited edges that form the minimum spanning tree in the result section.

Overall, the project provides an interactive way to understand and visualize the working of these graph algorithms, allowing users to gain insights into their behavior and results.
