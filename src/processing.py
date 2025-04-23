def filter_by_state(list_of_dicts: list[dict], state_value='EXECUTED') -> list[dict]:
    """ Функция возвращает отсортированный список по значению 'EXECUTED',
    или список со значением 'CANCELED', если передан аргумент 'CANCELED'
    """

    filtered_list = []
    if state_value == 'EXECUTED':
        for dict_data in list_of_dicts:
            if dict_data['state'] == 'EXECUTED':
                filtered_list.append(dict_data)
    else:
        for dict_data in list_of_dicts:
            if dict_data['state'] == 'CANCELED':
                filtered_list.append(dict_data)

    return filtered_list

    # Ниже код оформлен через List Comprehension. Ещё не проходили, сделал для тренировки,
    # к тому же программа ругается на возвращаемый из функции тип
    # if state_value == 'EXECUTED':
    #     filtered_list = [dict_data for dict_data in list_of_dicts if dict_data['state'] == 'EXECUTED']
    #     return filtered_list
    #
    # if state_value == 'CANCELED':
    #     filtered_list = [dict_data for dict_data in list_of_dicts if dict_data['state'] != 'EXECUTED']
    #     return filtered_list
