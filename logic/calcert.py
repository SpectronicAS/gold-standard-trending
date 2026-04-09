from logic.engineerset import EngineerStandard, loadStandard
from logic.fileprocessor import wavelengthResults, absorbanceResults, parseFile
from dataclasses import dataclass, fields, asdict

class Calcert():
    wl1: float
    wl2: float
    wl3: float
    wl4: float
    wl5: float
    abs1: float
    abs2: float
    abs3: float
    abs4: float
    abs5: float
    setname: str
    result: str

    def __init__(self, data: dict, set: str):
        self.calcert(data["wl_file_path"], data["abs_file_path"], set)
    
    def calcert(self, wl_filepath, abs_filepath, set_name: str):
        setattr(self, "setname", set_name)
        standard = EngineerStandard(set_name).return_attributes()
        setattr(self, "result", "Pass")
        wl_results = wavelengthResults(parseFile(wl_filepath))
        abs_results = absorbanceResults(parseFile(abs_filepath))
        wl_standard = self.loadWavelengths()
        self.populate(self, wl_results, abs_results)
        for i, value in enumerate(wl_results):
            if abs(value - float(wl_standard[i])) > 1:
                result = "Fail"
                setattr(self, "result", result)
        for i, value in enumerate(abs_results):
            if abs(value - float(standard[i])) > 0.01:
                result = "Fail"
                setattr(self, "result", result)
       
    def populate(self, wavelengths, absorbances):
        attrs = [f.name for f in fields(self)]

        for attr, value in zip(attrs[:5], wavelengths):
            setattr(self, attr, value)

        for attr, value in zip(attrs[5:10], absorbances):
            setattr(self, attr, value)

    def loadWavelengths():
        with open("wavelengths.txt") as f:
            wavelengths = f.read().splitlines()
        return wavelengths
    
    def return_dict(self):
        return asdict(self)

class Variances():
    wl1: float
    wl2: float
    wl3: float
    wl4: float
    wl5: float
    abs1: float
    abs2: float
    abs3: float
    abs4: float
    abs5: float

