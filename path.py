def numEdge(nodes: list):
    a, b, c, d, e, f, g = [nodes[i] for i in range(7)]
    return (a + b + c + d) * 1 + (a + b + c) * e + (c + d) * f + e * g + (f + g) * 1

def numPath(nodes: list):
    a, b, c, d, e, f, g = [nodes[i] for i in range(7)]
    return (a + b + c) * e * g + (c + d) * f

if __name__ == '__main__':
    nodes = [int(input()) for _ in range(7)]
    print(numEdge(nodes))
    print(numPath(nodes))
    