from logic.coffedatematching import compute_coffee_dates


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


def matchings_from_string(
    groups_sting: str,
    matchings_amount: int = 3,
):
    """
    Match a group sting.
    """
    print(groups_sting)
    print("----")
    return convert_matchings_to_string(
        compute_coffee_dates(
            convert_string_to_nested_list(groups_sting), matchings_amount
        )
    )


def generate_per_user_matches(matchings):
    """
    in: [
        {"Jasper Anders": "Pert", "Bob": "Hannes von Boetticher"},
        {"Jasper Anders": "Bob", "Pert": "Hannes von Boetticher"},
    ]

    out: {
        "Jasper Anders": ["Pert", "Bob"],
        "Pert": ["Jasper Anders", "Hannes von Boetticher"],
        "Bob": ["Hannes von Boetticher", "Jasper Anders"],
        "Hannes von Boetticher": ["Bob", "Pert"]
    }
    """

    result = {}

    for matching in matchings:
        for date in matching:
            result[date] = [] if result.get(date) is None else None
            result[matching[date]] = [] if result.get(date) is None else None

            result[date].append(matching[date])
            result[matching[date]].append(date)
