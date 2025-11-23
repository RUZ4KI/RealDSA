class Graph {
  constructor(vertices) {
    this.graph = [];
    for (let i = 0; i < vertices; i++) {
      this.graph.push([]);
      for (let j = 0; j < vertices; j++) {
        this.graph[i].push(0);
      }
    }
  }

  add_edge(u, v) {
    this.graph[u][v] = 1;
  }
}

const g = new Graph(4);
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(1, 3);
g.add_edge(2, 3);
console.log(g.graph);
