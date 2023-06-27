class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __eq__(self, other: "SimpleDate") -> bool:
        return (
            self.__year == other.__year and self.__month == other.__month and
            self.__day == other.__day
        )

    def __ne__(self, other: "SimpleDate") -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: "SimpleDate") -> bool:
        if self.__year == other.__year:
            if self.__month == other.__month:
                return self.__day < other.__day
            else:
                return self.__month < other.__month
        else:
            return self.__year < other.__year

    def __gt__(self, other: "SimpleDate") -> bool:
        return not self.__lt__(other) and not self.__eq__(other)

    def __add__(self, nb_days: int) -> "SimpleDate":
        new_day = nb_days + self.__day
        new_month = self.__month
        new_year = self.__year
        if new_day > 30:
            new_month += new_day // 30
            new_day %= 30
        if new_month > 12:
            new_year += new_month // 12
            new_month %= 12
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(begin: "SimpleDate", end: "SimpleDate") -> int:
        total_days = abs((end.__year - begin.__year) * 365)
        total_days += abs((end.__month - begin.__month) * 30)
        total_days += abs(end.__day - begin.__day)
        return total_days


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
