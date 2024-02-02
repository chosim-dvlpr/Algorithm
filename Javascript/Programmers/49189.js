function solution(n, edge) {
    let graph = [];
    for (let i=0; i < n+1; i++) {
        graph.push([]);
    }
    edge.forEach((e, i) => {
        graph[e[0]].push(e[1])
        graph[e[1]].push(e[0])
    })
    
    let visited = new Array(n+1).fill(0);
    visited[1] = 1;
    let cnt = 1;    
    let q = [1];
    
    while (q.length) {
        const idx = q.shift();
        graph[idx].forEach((g, i) => {
            if (visited[g] === 0) {
                visited[g] = visited[idx]+1;
                q.push(g)
            }
        })
    }
    
    let mx = 0;
    let answer = 0;
    
    visited.forEach((v, i) => {
        if (v > mx) {
            answer = 1;
            mx = v;
        } else if (v === mx) {
            answer++;
        }
    })
    return answer
}
