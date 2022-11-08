global mode_auto
mode_auto = {}
global matchings_amount
matchings_amount = {}


def cleanup(user_id):
    # print("hi")
    global mode_auto
    global matchings_amount
    mode_auto[user_id] = None
    matchings_amount[user_id] = None
