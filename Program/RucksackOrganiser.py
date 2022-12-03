class RucksackOrganiser():

    def __init__(self):
        self.data = []

    def read_data(self, filename):
        f = open(filename, "r")
        for l in f:
            self.data.append(list(l.strip()))
        f.close()
    
    def get_val(self, item):
        if('a' <= item <= 'z'):
            return ord(item) - 96
        else:
            return ord(item) - 38

    def get_containers_common(self, container_tuple):
        return list(set(container_tuple[0]).intersection(container_tuple[1]))

    # splits into two halves
    def get_containers(self, rucksack):
        return ( rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:])

    def get_common_item_priority_sum(self):
        sum = 0
        for rucksack in self.data:
            common = self.get_containers_common(self.get_containers(rucksack))
            for item in common:
                sum += self.get_val(item)
        return sum

    def get_groups_common(self, rucksack_triple):
        return list(set(rucksack_triple[0]).intersection(rucksack_triple[1]).intersection(rucksack_triple[2]))

    def get_groups(self):
        groupList = []
        group = []

        for rucksack in self.data:
            group.append(rucksack)
            if len(group) == 3:
                groupList.append(group)
                group = []

        return groupList

    def get_group_item_priority_sum(self):
        groupsList = self.get_groups()
        sum = 0
        for group in groupsList:
            common = self.get_groups_common(group)
            for badge in common:
                sum += self.get_val(badge)
        return sum