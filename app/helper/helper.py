from __init__ import mode_auto, matchings_amount
from coffedatematching import compute_coffee_dates


def convert_string_to_nested_list(string_input):
    baseArray = string_input.splitlines()
    result = [[]]

    list_counter = 0
    for i in range(len(baseArray)):
        if baseArray[i] == "":
            list_counter += 1
            result.append([])
        else:
            result[list_counter].append(baseArray[i])

    return result


def convert_matchings_to_string(matchings):
    result = ""
    for i, match in enumerate(matchings):
        result += f"{i+1}.\n"
        for date in match.keys():
            result += f"@{date} & @{match[date]}\n"
        result += "\n"
    return result


def match(
    groups_sting: str,
    matchings_amount: int = 3,
):
    """
    Match a
    """
    print(groups_sting)
    print("----")
    return compute_coffee_dates(
        convert_string_to_nested_list(groups_sting), matchings_amount
    )


def cleanup(user_id):
    mode_auto[user_id] = None
    matchings_amount[user_id] = None
