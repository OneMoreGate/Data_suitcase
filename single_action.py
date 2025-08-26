import pandas as pd
import os

class SingleAction():
    '''
    Создает класс с описанием какого-то конктретного действия и его параметрами
    '''

    def __init__(self, action_name):
        self.action_name = str(action_name)

    # изменяет имя для действия
    def change_name():
        pass

    # добавляет описательный параметр для действия 
    def add_param(self, name: str, value):
        new_param = pd.DataFrame({'Name': [str(name)], 'Value': [value]})
        if not hasattr(self, 'param_tabels'):
            self.param_tabels = new_param
        else:
            self.param_tabels = pd.concat([self.param_tabels, new_param], ignore_index=True)

    # удаляет описательный параметр для действия
    def del_param(self, index):
        self.param_tabels.drop(index, inplace = True)
        self.param_tabels.reset_index(drop = True, inplace = True)

    # сохраняет действие в отдельный файл
    def save_to_csv(self):
        path_to_save = os.path.join(os.getcwd(), self.action_name)
        self.param_tabels.to_csv(path_to_save)

    def read_from_csv(self):
        pass

    def del_txt(self):
        pass