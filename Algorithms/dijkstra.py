import time  
from pyamaze import maze, agent, textLabel  
from queue import PriorityQueue  

def dijkstra(m):  
    start_time = time.time()  
    start = (m.rows, m.cols)   
    distance = {cell: float('inf') for cell in m.grid}  
    distance[start] = 0  
    pq = PriorityQueue()  
    pq.put((0, start))  
    dPath = {}  
    visited = []  

    while not pq.empty():  
        currDist, currCell = pq.get()  
        visited.append(currCell)  

        if currCell == (1, 1):   
            break  

        for d in 'ESNW':  
            if m.maze_map[currCell][d]:  
                if d == 'E': childCell = (currCell[0], currCell[1] + 1)  
                if d == 'W': childCell = (currCell[0], currCell[1] - 1)  
                if d == 'N': childCell = (currCell[0] - 1, currCell[1])  
                if d == 'S': childCell = (currCell[0] + 1, currCell[1])  

                newDist = distance[currCell] + 1  

                if newDist < distance[childCell]:  
                    distance[childCell] = newDist  
                    pq.put((newDist, childCell))  
                    dPath[childCell] = currCell  

    fwdPath = {}  
    cell = (1, 1)  
    while cell != start:  
        fwdPath[dPath[cell]] = cell  
        cell = dPath[cell]  

    end_time = time.time()  
    return fwdPath, round(end_time - start_time, 8), visited  

rows=int(input("Enter number of rows in maze: "))
columns=int(input("Enter number of columns in maze: "))
m = maze(rows,columns)  

if __name__ == "__main__":  
    m.CreateMaze()  
    root = m._canvas.winfo_toplevel()  
    root.title("Maze Master by Piyush Naula")  
 
    path_dijkstra, time_dijkstra, visited_dijkstra = dijkstra(m)  

    backtrack_dijkstra = agent(m, footprints=True, color='yellow', filled=False)  
    m.tracePath({backtrack_dijkstra: visited_dijkstra}, delay=100)  

    d = agent(m, footprints=True, color='blue')  
    m.tracePath({d: path_dijkstra}, delay=50)  

    textLabel(m, 'Dijkstra Path Length', len(path_dijkstra) + 1)  
    textLabel(m, 'Dijkstra Time (s)', time_dijkstra)  

    print(m.maze_map)  
    print(f"Dijkstra Algorithm Time: {time_dijkstra} seconds")  

    m.run()