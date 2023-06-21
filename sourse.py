from math import floor
from string import ascii_letters


class Input:
    list = ['Алексей', 'men', 33, 116, 180, 1.4, '-']


class UserCal:
    S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбю-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, name, gender, age, weight, height, activ=1.4, goal='='):
        self.verify_name(name)
        self.verify_gender(gender)

        self.__user_name = name
        self.__gender = gender
        self.age = age
        self.weight = float(weight)
        self.height = height
        self.activ = activ
        self.calorie_goal = goal

        self.caloric = self.daily_calorie()
        self.total_caloric = floor(self.activ * self.caloric)
        self.ratio_min = floor(self.weight / 0.45 * 8)

    @classmethod
    def verify_name(cls, name):
        if type(name) != str or len(name) < 1:
            raise TypeError('Неправильный формат имени!')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in name:
            if len(s.strip(letters)) != 0:
                raise TypeError('В имени можно использовать только буквенные символы')

    @property
    def user_name(self):
        return self.__user_name

    @classmethod
    def verify_gender(cls, gender):
        if type(gender) != str:
            raise TypeError("Пол может быть или 'men' или 'woman'")

    @property
    def gender(self):
        return self.__gender

    @classmethod
    def verify_age(cls, age):
        if type(age) != int:
            raise TypeError('Возраст должен быть полным!')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float and type(weight) != int:
            raise TypeError('Вес должен быть числом!')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    def daily_calorie(self):
        if self.gender == 'men' and 13 <= self.age <= 80:
            calorie = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
            return floor(calorie)
        elif self.gender == 'woman' and 13 <= self.age <= 80:
            calorie = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
            return floor(calorie)
        elif self.gender == 'men' and (self.age < 13 or self.age > 80):
            calorie = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)
            return floor(calorie)
        elif self.gender == 'woman' and (self.age < 13 or self.age > 80):
            calorie = 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)
            return floor(calorie)
        else:
            return False

    def reduction_weight(self, percent):
        clr_reduction = self.total_caloric * (1 - percent / 100)
        if clr_reduction < self.ratio_min:
            return floor(self.ratio_min)
        else:
            return floor(clr_reduction)

    def gain_weight(self, percent):
        return self.total_caloric * (1 + percent / 100)

    def data_output(self):
        if self.calorie_goal == "=":
            print(
                f"\n{self.__user_name}: максимальная соточная калорийность для сохранения веса - "
                f"{self.total_caloric} ккал")
        elif self.calorie_goal == "-":
            print(
                f"\n{self.__user_name}: для достижения своей цели необходимо употреблять не более "
                f"{self.reduction_weight(20)} ккал, но и не менее {self.ratio_min} ккал")
        elif self.calorie_goal == "+":
            print(
                f"\n{self.__user_name}: для достижения своей цели необходимо употреблять не менее "
                f"{self.gain_weight(20)} ккал")


user_1_info = Input()

user_1 = UserCal(*user_1_info.list)
user_1.data_output()
