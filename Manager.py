import datetime


class TimeManage:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.start = datetime.datetime.now()
    def __enter__(self):
        self.documents = []
        with open(self.path1) as documents:
            while True:
                document_type = documents.readline().strip()
                doc_num = documents.readline().strip()
                person_name = documents.readline().strip()
                if not document_type:
                    break
                doc_dict = {"type": document_type, "number": doc_num, "name": person_name}
                self.documents.append(doc_dict)
        with open(self.path2) as shelves:
            self.directories = {}
            while True:
                directory_num = shelves.readline().strip()
                numbers = shelves.readline().strip()
                if not directory_num:
                    break
                num_list = numbers.split()
                new_dir = {directory_num: num_list}
                self.directories.update(new_dir)
        return self
    def num_to_name(self):
        any_num = str(input("Введите номер: "))
        for doc_dict in self.documents:
            if doc_dict["number"] == any_num:
                return doc_dict["name"]
    def list_print(self):
        for doc_list in self.documents:
            print(doc_list['type'], doc_list['number'], doc_list['name'])
    def num_to_shelf(self):
        any_num = str(input("Введите номер: "))
        for shelf, number_list in self.directories.items():
            for number in number_list:
                if number == any_num:
                    return shelf
    def add_new_doc(self):
        new_num = str(input("Введите номер: "))
        new_type = str(input("Введите тип: "))
        new_name = str(input("Введите имя: "))
        new_shelf = str(input("Введите полку: "))
        new_dict = dict(type=new_type, number=new_num, name=new_name)
        if new_shelf in self.directories:
            self.documents.append(new_dict)
            for shelf, number_list in self.directories.items():
                if shelf == new_shelf:
                    number_list.append(new_num)
            print("Документ добавлен")
        else:
            print("Такой полки не существует!")
    def all_names(self):
        try:
             for doc_dict in self.documents:
                 print(doc_dict["name"])
        except KeyError:
            print("Имя не записано!")
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        print("Начало в:", self.start)
        print("Конец в:", self.end)
        print("Затрачено:", self.end - self.start)
with TimeManage("Documents","Directories") as doc_arch:
    print(doc_arch.all_names())