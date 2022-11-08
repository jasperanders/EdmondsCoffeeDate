from slackbot import compute_coffee_dates


def test_basic_matching():
    Groups = []
    
    num_groups = 5
    num_per_group = 6

    group_count = 0
    member_count = 0
    bob_counter = 0

    while group_count < num_groups:
        group = []
        member_count = 0
        while member_count < num_per_group:
            group.append(f"Bob {bob_counter}")
            member_count += 1
            bob_counter += 1
        Groups.append(group)
        group_count += 1

    num_matches = 4
    dates = compute_coffee_dates(Groups, num_matches)
    # check if there are two set of dates are generated
    assert len(dates) == num_matches

    # check if each match has  matches
    for match in dates:
        assert len(match) == num_per_group * num_groups / 2

    flat = {}
    for match in dates:
        flat = flat | match

    print(flat)
    assert len(flat) == num_matches * num_groups * num_per_group / 2