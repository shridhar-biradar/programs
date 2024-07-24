#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <climits>

// Class DroneOperation
// Simulates basic drone operations.
class DroneOperation {
public:
    // Simulates drone takeoff.
    virtual void takeoff() {
        std::cout << "Drone is taking off\n";
    }

    // Simulates drone survey operation.
    virtual void survey() {
        std::cout << "Drone is surveying \n";
    }

    // Simulates drone returning to home position.
    virtual void returnToHome() {
        std::cout << "Drone is returning to home\n";
    }

    // Simulates drone landing.
    virtual void land() {
        std::cout << "Drone is landing\n";
    }

    // Simulates failure of drone operation.
    virtual void failure() {
        std::cout << "Drone operation failed\n";
    }
};

// Class MissionPlanning
// Handles mission planning and computation of shortest paths by Dijkstra's Algorithm.
class MissionPlanning {
    int numNodes; // Number of nodes in the graph.
    std::vector<std::vector<std::pair<int, int>>> adjList; // Representation of the graph in terms of an adjacency list.
    std::unordered_map<int, int> prev; // The previous node in path to each node.

public:
    // The constructor that initializes the mission planning graph.
    // Number of nodes in the graph.
    MissionPlanning(int nodes) : numNodes(nodes) {
        adjList.resize(numNodes);
    }

    // Adds an edge to the graph.
    // u Source node.
    // v Destination node.
    // weight Weight of the edge.
    void addEdge(int u, int v, int weight) {
        adjList[u].emplace_back(v, weight);
        adjList[v].emplace_back(u, weight); // Assuming an undirected graph.
    }

    // Implements Dijkstra's Algorithm to find the shortest path from src to dest.
    // src Source node.
    // dest Destination node.
    // Initialize distances to all nodes as infinity, except the source node which is set to 0.
    // Explore nodes with the smallest known distance using a priority queue.
    // Update distances and previous nodes when a shorter path is found.
    // time_complexity O(E log V), where E is the number of edges and V is the number of vertices.
    void dijkstra(int src, int dest) {
        std::vector<int> dist(numNodes, INT_MAX);
        dist[src] = 0;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;
        pq.emplace(0, src);

        while (!pq.empty()) {
            int u = pq.top().second;
            pq.pop();

            for (const auto& neighbor : adjList[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.emplace(dist[v], v);
                    prev[v] = u;
                }
            }
        }
        printPath(src, dest);
    }

    // Prints shortest path from src to dest using prev map.
    // src Source node.
    // dest Destination node.
    void printPath(int src, int dest) {
        if (dest == src) {
            std::cout << src << " ";
            return;
        }
        printPath(src, prev[dest]);
        std::cout << dest << " ";
    }
};

// Class Survey
// Performing route inspection operation.
class Survey {
public:
    // Simulates inspecting the route.
    void inspectRoute() {
        std::cout << "Inspecting the route\n";
    }
};

// Driver function to simulate drone operations, mission planning, and route inspection.
// return int Exit status.
int main() {
    DroneOperation drone;
    MissionPlanning mission(100);
    Survey survey;

    // Simulate the drone operations.
    drone.takeoff();

    // Add edges to the graph.
    // O(V^2) where V is the number of vertices. In this case, V=100.
    for (int i = 0; i < 100; ++i) {
        for (int j = i + 1; j < 100; ++j) {
            mission.addEdge(i, j, rand() % 100);
        }
    }

    int src = 0;
    int dest = 99;

    // This function calculates the shortest path from 'src' to 'dest'.
    mission.dijkstra(src, dest);

    // Simulate route inspection.
    survey.inspectRoute();

    // Simulate returning home, landing.
    drone.returnToHome();
    drone.land();

    return 0;
}
