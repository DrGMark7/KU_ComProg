class Course:
    def __init__(self,title,course_id,credit) -> None:
        self.title = title
        self.course_id = course_id
        self.credit = credit

class Teacher:
    def __init__(self, firstname, lastname, id) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"
    
class Major:
    def __init__(self, id, name, faculty) -> None:
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f"{self.name} {self.faculty} ({self.id})"

class Student(Course,Teacher,Major):
    def __init__(self,id,firstname,lastname) -> None:
        self.id = id
        self.firstname ,self.lastname = firstname,lastname
        self.courses ,self.num_course  = [],[]
        self.total_credit = 0
        self.advisor = None
        self.major = None
        self.current_course = None

    def __str__(self):
        string = f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {' '.join(self.num_course)} "
        return string

    
    def add_course(self,course):
        self.current_course = course
        if (self.current_course.title not in self.courses) and (self.total_credit + self.current_course.credit <= 25):
            self.courses.append(self.current_course.title)
            self.num_course.append(self.current_course.course_id)
            self.total_credit += self.current_course.credit
            return True
        else:
            return False
        

    def drop_course(self,course):
        self.current_course = course
        if self.courses[-1] == self.current_course.title:
            self.courses.append("")
            self.courses.remove(self.current_course.title)
            self.num_course.remove(self.current_course.course_id)
            self.total_credit -= self.current_course.credit
            return True
        elif len(self.courses) != 0:
            try:
                self.courses.remove(self.current_course.title)
                self.num_course.remove(self.current_course.course_id)
                self.total_credit -= self.current_course.credit
                return True
            except:
                return False
        else:
            return False
        
    def set_advisor(self,advisor):
        self.advisor = advisor

    def set_major(self,major):
        self.major = major 

    def get_credit(self):
        return self.total_credit        

#- ---------------------------------------
