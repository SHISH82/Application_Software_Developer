# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, Divider=","):
    participants1 = group1.split(Divider)
    participants2 = group2.split(Divider)
    common_participants = list(set(participants1) & set(participants2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, Divider="|")

print(common_participants)