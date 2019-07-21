class Student():
    def __init__(self, name, rno, study_year, aggregate):
        self.name = name
        self.rno = rno
        self.study_year = study_year
        self.aggregate = aggregate

    def studentDetails(self):
        print(self.name,"\n",self.rno,"\n",self.study_year)

    def studyCredentials(self):
        print(self.name,"\t",self.aggregate)

    def __repr__(self):
        return "Student Name: {},Roll No: {}, Study_year: {} and Aggregate: {}".format(self.name, self.rno, self.study_year, self.aggregate)


