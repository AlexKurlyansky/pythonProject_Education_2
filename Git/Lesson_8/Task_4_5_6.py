def numb(func):
    def arguments(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print('Недостаточно техники!')
        except KeyError:
            print('Нет такого товара!')
    return arguments

class Storage:
    technics = {}
    @classmethod
    @numb
    def tech_to(cls, tech_type, tech_name, tech_model, tech_count):
        cls.technics[tech_type][tech_name][tech_model]["count"] += tech_count

    @classmethod
    @numb
    def tech_from(cls, tech_type, tech_name, tech_model, tech_count):
        current_count = cls.technics[tech_type][tech_name][tech_model]["count"]
        if current_count < tech_count:
            raise ValueError
        else:
            cls.technics[tech_type][tech_name][tech_model]["count"] -= tech_count

    @staticmethod
    def get_args():
        for key, value in Storage.technics.items():
            print(key, value)

class TypeTech:
    def __init__(self, name, model, technic_type, count=0):
        self.name = name
        self.model = model
        self.technic_type = technic_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Неверные данные!")
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        tech_storage_info = Storage.technics.get(self.technic_type, {})
        if self.name in tech_storage_info.keys():
            tech_storage_info_by_name = tech_storage_info[self.name]
            if self.model in tech_storage_info_by_name.keys():
                tech_storage_info_by_model = tech_storage_info_by_name[self.model]
                tech_storage_info_by_model["count"] += self.__count
            else:
                tech_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            tech_storage_info[self.name] = {self.model: {"count": self.__count}}

        Storage.technics[self.technic_type] = tech_storage_info

class Printer(TypeTech):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, "Printer", count)
        self.colors = colors

class Scanner(TypeTech):
    def __init__(self, name, model, count):
        super().__init__(name, model, "Scanner", count)

class Xerox(TypeTech):
    def __init__(self, name, model, count):
        super().__init__(name, model, "Xerox", count)

class Notebook(TypeTech):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, "Notebook", count)
        self.ram = ram
        self.system_type = system_type

printer_1 = Printer('HP', '6543', 1000, ['red', 'blue', 'green'])
printer_2 = Printer('Samsung', '5678', 500, ['black'])
xerox_1 = Xerox('LG', '3214', 100)
scanner_1 = Scanner('Samsung', '7890', 50)
notebook_1 = Notebook('Mac', 'MacBookAir', 500, 8, 'MacOS')

Storage.get_args()
Storage.tech_to(tech_type='Printer', tech_name='HP', tech_model='6543', tech_count=100)
Storage.get_args()
Storage.tech_from(tech_type='Scanner', tech_name='Samsung', tech_model='7890', tech_count=30)
Storage.get_args()
