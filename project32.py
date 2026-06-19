# This is coding for making oops file in whichwe use multilevel inheritance


class dadu:
    anger=100
class papa(dadu):
    anger=50
    def fanger(self):
        return(f"he is very good person and only {self.anger} of his father")
class me(papa):
    anger=20
    def fanger(self):
        return(f"I am very calm and introvert type and only {self.anger} of my father")

rdadu=dadu()
vpapa=papa()
ame=me()

print(ame.fanger())
