time = int(input("Введите время в секундах: "))
days = time // 86400
hours = (time % 86400) // 3600
minutes = ((time % 86400) % 3600) // 60
seconds = ((time % 86400) % 3600) % 60

print(days, "дней", hours, "часов", minutes, "минут", seconds, "секунд")
