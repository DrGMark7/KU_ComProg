n_partylist = int(input("number of party list: "))
SORWOR = int(input("number of สว."))

SORSOR_by_party,n_way = [],0
for _ in range(n_partylist):
    SORSOR_by_party.append(int(input("number of สส. ที่ชนะในแต่ล่ะพรรค : ")))

def all_possible_groups(elements):
    if not elements:
        return [[]]

    first_element = elements[0]
    rest_of_elements = elements[1:]

    groups_without_first = all_possible_groups(rest_of_elements)
    groups_with_first = []
    for group in groups_without_first:
        groups_with_first.append(group + [first_element])

    return groups_without_first + groups_with_first

Sample_space = all_possible_groups(SORSOR_by_party)

for i in Sample_space:
    if sum(i) >= SORWOR:
        n_way += 1
    else:
        pass

print(f"num of way {n_way}")