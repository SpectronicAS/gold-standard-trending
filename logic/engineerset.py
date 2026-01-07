from dataclasses import dataclass, fields

@dataclass
class EngineerStandard:
    wl635: float = 0
    wl590: float = 0
    wl546: float = 0
    wl465: float = 0
    wl440: float = 0

    @classmethod
    def from_file(cls, path: str):
        data = {}
        with open(path) as f:
            for line in f:
                if "=" not in line:
                    continue

                key, value = line.strip().split("=")

                if key not in cls.__annotations__:
                    continue
            
                field_type = cls.__annotations__[key]
                data[key] = field_type(value)
        

        return cls(**data)
    
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