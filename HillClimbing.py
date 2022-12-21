'''
S -> a
E -> z

a = lowest
z = highest

Move up, down, left, right

Shortest Path
https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
'''

from Map import Map
from Djikstra import Graph
import heapq

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start, target):
    print("Dijkstra's shortest path")
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print("updated : current = %s next = %s new_dist = %s" % current.get_id(), next.get_id(), next.get_distance())
            else:
                print("not updated : current = %s next = %s new_dist = %s" % current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(list(l.strip()))
    f.close()
    return data

def main():
    data = read_data("TestData.txt")
    
    map = Map(data)
    
    map.print_map()

    map.create_graph()

    g = map.get_graph()

    print('graph')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print (f"( {vid} , {wid})")
    
    dijkstra(g, g.get_vertex('a'), g.get_vertex('e')) 

    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print(f"The shortest path : {(path[::-1])}")

if __name__=='__main__':
    main()