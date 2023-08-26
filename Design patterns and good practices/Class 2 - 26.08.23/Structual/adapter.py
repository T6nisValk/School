class Elf:
    def nall_nin(self):
        print("Elf says: Calling the overlord...")


class Dwarf:
    def estver_narbo(self):
        print("Dwarf says: Calling the overlord...")


class Human:
    def ring_mig(self):
        print("Human says: Calling the overlord...")


class ElfAdapter:
    def __init__(self, elf) -> None:
        self.elf = elf

    def call_me(self):
        self.elf.nall_nin()


class DwarfAdapter:
    def __init__(self, dwarf) -> None:
        self.dwarf = dwarf

    def call_me(self):
        self.dwarf.estver_narbo()


class HumanAdapter:
    def __init__(self, human) -> None:
        self.human = human

    def call_me(self):
        self.human.ring_mig()


minions = [ElfAdapter(Elf()), DwarfAdapter(Dwarf()), HumanAdapter(Human())]
for minion in minions:
    minion.call_me()
