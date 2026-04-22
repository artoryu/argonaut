languages = ["Python", "Java", "C++", "JavaScript"]

# Вместо создания счетчика i = 0 и i += 1
for index, name in enumerate(languages, start=1):
    print(f"{index}. {name}")

# Вывод:
# 1. Python
# 2. Java
# 3. C++
# 4. JavaScript