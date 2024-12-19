graph = {}
costs = {}
parents = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 2
graph['a']['d'] = 4

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['c'] = 7

graph['c'] = {}
graph['c']['fin'] = 1

graph['d'] = {}
graph['d']['c'] = 6
graph['d']['fin'] = 3

graph['fin'] = {}

infinity = float('inf')

costs['a'] = 5
costs['b'] = 2
costs['fin'] = infinity

parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

print(graph)
print(costs)
print(parents)


processed = []

def find_lowest_cost_node(some_costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in some_costs:
        cost = some_costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node:
    current_cost = costs[node]
    neighbours = graph[node]
    for neighbour_node in neighbours.keys():
        new_cost = current_cost + neighbours[neighbour_node]
        if costs.get(neighbour_node, float('inf')) > new_cost:
            costs[neighbour_node] = new_cost
            parents[neighbour_node] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs['fin'])
print(parents['fin'])

