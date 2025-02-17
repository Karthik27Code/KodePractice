from collections import defaultdict, deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        in_cntr = [0] * numCourses
        visited = {}
        for course, pre_req in prerequisites:
            in_cntr[course] += 1
            graph[pre_req].append(course)

        graph_queue = deque()
        for course, in_cnt in enumerate(in_cntr):
            if in_cnt == 0:
                graph_queue.append(course)
        
        while graph_queue:
            curr_course = graph_queue.popleft()

            visited[curr_course] = True

            neighbors = graph[curr_course]

            for neighbor in neighbors:
                if neighbor not in visited:
                    graph_queue.append(neighbor)

        if len(visited) == numCourses:
            return True
        else:
            return False
        

sol = Solution()
# print(sol.canFinish(2, [[1,0]]))
# print(sol.canFinish(2, [[1,0],[0,1]])) 
print(sol.canFinish(2, [[0,1]])) 