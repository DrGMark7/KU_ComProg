class ClassRoom:
    def __init__(self,grade=0,home_room_teacher="") -> None:
        self.grade = grade
        self.home_room_teacher = home_room_teacher
        self.student_List = []
        self.numStudents = 0
    def __str__(self) -> str:
        return f"Grade: {self.grade} \nHomeroom Teacher: {self.home_room_teacher}\nStudents: {', '.join(self.student_List)}"

    def get_student_no(self,n):
        return self.student_List[n-1]

    def add_student(self,student_name):
        if len(self.student_List) < 10:
            self.student_List.append(student_name)
            self.numStudents += 1
            return True
        else:
            return False
        
    def change_student(self,n,new_name):
        if 1 <= n <= self.numStudents:
            self.student_List[n-1] = new_name
            return True
        else:
            return False
        
    def remove_student(self,student_name):

        try:
            index_remove = self.student_List.index(student_name)
        except ValueError:
            return False
        
        self.student_List.pop(index_remove)
        self.numStudents -= 1
        return True
    
    def remove_student_no(self,n):
        if 1 <= n <= self.numStudents:
            self.student_List.pop(n-1)
            self.numStudents -= 1
            return True
        else:
            return False
        
    def set_grade(self,grade):
        self.grade = grade

    def set_homeroom_teacher(self,homeroom_teacher):
        self.home_room_teacher = homeroom_teacher

    def set_student_list(self,student_List):
        self.student_List = student_List

    def set_num_student(self,num_student):
        self.numStudents = num_student

    def get_grade(self):
        return self.grade
    
    def get_homeroom_teacher(self):
        return self.home_room_teacher

    def get_student_list(self):
        return self.student_List

    def get_num_student(self):
        return self.numStudents
