import math
import heapq

global cross_roads, list_of_roads, total_path, h_value, path_cost

cross_roads = {}     # cross_roads here is intersections property of Map represented as dictionary
list_of_roads = []   # list_of_roads is roads property of Map represented as list
total_path = []       # possible path
h_value = {}         # calculate heuristic value and store it in h_value

# Typical implementations of A* use a priority queue to perform
# the repeated selection of minimum (estimated) cost nodes to expand.
# using Python's built-in function heap for priority queue

def shortest_path(M, start, goal, default_msg=True):
    # print("shortest path called")
    # return
    
    global cross_roads, list_of_roads, total_path, h_value, path_cost
    h_value = {}
    cross_roads = M.intersections
    list_of_roads = M.roads

    frontier_set = set()
    frontier_set.add(start)
    
    explored_set = set()   
    
    heap = []
    path_cost = 0
    total_path_cost = 0
    
    heapq.heappush(heap, (path_cost, start, total_path_cost))
    
    prev_path = {}
    
    h_value[start] = euclidean_distance(start, goal)
    
    if default_msg == True:
        print("shortest path called")
        
    while len(frontier_set) > 0:
        path_cost, current, total_path_cost = heapq.heappop(heap)
        
        if current in frontier_set:
            frontier_set.remove(current)
        else:
            continue
        
        explored_set.add(current)
        
        if current == goal:
            return reconstruct_path(prev_path, current)
        
        for next_path in list_of_roads[current]:   
            
            if next_path in explored_set: 
                continue  
            
            new_cost = total_path_cost + euclidean_distance(current, next_path)         
            gScore = calculate_path_cost(heap, next_path)
                          
            if next_path not in frontier_set or new_cost < gScore:                
                gScore = new_cost
                prev_path[next_path] = current
                
                h_value[next_path] = new_cost + euclidean_distance(next_path, goal)
                heapq.heappush(heap, (h_value[next_path], next_path, gScore))
                frontier_set.add(next_path)
   
    return "Route Finder did not find any possible path"

def calculate_path_cost(heap, path):
    for i in heap:
        if i[1] == path:  
            item = heap[0][2]
            return item

def reconstruct_path(prev_pos, current_position):
    new_path = [current_position]
    while current_position in prev_pos.keys():
        current_position = prev_pos[current_position]
        new_path.append(current_position)
    return new_path[::-1]


def euclidean_distance(start, goal):
    x1 = cross_roads[start][0]
    x2 = cross_roads[goal][0]
    y1 = cross_roads[start][1]
    y2 = cross_roads[goal][1]
    return math.sqrt((x1 - x2) ** 2 + (abs(y1 -y2)) ** 2)
