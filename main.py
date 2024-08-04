class CinemaTicketSystem:
    def __init__(self):
        self.film = []
        self.ticket = []
        self.user = []
    def addMovie(self, movieName):
        self.film.append(movieName)
        return self.film.index(movieName)
    def addUser(self, userName):
        self.user.append(userName)
        return self.user.index(userName)

    def showAllMovies(self):
        for x in self.film:
            index = self.film.index(x)
            print(f"{index}. {x} ")
    def buyTicket(self,userID,movieID):
        s = f"{self.user[userID]} покупает билет на {self.film[movieID]}"
        print(s)
        self.ticket.append(s)
        return self.ticket.index(s)
    def cancelTicket(self,ticketID):
        if len(self.ticket) > ticketID:
            self.ticket.pop(ticketID)
            return True
        else:
            return False


def Menu(obj):
    if isinstance(obj, CinemaTicketSystem):
        print("Здравствуйте, у вас есть следующие доступные функции:")
        print(" 1. Добавить новый фильм; ")
        print(" 2. Показать все доступные фильмы; ")
        print(" 3. Добавить нового пользователя; ")
        print(" 4. Купить билет; ")
        print(" 5. Отменить покупку билета; ")
        print(" 0. Завершить программу")

        choice = int(input())
        if choice == 1:
            print("Введите название фильма, которую хотите добавить:")
            s = input()
            obj.addMovie(s)
            print(f"Фильм {s} добавлен в список")
            return Menu(obj)
        if choice == 2:
            obj.showAllMovies()
            return Menu(obj)
        if choice == 3:
            print("Введите название пользователя, которую хотите добавить:")
            s = input()
            obj.addUser(s)
            print(f"Пользователь {s} добавлен в список")
            return Menu(obj)
        if choice == 4:
            print("Введите идентификатор пользователя чтобы купить билет:")
            s = int(input())
            if s>=len(obj.user):
                print("Такого пользователя не существует")
                return Menu(obj)
            print("Теперь идентификатор фильма:")
            d = int(input())
            if d >= len(obj.film):
                print("Такого фильма не существует")
                return Menu(obj)
            obj.buyTicket(s,d)
            return Menu(obj)
        if choice == 5:
            print("Введите идентификатор билета чтобы отменить покупку:")
            s = int(input())
            if s >= len(obj.ticket):
                print("Такого билета не существует")
                return Menu(obj)
            obj.cancelTicket(s)
            return Menu(obj)
        if choice == 0:
            print("Программа завершена")

system = CinemaTicketSystem()
Menu(system)




