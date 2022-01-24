class My_ZeroDivizion_Error(Exception):
    def __init__(self):
        self.txt = "Деление на 0 недопустимо!"

def division(inp_submitted, inp_deliverer):

    try:
        if inp_deliverer == 0:
              raise My_ZeroDivizion_Error
        print(inp_submitted / inp_deliverer)
    except My_ZeroDivizion_Error as err:
        print(err.txt)

division(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
division(150, 10)
division(12, 0)