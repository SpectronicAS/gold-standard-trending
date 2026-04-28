from logic.engineerset import EngineerStandard, loadStandard
from logic.fileprocessor import wavelengthResults, absorbanceResults, parseFile

class Calcert:
    def __init__(self, data: dict, set):
        
        self.wl1 = None
        self.wl2 = None
        self.wl3 = None
        self.wl4 = None
        self.wl5 = None
        self.abs1 = None
        self.abs2 = None
        self.abs3 = None
        self.abs4 = None
        self.abs5 = None
        self.setname = set
        self.result = "Pass"
        self.errors = None


    def calcert(self, wl_filepath, abs_filepath, set_name):
        errors = []
        errors_dict = {}
        standard = EngineerStandard(self.setname).return_attributes()
        wl_results = wavelengthResults(parseFile(wl_filepath))
        abs_results = absorbanceResults(parseFile(abs_filepath))
        wl_standard = self.loadWavelengths()
        self.assign_list(wl_results, ["wl1", "wl2", "wl3", "wl4", "wl5"])
        self.assign_list(abs_results, ["abs1", "abs2", "abs3", "abs4", "abs5"])
        for i, value in enumerate(wl_results):
            if abs(value - float(wl_standard[i])) > 1:
                result = "Fail"
                setattr(self, "result", result)
                errors.append(value - float(wl_standard[i]))
        for i, value in enumerate(abs_results):
            if abs(value - float(standard[i])) > 0.01:
                result = "Fail"
                setattr(self, "result", result)
                errors.append(value - float(wl_standard[i]))
        for i, error in enumerate(errors):
            if i < 5:
                errors_dict[f"wl{i+1}"] = error
            else:
                errors_dict[f"abs{i+1}"] = error
        setattr(self, "errors", errors_dict)
    
    def assign_list(self, values, attrs):
        for attr, value in zip(attrs, values):
            setattr(self, attr, value)

    def loadWavelengths(self):
        with open("wavelengths.txt") as f:
            wavelengths = f.read().splitlines()
        return wavelengths
