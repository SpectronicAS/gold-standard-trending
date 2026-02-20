from logic.engineerset import EngineerStandard, loadStandard
from logic.fileprocessor import wavelengthResults, absorbanceResults, parseFile
from dataclasses import dataclass, fields

@dataclass
class Calcert:
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
    
    @classmethod
    def calcert(cls, wl_filepath, abs_filepath, setName: str):
        cls.setname = setName
        standard = loadStandard(setName).return_attributes()
        result = "Pass"
        wl_results = wavelengthResults(parseFile(wl_filepath))
        abs_results = absorbanceResults(parseFile(abs_filepath))
        wl_standard = cls.loadWavelengths()
        cls.populate(wl_results, abs_results)
        for i, value in enumerate(wl_results):
            if abs(value - wl_standard[i]) > 1:
                result = "Fail"
                cls.result = result
        for i, value in abs_results:
            if abs(value-standard[i]) > 0.01:
                result = "Fail"
                cls.result = result
            
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
