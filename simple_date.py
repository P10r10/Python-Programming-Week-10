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

    def __total_days(self, date: "SimpleDate") -> int:
        return date.__day + date.__month * 30 + date.__year * 360

    def __sub__(self, other: "SimpleDate") -> int:
        return abs(self.__total_days(self) - self.__total_days(other))


if __name__ == "__main__":
    d1 = SimpleDate(1, 7, 1999)  # 719640 + 210 + 1 = 719851
    d2 = SimpleDate(1, 8, 1998)  # 719280 + 240 + 1 = 719521

    print(d1-d2)
