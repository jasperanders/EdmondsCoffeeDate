def convert_string_to_nested_list(string_input):
    baseArray = string_input.splitlines()
    result = [[]]

    list_counter = 0
    for i in range(len(baseArray)):
        print(i)
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
