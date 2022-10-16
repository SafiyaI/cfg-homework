class Student:

    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = subjects

class CFGStudent(Student): # Class Inheriting
     def __init__(self, name, age, id, subjects, spec_name):      # Instantiating of class
         super().__init__(name, age, id, subjects)
         self.spec_name = spec_name
         print(f"  -- Specialisation {spec_name}  -- ")

     def new_subject(self, new_subject):               # Method
         self.subjects.update(new_subject)
         print("LIST OF SUBJECTS AFTER ADDING (+)")
         print(self.subjects)

     def delete_subject(self, old_subject):              # Method (delete)
         self.subjects.pop(old_subject)
         print("LIST OF SUBJECTS AFTER REMOVING (-)")
         print(self.subjects)

     def view_subjects(self):                          # Method to print all subjects
         subjects = self.subjects.keys()
         print(f"SUBJECTS WHICH IS TAKEN BY THE STUDENT - {subjects}")

     def overall_mark(self):                          # Method to find average
        sum = 0
        avg = 0                                # Initializing
        length = len(self.subjects)
        for i in self.subjects.values():
            sum = sum+i
        avg = sum/length                          # Storing result in newly created result variable
        print("average marks  = "+str(avg))


ob = Student("pinky", 25, 5, {"SQL": 100, "python": 90, "OOP":  10})
oa = CFGStudent("ALAN", 30, 87290, {"SQL": 98}, 'data')
oa.new_subject({"java": 98})
oa.delete_subject("SQL")
oa.view_subjects()
oa.overall_mark()