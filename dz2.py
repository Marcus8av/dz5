# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Олег', 'Егор', 'Андрей']
rates = [1000, 2000, 3000]
percentages = ['10.25%', '5%', '20%']

def generate_premiums_dict(names, rates, percentages):
    premiums_dict = {}
    for i in range(len(names)):
        rate = rates[i]
        percentage = float(percentages[i].replace('%', '')) / 100
        premium = rate * percentage
        premiums_dict[names[i]] = premium
    return premiums_dict

premiums_dict = generate_premiums_dict(names, rates, percentages)
print(premiums_dict)