class Menu:
    def __init__(self) -> None:
        self.__options = {
            "1": "add course",
            "2": "get course data",
            "3": "statistics",
            "0": "exit",
        }
        self.__studies = Studies()

    def show(self):
        for number, option in self.__options.items():
            print(number, option)
        self.__get_user_input()

    def __get_user_input(self):
        while True:
            option = input("\ncommand: ")
            if option == "0":
                break
            self.__treat_option(option)

    def __treat_option(self, option: int):
        if option == "1":
            self.__add_course()
        elif option == "2":
            self.__get_course_data()

    def __add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__studies.add_course(Course(name, grade, credits))

    def __get_course_data(self):
        name = input("course: ")
        course = self.__studies.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(course)


class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def __str__(self) -> str:
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class Studies:
    def __init__(self) -> None:
        self.__courses = {}

    def add_course(self, course: Course):
        self.__courses[course.name()] = course

    def get_course(self, name: str) -> Course:
        if name not in self.__courses:
            return None
        return self.__courses[name]


if __name__ == "__main__":
    Menu().show()
    # TODO statistics create Statistics class in: Studies
