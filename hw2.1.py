def read_cook_book():
  cook_book = {}
  with open('cookbook.txt') as f:
    for line in f:
      dish_name = line.strip().lower()
      num_ingridients = int(f.readline())
      ingridients = []
      for num in range(num_ingridients):
        ingridient_to_list = f.readline().split('|')
        ingridient_to_dict = {'ingridient_name': ingridient_to_list[0].strip().lower(),\
                              'quantity': int(ingridient_to_list[1].strip()),\
                              'measure': ingridient_to_list[2].strip().lower()}
        ingridients.append(ingridient_to_dict)
      cook_book.update({dish_name: ingridients})
      f.readline()
  return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list(cook_book):
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)

create_shop_list(read_cook_book())