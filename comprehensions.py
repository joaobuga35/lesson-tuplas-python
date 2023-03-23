def list_comprehension_exercise_1():
    new_list = [n for n in range(11)]
    return new_list


def list_comprehension_exercise_2():
    new_list = [n for n in range(0, 22) if n % 2 == 0 or n % 3 == 0]
    return new_list


def list_comprehension_exercise_3():
    new_list = [n for n in range(-5, 32) if n % 2 != 0 or n % 5 != 0]
    return new_list
    ...


def list_comprehension_exercise_4():
    new_list = [n**2 for n in range(11)]
    return new_list


def list_comprehension_exercise_5(sentence: str):
    new_list = [letter for letter in sentence if letter.isupper()]
    return new_list


def list_comprehension_exercise_6(sentence: str):
    new_list = [letter for letter in sentence if letter.isupper()]
    return new_list


def list_comprehension_exercise_7(sentence: str):
    new_list = [letter for letter in sentence.split() if letter[0] == 'r' and len(letter) >= 4]
    return new_list
    ...


sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'
sentence_2 = 'o rato rui roeu a roupa do rei de roma'
print(list_comprehension_exercise_7(sentence_2))