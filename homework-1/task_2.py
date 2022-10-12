class Student:

    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects =subjects

 class Special_Student(Student):                #class inheriting student for specialization#

     def __init__(self,spec_name):             #instantiating class#
        self.spec_name=spec_name
        print("specialization "+str(spec_name))

     def new(self, new_subject):               #method to add new subject#
         self.new_subject=new_subject
         ob.subjects.update(new_subject)
         print("LIST OF SUBJECTS AFTER ADDING")
         print(ob.subjects)

     def delete(self, old_subject):              #method to deleted selected  subject#
         self.old_subject = old_subject
         ob.subjects.pop(old_subject)
         print("LIST OF SUBJECTS AFTER REMOVING")
         print(ob.subjects)

     def subjects(self):                          #method to print all subjects#
         ob.subjects.update({"java":89})     #since the object has a subject deleted, updating with the deleted subject#
         subjects=ob.subjects.keys()
         print("subjects taken by student "+(str(subjects)[9:42]))      #converting dict into string and printing#

     def overall_mark(self):                          #method to find average#
        sum=0
        avg=0                                # initializing new variable to store result avg#
        length=len(ob.subjects)
        for i in ob.subjects.values():
            sum=sum+i
        avg=sum/length                          # Storing result in newly created result variable#
        print("avg of marks "+str(avg))


ob=Student("pinky",23,1,{"math":100,"python":90, "java":89 })          #passing object to parent 'Student' class#
oa=Special_Student("software")                                          # passing object to child Specialization class#
oa.new({"c":76})                                                   #calling add_item method#
oa.delete("java")                                               # calling remove subject method#
oa.subjects()                                                    # calling subjects method fo list of subjects#
oa.overall_mark()