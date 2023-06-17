from math import floor

gender_user = input("Ваш пол (м/ж): ").lower()
age_user = int(input("Ваш возраст: "))
weight_user = int(input("Ваш вес: "))
height_user = int(input("Ваш рост: "))


class UserCal:
    gender = gender_user

    def __init__(self):
        self.gender = self.__examination_gender()
        self.age = age_user
        self.weight = weight_user
        self.height = height_user

    @classmethod
    def __examination_gender(cls):
        if cls.gender == 'м' or cls.gender == 'мужской' or cls.gender == 've;crjq' or cls.gender == 'v':
            return 1
        elif cls.gender == 'ж' or cls.gender == 'женский' or cls.gender == ';tycrbq' or cls.gender == ';':
            return 2

    def daily_calorie(self):
        if self.gender == 1 and 13 <= self.age <= 80:
            calorie = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
            return floor(calorie)
        elif self.gender == 2 and 13 <= self.age <= 80:
            calorie = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
            return floor(calorie)
        elif self.gender == 1 and (self.age < 13 or self.age > 80):
            calorie = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)
            return floor(calorie)
        elif self.gender == 2 and (self.age < 13 or self.age > 80):
            calorie = 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)
            return floor(calorie)
        else:
            return False


def calories_per_activity():
    activ = int(input(
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
    ))
    if activ == 1:
        return 1.4
    elif activ == 2:
        return 1.6
    elif activ == 3:
        return 1.9
    elif activ == 4:
        return 2
    elif activ == 5:
        return 2.2


alexey = UserCal()
print(alexey.__dict__)
print(alexey.daily_calorie())
