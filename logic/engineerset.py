import json
from dataclasses import dataclass, fields
from pathlib import Path

@dataclass
class EngineerStandard:
    wl635: float = 0
    wl590: float = 0
    wl546: float = 0
    wl465: float = 0
    wl440: float = 0

    @classmethod
    def from_file(cls, path: Path) -> "EngineerStandard":
        if not path.exists():
            return cls()
        
        with path.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        
        valid_keys = {f.name for f in fields(cls)}
        data = {k: v for k, v in raw.items() if k in valid_keys}

        return cls(**data)
    
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

