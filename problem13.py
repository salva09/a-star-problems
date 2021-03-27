def get_graph():
    graph = {
            "A": {"B": 2, "C": 1, "D": 2},
            "B": {"C": 1, "E": 1},
            "C": {"F": 4, "G": 2},
            "D": {"G": 2, "H": 1},
            "E": {"F": 1, "I": 1, "J": 3},
            "F": {"J": 1, "K": 1},
            "G": {"K": 3},
            "H": {"K": 2, "L": 2},
            "I": {"M": 3},
            "J": {"M": 2, "N": 1},
            "K": {"J": 1, "O": 3},
            "L": {"O": 1},
            "M": {},
            "N": {"O": 1},
            "O": {},
    }
    return graph

def get_h():
    cost = {
            "A": 6,
            "B": 5,                         
            "C": 6,
            "D": 6,
            "E": 3,
            "F": 5,
            "G": 5,
            "H": 4,
            "I": 8,
            "J": 3,
            "K": 2,
            "L": 1,
            "M": 5,
            "N": 1,
            "O": 0,
    }
    return cost

graph = get_graph()

initial_node = "A"
meta_node = "O"

acumulated_cost = 0

def get_weight(parent, child):
    weight = 0
    weight += acumulated_cost
    weight += graph[parent][child]
    weight += get_h()[child]
    return weight

if __name__ == "__main__":
    current_node = initial_node
    visited_nodes = []

    while(current_node != meta_node):
        print(f"Current node: {current_node}")
        visited_nodes.append(current_node)

        child_weights = {}
        for child in graph[current_node]:
            if child not in visited_nodes:
                child_weights[child] = get_weight(current_node, child)
        
        min_weight = min(child_weights.values())
        index = ""

        for child, value in child_weights.items():
            if value == min_weight:
                index = child
                break;

        acumulated_cost += graph[current_node][index]

        current_node = index

        input()

    print(f"Initial node: {initial_node}")
    print(f"Current node: {current_node}")
    print(f"Meta node: {meta_node}")
    print(f"Cost: {acumulated_cost}")
    print(f"Visited nodes: {visited_nodes}")
