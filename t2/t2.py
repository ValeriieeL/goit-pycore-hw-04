def get_cats_info(path):
  try:
      with open(path, 'r+') as file:
        cats_list = []
        for line in file:
          cat_id, cat_name, cat_age = line.strip().split(',')
          cats_list.append({'id': cat_id, 'name': cat_name, 'age': cat_age })
        print(cats_list)
        return cats_list
  except FileNotFoundError:
        print("Файл не знайдено.")
        return []
  except Exception as e:
        print(f"Помилка: {e}")
        return []
get_cats_info('C:/Users/1/OneDrive/Рабочий стол/progects/vsc-basics/.vscode/goit-pycore-hw-04/t2.py/t2.data.txt')