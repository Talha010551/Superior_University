def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_neighbors(state, cap1, cap2):
    x, y = state
    neigh = []
    if x < cap1:
        neigh.append(((cap1, y), "Fill Jug1"))
    if y < cap2:
        neigh.append(((x, cap2), "Fill Jug2"))
    if x > 0:
        neigh.append(((0, y), "Empty Jug1"))
    if y > 0:
        neigh.append(((x, 0), "Empty Jug2"))
    if x > 0 and y < cap2:
        pour = min(x, cap2 - y)
        neigh.append(((x - pour, y + pour), f"Pour Jug1 -> Jug2 ({pour} units)"))
    if y > 0 and x < cap1:
        pour = min(y, cap1 - x)
        neigh.append(((x + pour, y - pour), f"Pour Jug2 -> Jug1 ({pour} units)"))
    return neigh

def dfs_water_jug(cap1, cap2, target):
    if target == 0:
        print("Target is 0 — start state already satisfies the goal: (0, 0)")
        return
    if target > max(cap1, cap2):
        print(f"No solution: target ({target}) is greater than both jug capacities.")
        return
    if target % gcd(cap1, cap2) != 0:
        print(f"No solution: target ({target}) is not a multiple of gcd({cap1},{cap2}) = {gcd(cap1,cap2)}.")
        return

    start = (0, 0)
    stack = [start]
    visited = set([start])
    parent = {start: None}  

    found_state = None
    while stack:
        state = stack.pop()
        x, y = state
        if x == target or y == target:
            found_state = state
            break
        for (ns, action) in get_neighbors(state, cap1, cap2):
            if ns not in visited:
                visited.add(ns)
                parent[ns] = (state, action)
                stack.append(ns)

    if not found_state:
        print("No solution found by DFS.")
        return

    path_states = []
    actions = []
    s = found_state
    while parent[s] is not None:
        prev, act = parent[s]
        path_states.append(s)
        actions.append(act)
        s = prev
    path_states.append(start)
    path_states.reverse()
    actions.reverse()

    print(f"\nSolution found! Jug capacities: Jug1={cap1}, Jug2={cap2}, target={target}")
    print("Steps (rules applied):")
    print(f"Step 0: Start state {path_states[0]}")
    for i, act in enumerate(actions, start=1):
        print(f"Step {i}: {act} -> {path_states[i]}")
    print(f"Goal reached at step {len(actions)}: {path_states[-1]}")

dfs_water_jug(4, 3, 2)   
dfs_water_jug(5, 3, 4)   

