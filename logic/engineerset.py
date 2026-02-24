from dataclasses import dataclass, fields

@dataclass
class EngineerStandard:
    wl635: float = 0
    wl590: float = 0
    wl546: float = 0
    wl465: float = 0
    wl440: float = 0

    @classmethod
    def __init__(self, set_name: str):
        attrs = [f.name for f in fields(self)]
        with open(f"{set_name}.txt") as s:
            absorbances = s.read().splitlines()

        for attr, value in zip(attrs, absorbances):
            setattr(self, attr, value)


    
    def return_attributes(self) -> list[float]:
        return[self.wl635, self.wl590, self.wl546, self.wl465, self.wl440]

    
def createStandard(eng_name, wl635, wl590, wl546, wl465, wl440):
    standard = {
        "wl635": wl635,
        "wl590": wl590,
        "wl546": wl546,
        "wl465": wl465,
        "wl440": wl440
    }
    with open(f"{eng_name}.txt", "w") as file:
        file.write(standard)

def loadStandard( setName: str):
    standard = EngineerStandard()
    return standard.from_file(f"{setName}.txt")