class Employed:
    def __init__(self):
        self.name = "Francisco"
        self.salary = 1000

    def get_salary(self, salary, query):
        self.salary = salary
        query = "SELECT salary FROM Employed;"

    def change_salary(self, salary, query):
        self.salary = salary
        query = "INSERT INTO Employed (name, salary) VALUES("Francisco", 2000);"

if __name__ == '__main__':
    Employed = employed()
    Employed.get_salary()
    Employed.change_salary()
