class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])

        class DSU:
            def __init__(self, points):
                self.points = points
                self.n = len(points)

                # representative
                self.repr = dict()
                # size
                self.size = dict()
                # intersection
                self.intr = dict()

                # filling default values
                for i in range(self.n):
                    self.repr[i] = i
                    self.size[i] = 1
                    self.intr[i] = self.points[i]

            def find(self, u):
                if u == self.repr[u]:
                    return u
                self.repr[u] = self.find(self.repr[u])
                return self.repr[u]

            def combine(self, u, v):
                u = self.find(u) 
                v = self.find(v)
                if self.size[u] > self.size[v]:
                    u, v = v, u

                self.repr[u] = v
                self.size[v] += self.size[u]

                # changing intersection of new representative
                self.intr[v] = [max(self.intr[u][0], self.intr[v][0]), \
                                min(self.intr[u][1], self.intr[v][1])]
                
            def answer(self):
                s = set()
                for i in range(self.n):
                    # referring to intersection of representative's tree
                    val = self.intr[self.find(i)]
                    s.add(tuple(val))
                return len(s)


        dsu = DSU(points=points)
        for i in range(len(points)-1):
            # only representatives contain real
            # intersection value for all childs in DSU tree
            left = dsu.intr[dsu.find(i)]
            right = dsu.intr[dsu.find(i+1)]
            if left[1] >= right[0]:
                # we only combine representatives
                dsu.combine(dsu.find(i), dsu.find(i+1))

        # getting answer
        return dsu.answer()