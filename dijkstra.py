'''
# Promt:

def dijkstra(graph, source):
    previous = {}
    distance = {}
    for node in graph.nodes:
        distance[node] = float('inf')
        previous[node] = None
    distance[source] = 0
    nodelist = list(graph.nodes)
    while len(nodelist) > 0:
        singlenode = min(nodelist, key=lambda x: distance[x])
        nodelist.remove(singlenode)
        for neighbour in graph.neighbors(singlenode):
            distance_nodes = distance[singlenode] + graph[singlenode][neighbour]['weight']
            if distance_nodes < distance[neighbour]:
                distance[neighbour] = distance_nodes
                previous[neighbour] = singlenode
    return distance, previous   #explain line by line


'''

#response A

'''
def dijkstra(graph, source):
  """Finds the shortest path from a single source node to all other nodes in a weighted graph.

  Args:
    graph: A weighted graph.
    source: The source node.

  Returns:
    A dictionary containing the shortest path from the source node to each other node in the graph.
  """

  # Initialize the visited set to contain only the source node.
  visited = {source}

  # Initialize the shortest paths to all other nodes to infinity.
  shortest_paths = {}
  for node in graph.nodes:
    shortest_paths[node] = float("inf")

  # Set the shortest path to the source node to 0.
  shortest_paths[source] = 0

  # While there are still unvisited nodes, repeat the following steps:
  while visited != graph.nodes:

    # Find the unvisited node with the shortest path from the source node.
    current_node = min(visited - shortest_paths, key=shortest_paths.get)

    # Add this node to the visited set.
    visited.add(current_node)

    # Update the shortest paths to all of the unvisited neighbors of this node.
    for neighbor in graph.neighbors(current_node):
      if neighbor not in visited:
        new_path_length = shortest_paths[current_node] + graph.get_edge_weight(current_node, neighbor)
        if new_path_length < shortest_paths[neighbor]:
          shortest_paths[neighbor] = new_path_length

  # Return the shortest paths to all nodes.
  return shortest_paths
'''

#Response B:

