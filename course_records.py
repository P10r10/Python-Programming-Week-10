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

    def __treat_option(self, option: int) -> None:
        if option == "1":
            self.__add_course()
        elif option == "2":
            self.__show_course_data()
        elif option == "3":
            self.__statistics()

    def __add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__studies.add_course(Course(name, grade, credits))

    def __show_course_data(self) -> None:
        name = input("course: ")
        course = self.__studies.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(course)

    def __statistics(self) -> None:
        Statistics(self.__studies).show()


class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self) -> str:
        return self.__name

    def grade(self) -> int:
        return self.__grade

    def credits(self) -> int:
        return self.__credits

    def __str__(self) -> str:
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class Studies:
    def __init__(self) -> None:
        self.__courses = {}

    def add_course(self, course: Course) -> None:
        if not course.name() in self.__courses:
            self.__courses[course.name()] = course
        elif self.__courses[course.name()].grade() < course.grade():
            self.__courses[course.name()] = course

    def get_course(self, name: str) -> Course:
        if name not in self.__courses:
            return None
        return self.__courses[name]

    def get_courses(self) -> dict:
        return self.__courses

    def courses_with_grade(self, grade: int) -> int:
        return sum([c.grade() == grade for c in self.__courses.values()])


class Statistics:
    def __init__(self, studies: Studies) -> None:
        self.__studies = studies

    def __get_total_credits(self):
        return sum([c.credits() for c in self.__studies.get_courses().values()])

    def __get_mean_grade(self, nb_courses: int) -> float:
        if nb_courses == 0:
            return 0
        grades = [c.grade() for c in self.__studies.get_courses().values()]
        return sum(grades) / nb_courses

    def show(self):
        nb = len(self.__studies.get_courses())  # total number of courses
        credits = self.__get_total_credits()
        mean = self.__get_mean_grade(nb)
        print(f"{nb} completed courses, a total of {credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            print(f"{i}: {self.__studies.courses_with_grade(i) * 'x'}")


if __name__ == "__main__":
    Menu().show()
