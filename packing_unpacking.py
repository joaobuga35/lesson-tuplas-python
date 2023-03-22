def sum_numbers(*args):
    acumulador = 0
    for arg in args:
        acumulador = arg + acumulador
    return acumulador


numbers = [1, 2, 3, 4, 5, 6]


def get_multiplied_amount(multiplier: int, *args):
    acumulador = 0
    for arg in args:
        acumulador = arg + acumulador
    return acumulador * multiplier


numbers_2 = [1, 2, 3]


def word_concatenator(*args):
    new_word = ' '.join(args)
    return new_word


def word_concatenator_2(*args):
    new_arg = []
    for arg in args:
        new_arg.append(arg[::-1])   
    return new_arg


words = ["Tá", "pegando", "fogo", "bicho!!!"]


def dicionary_separator(**kwargs):
    list_values = []
    list_keys = []
    for key, values in kwargs.items():
        list_keys.append(key)
        list_values.append(values)
    
    return list_keys, list_values


user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}
item = dicionary_separator(**user)


def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    new_model = {} 
    for key, value in enumerate(kwargs.values()):
        new_key = args[key]
        new_values = value
        new_model[new_key] = new_values
    return new_model


change_keys = ["username", "password", "address"]
user = {"name": "Williams", "some_key": "1234"}
result = dictionary_creator(*change_keys, **user)


def purchase_logger(**kwargs):
    return f"""{kwargs['quantity']} {kwargs['name']} bought by {kwargs['price']}"""


purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}


def world_cup_logger(country, *args):
    new_list = []

    for arg in sorted(args):
        new_list.append(arg)
    
    formatted_string = ''.join(str(new_list))
    return f'{country} - {formatted_string}'


country_1 = 'Alemanha'
year_list = [2014, 1990, 1974, 1954]

print(world_cup_logger(country_1, *year_list))
"""print(sum_numbers(*numbers))
print(purchase_logger(**purchase))
print(result)
print(get_multiplied_amount(2, *numbers_2))
print(word_concatenator(*words))
print(word_concatenator_2(*words))
print(item)"""