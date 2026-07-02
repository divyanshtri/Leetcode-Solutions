class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ate=0
        i=0
        rotations=0
        while(i>=0):
            if rotations == len(students):
                break
            if students[i]==sandwiches[0]:
                ate+=1
                rotations=0
                students.pop(i)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                rotations += 1
                
        return len(students)