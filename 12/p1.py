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
    def __init__(self, path, visited, node, possible_next):
        self.node = node
        self.visited = visited
        self.reached_end = False
        self.path = path
        self.path.append(node)

        if node.lower() == node:
            self.visited.add(node)

        if node == "end":
            global found_paths
            found_paths.append(path.copy())
            self.reached_end = True
            self.possible_next = set()
        else:
            self.possible_next = set(possible_next) - self.visited

    def next_step(self):
        steps = set(self.possible_next) - self.visited
        for step in steps:
            p = Path(
                path=self.path,
                visited=self.visited,
                node=step,
                possible_next=network[step],
            )
            if p.reached_end:
                p.cleanup()
                continue

            p.next_step()

        self.cleanup()

    def cleanup(self):
        if self.node in self.visited:
            self.visited.remove(self.node)

        self.path = self.path[:-1]
        self.reached_end = False


p = Path(path=[], visited=visited, node="start", possible_next=network["start"])
p.next_step()
# print(found_paths)
print(len(found_paths))