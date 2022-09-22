class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


if __name__ == '__main__':

    op = 1

    while op != '0':
        print('Enter two numbers:')
        a = float(input('Enter the first number:'))
        b = float(input('Enter ther second number:'))
        obj = calc(a, b)

        print('Enter the operation:')
        op = input(' Enter + for addition \n Enter - for substraction \n Enter * for Multiplication \n Enter / for division  \n Enter 0 for Exit\n')
        if op == '+':
            print(obj.add())
        elif op == '-':
            print(obj.sub())
        elif op == '*':
            print(obj.mul())
        elif op == '/':
            print(obj.div())
        elif op == '0':
            print('closing calcultor')
        else:
            print('invalid choice')
