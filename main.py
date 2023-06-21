from math import floor


class UserCal:

    def __init__(self):
        self.user_name = input("Ваше имя: ").capitalize()
        self.gender = self.__get_gender(input("Ваш пол (м/ж): ").lower())
        self.age = int(input("Ваш возраст: "))
        self.weight = float(input("Ваш вес: "))
        self.height = int(input("Ваш рост: "))
        self.activ = self.__get_activity(int(input(
            "1 - Незначительная физическая нагрузка\n"
            "\tЧеловек редко прилагает физические усилия, не ходит пешком на большие расстояния,\n"
            "\tне занимается спортом, работает в офисе за компьютером, досуг проводит неактивно:\n"
            "\tчитает, общается в социальных сетях, смотрит телевизор.\n"

            "2 - Легкая физическая нагрузка\n"
            "\tЧеловек, испытывающий умеренные физические нагрузки на работе или ведущий в целом\n"
            "\tмалоподвижный образ жизни, но периодически занимающийся спортом. Например:\n"
            "\t- Офисный работник, занимающийся бегом или велоспортом в среднем 1 час не менее 3-х раз в неделю;\n"
            "\t- Рабочие не тяжелых производств;\n"

            "3 - Средняя физическая нагрузка\n"
            "\tЛюди, занятые физическим трудом:\n"
            "\t- Рабочие не тяжелых производств;\n"
            "\t- Люди, занимающиеся бегом или велоспортом не менее 1 часа ежедневно.\n"

            "4 - Выраженная физическая нагрузка\n"
            "\tЛюди, занятые многочасовым физическим трудом или спортсмены, а именно:\n"
            "\t- Профессиональные танцоры;\n"
            "\t- Работники, производящие сельскохозяйственные не механизированные работы.\n"

            "5 - Тяжелая физическая нагрузка\n"
            "\tЛюди, занятые тяжелым немеханизированным трудом, спортсмены. Сюда входят:\n"
            "\t- Артисты классического балета;\n"
            "\t- Профессиональные спортсмены в период активных тренировок и соревнований.\n"
            "\nВЫБЕРИТЕ ТОТ НОМЕР КОТОРЫЙ ПОДХОДИТ ВАМ: "
        )))
        self.caloric = self.daily_calorie()
        self.total_caloric = floor(self.activ * self.caloric)
        self.ratio_min = floor(self.weight / (0.45 * 8))

    @classmethod
    def __get_activity(cls, x):
        if x == 1:
            return 1.4
        elif x == 2:
            return 1.6
        elif x == 3:
            return 1.9
        elif x == 4:
            return 2
        elif x == 5:
            return 2.2

    @classmethod
    def __get_gender(cls, x):
        if x in ('v', 'мужской', 'м'):
            return 'men'
        elif x in (';', 'женский', 'ж'):
            return 'woman'

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

    def data_output(self, user):
        if calorie_goal == "=":
            print(
                f"\n{self.user_name}: максимальная соточная калорийность для сохранения веса - {self.total_caloric} ккал")
        elif calorie_goal == "-":
            print(
                f"{self.user_name}: для достижения своей цели необходимо употреблять не более {self.reduction_weight(20)},"
                f"но и не менее {self.ratio_min} ккал")
        elif calorie_goal == "+":
            print(
                f"{self.user_name}: для достижения своей цели необходимо употреблять не менее {self.gain_weight(20)} ккал")


user_1 = UserCal()

calorie_goal = input("= сохранить вес\n+ набрать вес\n- уменьшить вес\nВВЕДИТЕ ВАШУ ЦЕЛЬ: ")

