def filter_by_state(list_of_dicts: list[dict], state_value: str = 'EXECUTED') -> list[dict]:
    """ Функция возвращает отсортированный список по значению 'EXECUTED',
    или список со значением переданным в state_value.
    """

    filtered_list = []
    if state_value == 'EXECUTED':
        for dict_data in list_of_dicts:
            if dict_data.get('state') == 'EXECUTED':
                filtered_list.append(dict_data)
    else:
        for dict_data in list_of_dicts:
            if dict_data.get('state') == state_value:
                filtered_list.append(dict_data)

    return filtered_list


def sort_by_date(list_of_dicts: list[dict], sort_arg: bool = True) -> list[dict]:
    """ Функция возвращает отсортированный по дате список(по умолчанию-по убыванию,
    или по возрастанию, если в параметр со значением по умолчанию введено False)."""

    new_list = []

    for dicts in list_of_dicts:
        if 'date' in dicts:
            if dicts['date']:
                new_list.append(dicts)

    if sort_arg:
        sorted_list = sorted(new_list, key=lambda d: d['date'], reverse=True)
    else:
        sorted_list = sorted(new_list, key=lambda d: d['date'])

    return sorted_list
