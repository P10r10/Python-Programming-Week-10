class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: "Money"):
        return (
            self.__euros == another.__euros and self.__cents == another.__cents
        )

    def __lt__(self, another: "Money"):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        else:
            return self.__euros < another.__euros

    def __gt__(self, another: "Money"):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        else:
            return self.__euros > another.__euros

    def __ne__(self, another: "Money"):
        return not self.__eq__(another)

    def __add__(self, another: "Money"):
        total_cents = self.__cents + another.__cents
        total_euros = self.__euros + another.__euros
        if total_cents >= 100:
            total_cents -= 100
            total_euros += 1
        return Money(total_euros, total_cents)

    def __sub__(self, another: "Money"):
        total_cents = self.__cents - another.__cents
        total_euros = self.__euros - another.__euros
        if total_cents < 0:
            total_cents += 100
            total_euros -= 1
        if total_cents < 0 or total_euros < 0:
            raise ValueError("a negative result is not allowed")
        return Money(total_euros, total_cents)


if __name__ == "__main__":
    e1 = Money(1, 1)
    print(e1)
    e1.euros = 1000
    print(e1)
