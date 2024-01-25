#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <fstream>
#include <sstream>
#include <functional>

using namespace std;

struct Node
{
    int y, x;           // Pozycje wêz³a na mapie
    int g_cost, h_cost; // Koszt dotarcia i heurystyka
    Node *parent;       // WskaŸnik do wêz³a rodzica

    Node(int y, int x, int g_cost = 0, int h_cost = 0, Node *parent = nullptr)
        : y(y), x(x), g_cost(g_cost), h_cost(h_cost), parent(parent) {}

    int f_cost() const
    {
        return g_cost + h_cost;
    }

    bool operator==(const Node &other) const // Porównanie kosztu kolejki
    {
        return y == other.y && x == other.x;
    }
};

// Funkcja Heurystyki (Odleg³oœæ Euklidesowa)
int heuristic(int y1, int x1, int y2, int x2)
{
    return static_cast<int>(sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)));
}

// Sprawdzenie, czy punkt jest w granicach mapy i nie jest przeszkod¹
bool isValidPoint(int y, int x, const vector<vector<int>> &grid)
{
    return y >= 0 && y < grid.size() && x >= 0 && x < grid[0].size() && grid[y][x] != 5;
}

// Implementacja algorytmu A*
void AStarSearch(vector<vector<int>> &grid, Node start, Node goal)
{
    if (!isValidPoint(start.y, start.x, grid) || !isValidPoint(goal.y, goal.x, grid))
    {
        cout << "Invalid start or goal position." << endl;
        return;
    }

    const int rows = grid.size();
    const int cols = grid[0].size();

    auto compare = [](const Node *a, const Node *b)
    {
        return a->f_cost() > b->f_cost();
    };

    priority_queue<Node *, vector<Node *>, decltype(compare)> openSet(compare);
    vector<vector<bool>> closedSet(rows, vector<bool>(cols, false));

    openSet.push(new Node(start));

    while (!openSet.empty())
    {
        Node *current = openSet.top();
        openSet.pop();

        if (*current == goal)
        {
            // Odtwarzanie œcie¿ki
            Node *temp = current;
            while (temp != nullptr)
            {
                if (temp->y >= 0 && temp->y < rows && temp->x >= 0 && temp->x < cols)
                {
                    grid[temp->y][temp->x] = 3;
                }
                temp = temp->parent;
            }

            // Zwolnienie pamiêci zajêtej przez wêz³y
            while (!openSet.empty())
            {
                delete openSet.top();
                openSet.pop();
            }

            return;
        }

        closedSet[current->y][current->x] = true;

        // Sprawdzanie s¹siadów
        const int dy[] = {-1, 1, 0, 0};
        const int dx[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; ++i)
        {
            int newY = current->y + dy[i];
            int newX = current->x + dx[i];

            if (isValidPoint(newY, newX, grid) && !closedSet[newY][newX])
            {
                int newGCost = current->g_cost + 1; // Koszt ruchu do s¹siada

                Node *neighbor = new Node(newY, newX, newGCost, heuristic(newY, newX, goal.y, goal.x), current);

                if (!closedSet[neighbor->y][neighbor->x])
                {
                    openSet.push(neighbor);
                }
            }
        }
    }

    // Zwolnienie pamiêci zajêtej przez wêz³y
    while (!openSet.empty())
    {
        delete openSet.top();
        openSet.pop();
    }

    cout << "No path found." << endl;
}

vector<vector<int>> loadMapFromFile(const string &filename)
{
    vector<vector<int>> map;
    ifstream file(filename);
    string line;

    while (getline(file, line))
    {
        stringstream ss(line);
        vector<int> row;
        int value;
        while (ss >> value)
        {
            row.push_back(value);
        }
        map.push_back(row);
    }

    return map;
}

int main()
{
    vector<vector<int>> mapFromFile = loadMapFromFile("grid.txt");
    Node start(10, 10);
    Node goal(19,19);

    for (const auto &row : mapFromFile)
    {
        for (int cell : row)
        {
            cout << cell << " ";
        }
        cout << endl;
    }
    cout << endl;
    cout << endl;

    AStarSearch(mapFromFile, start, goal);

    for (const auto &row : mapFromFile)
    {
        for (int cell : row)
        {
            cout << cell << " ";
        }
        cout << endl;
    }

    return 0;
}
