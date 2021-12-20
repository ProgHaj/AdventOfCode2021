import sys

nodes_raw = open("input", "r").readlines()
edges = [node.strip().split("-") for node in nodes_raw]
network = {}
nodes = {}
parents = {}

for source, target in edges:
    if source not in network:
        network[source] = set()

    if target not in network:
        network[target] = set()

    network[source].add(target)
    network[target].add(source)


found_paths = []
visited = set()


class Path:
    def __init__(self, path, visited, node, possible_next, visited_two):
        self.node = node
        self.visited = visited
        self.reached_end = False
        self.path = path
        self.path.append(node)
        self.visited_two = visited_two

        if node.lower() == node:
            if node in self.visited:
                self.visited_two = node

            self.visited.add(node)

        if node == "end":
            global found_paths
            found_paths.append(path.copy())
            self.reached_end = True
            self.possible_next = set()
        else:
            if self.visited_two:
                possible_next = set(possible_next) - set(self.visited)
            else:
                possible_next = set(possible_next)

            self.possible_next = possible_next

    def next_step(self):
        steps = set(self.possible_next)
        for step in steps:
            if step == "start":
                continue

            p = Path(
                path=self.path,
                visited=self.visited,
                node=step,
                possible_next=network[step],
                visited_two=self.visited_two,
            )
            if p.reached_end:
                p.cleanup()
                continue

            p.next_step()

        self.cleanup()

    def cleanup(self):
        self.path.pop()
        if self.visited_two == self.node:
            self.visited_two = None
        elif self.node in self.visited:
            self.visited.remove(self.node)

        self.reached_end = False


p = Path(
    path=[],
    visited=visited,
    node="start",
    possible_next=network["start"],
    visited_two=None,
)
p.next_step()
# print(found_paths)
print(len(found_paths))