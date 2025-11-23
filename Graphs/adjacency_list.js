class Graph {
  constructor() {
    this.graph = {};
  }

  add_edge(u, v) {
    if (!this.graph[u]) {
      this.graph[u] = [];
    }
    if (!this.graph[v]) {
      this.graph[v] = [];
    }
    this.graph[u].push(v);
  }
}

const g = new Graph();
g.add_edge("A", "B");
g.add_edge("A", "C");
g.add_edge("B", "D");
g.add_edge("C", "D");
console.log(g.graph);
