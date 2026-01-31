
class Solution:
    results = []
    course_done = {}

    def takeCourse(self, graph, course, visited):
        
        if course in self.course_done:
            return True
        
        if course not in graph:
            self.results.append(course)
            self.course_done[course] = True
            return True
        else:
            has_all_requ = True
            visited[course] = True
            for prerq in graph[course]:
                if prerq not in visited or prerq in self.course_done:
                    if prerq not in self.course_done:
                        done = self.takeCourse(graph, prerq, visited)
                    else:
                        done = True
                    
                    if done == False:
                        has_all_requ = False
                else:
                    has_all_requ = False
                
            if has_all_requ:
                self.course_done[course] = True
                self.results.append(course)

            
            return has_all_requ
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        self.results = []
        self.course_done = {}
        for prerequisite in prerequisites:
            course = prerequisite[0] 
            prerq = prerequisite[1]

            if course not in graph:
                graph[course] = [prerq]
            else:
                graph[course].append(prerq)
        
        no_fit = []
        for i in range(numCourses):
            done = self.takeCourse(graph, i, {})
            if not done:
                no_fit.append(i)
        
        if len(no_fit) > 0:
            return []
        
        return self.results
        