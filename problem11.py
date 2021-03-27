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
