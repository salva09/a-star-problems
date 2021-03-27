# Problema 11

Tenemos cinco monedas dispuestas de la siguiente forma:  
 **A R A R A**  
El anverso de la moneda está representado por A y el reverso por R. Se considera un movimiento **(de coste 1)** el dar la vuelta a dos monedas contiguas.  
Deseamos obtener la situación final siguiente:  
 **R R R A R**  
Dada la función heurística *h(n) = número de monedas mal colocadas*.

## Solución

Para que fuera más sencillo la comparación y hacer el movimiento de "voltear" las monedas, utilicé valores booleanos en lugar de A y R.

```python
# A = True
# R = False

initial_state = [True, False, True, False, True]
solution_state = [False, False, False, True, False]

acumulated_cost = 0

def move(array, pos):
    array[pos] = not array[pos]
    array[pos + 1] = not array[pos + 1]
    return array

def weight(array):
    weight = 0
    for i in range(0, len(array)):
        if (array[i] != solution_state[i]):
            weight += 1

    weight += acumulated_cost
    return weight

if __name__ == "__main__":
    current_state = initial_state.copy()
    visited_states = []

    while(current_state != solution_state):
        print(f"Current: {current_state}")
        visited_states.append(current_state.copy())

        states = []
        for i in range(0, len(current_state) - 1):
            state = move(current_state.copy(), i)
            if state not in visited_states:
                states.append(state)

        print(f"States: {states}")

        acumulated_cost += 1
        state_weights = []
        for state in states:
            state_weights.append(weight(state))

        print(f"State wheights: {state_weights}")

        min_weight = min(state_weights)
        print(f"Min: {min_weight}")
        index = state_weights.index(min_weight)
        print(f"Index: {index}")

        current_state = states[index]
        print(f"Selected: {current_state}")
        input()

    print(f"Initial: {initial_state}")
    print(f"Current: {current_state}")
    print(f"Solution: {solution_state}")
    print(f"Cost: {acumulated_cost}")
    print(f"Visited states: {visited_states}")
```

Y esta es la salida del programa.

```
$ python problema11.py
Current: [True, False, True, False, True]
States: [[False, True, True, False, True], [True, True, False, False, True], [True, False, False, True, True], [True, False, True, True, False]]
State wheights: [5, 5, 3, 3]
Min: 3
Index: 2
Selected: [True, False, False, True, True]

Current: [True, False, False, True, True]
States: [[False, True, False, True, True], [True, True, True, True, True], [True, False, False, False, False]]
State wheights: [4, 6, 4]
Min: 4
Index: 0
Selected: [False, True, False, True, True]

Current: [False, True, False, True, True]
States: [[False, False, True, True, True], [False, True, True, False, True], [False, True, False, False, False]]
State wheights: [5, 7, 5]
Min: 5
Index: 0
Selected: [False, False, True, True, True]

Current: [False, False, True, True, True]
States: [[True, True, True, True, True], [False, False, False, False, True], [False, False, True, False, False]]
State wheights: [8, 6, 6]
Min: 6
Index: 1
Selected: [False, False, False, False, True]

Current: [False, False, False, False, True]
States: [[True, True, False, False, True], [False, True, True, False, True], [False, False, False, True, False]]
State wheights: [9, 9, 5]
Min: 5
Index: 2
Selected: [False, False, False, True, False]

Initial: [True, False, True, False, True]
Current: [False, False, False, True, False]
Solution: [False, False, False, True, False]
Cost: 5
Visited states: [[True, False, True, False, True], [True, False, False, True, True], [False, True, False, True, True], [False, False, True, True, True], [False, False, False, False, True]]
```



# Problema 13

Dado el siguiente grafo donde cada arco indica su coste y la tabla que indica la estimación del coste *h* hasta la solución, indica cual sería el árbol de búsqueda que se obtendría mediante el algoritmo de **A*** para encontrar el camino entre el nodo **A** y el nodo **O**.

![](/home/salva/Documents/Development/ExamenIA/b31c9921-ced0-4d09-8dde-2ae278f909bc.png)

## Solución

El código es muy parecido al anterior, sólo que en lugar de expandir los estados, el gráfo ya está hecho y sólo había que buscar los valores.

```python
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
```

Y esta es la salida del programa.

```
Current node: A

Current node: B

Current node: E

Current node: F

Current node: K

Initial node: A
Current node: O
Meta node: O
Cost: 8
Visited nodes: ['A', 'B', 'E', 'F', 'K']
```

En ambos programas, se muestran los estados que deben recorrerse para llegar a la solución, al igual que sus costos.

# Repositorio

El código se encuentra en el siguiente repositorio: [GitHub - salva09/a-star-problems](https://github.com/salva09/a-star-problems)


