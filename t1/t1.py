def total_salary(path:str)-> int:
    try: 
        with open(path, "r+", encoding="utf-8") as file :
            ttl_salary = 0 
            salaries_num = 0
            average_salary = 0
        
            for line in file : 
                _, salary= line.split (',')
                ttl_salary += int(salary.strip()) 
                salaries_num += 1
            average_salary = ttl_salary // salaries_num
            print(f"Загальна сума заробітної плати: {ttl_salary}, Середня заробітна плата: {average_salary}")
            return (ttl_salary, average_salary)
    except FileNotFoundError:
      print("Файл не знайдено.")
      return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0
total_salary("C:/Users/1/OneDrive/Рабочий стол/progects/vsc-basics/.vscode/goit-pycore-hw-04/t1.py/t1.data.txt")

