
class Composto:

    __elements = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og")
    __dict = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067, 'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98977, 'Mg': 24.305, 'Al': 26.981538, 'Si': 28.0855, 'P': 30.973761, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078, 'Sc': 44.95591, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938049, 'Fe': 55.845, 'Co': 58.9332, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64, 'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585, 'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42, 'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.90447, 'Xe': 131.293, 'Cs': 132.90545, 'Ba': 137.327, 'La': 138.9055, 'Ce': 140.116, 'Pr': 140.90765, 'Nd': 144.24, 'Pm': 145, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.92534, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04, 'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217, 'Pt': 195.078, 'Au': 196.96655, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.98038, 'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.0381, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 261, 'Db': 262, 'Sg': 266, 'Bh': 264, 'Hs': 277, 'Mt': 268, 'Ds': 281, 'Rg': 272, 'Cn': 285, 'Nh': 286, 'Fl': 289, 'Mc': 289, 'Lv': 293, 'Ts': 294, 'Og': 294}

    def __init__(self, formula):
        self.formula = formula
        self.mm = self.__mm()

    def __split(self):
        for f in self.formula:
            if f not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                return -1
        if self.formula in self.__elements:
            return 1
        splitted = []
        for i in range(len(self.formula)):
            obj = []
            if self.formula[i].isnumeric():
                continue
            if self.formula[i:i+2] in self.__elements and len(self.formula[i:i+2]) > 1:
                try:
                    if (self.formula[i+2].isnumeric()):
                        num = ""
                        j = 0
                        while self.formula[i+2+j].isnumeric():
                            num += (str)(self.formula[i+2+j])
                            j+=1
                            if len(self.formula) <= i+2+j:
                                break
                        obj += [self.formula[i:i+2],(int)(num)]
                    else:
                        obj += [self.formula[i:i+2],1]
                except:
                    obj += [self.formula[i:i+2],1]
            else:
                if self.formula[i:i+1] not in self.__elements:
                    continue
                try:
                    if (self.formula[i+1].isnumeric()):
                        num = ""
                        j = 0
                        while self.formula[i+1+j].isnumeric():
                            num += (str)(self.formula[i+1+j])
                            j+=1
                            if len(self.formula) <= i+1+j:
                                break
                        obj += [self.formula[i:i+1],(int)(num)]
                    else:
                        obj += [self.formula[i:i+1],1]
                except:
                    obj += [self.formula[i:i+1],1]

            splitted += [obj] 
            
        return -1 if splitted == [] else splitted
        
    def __mm(self):
        splitted = self.__split()
        if splitted == 1: 
            return [self.__dict[self.formula], "g/mol"]
        elif splitted == -1:
            raise Exception()
        else:
            mm = 0
            for obj in splitted:
                mm += self.__dict[obj[0]] * obj[1]
            return [mm, "g/mol"]

def App():
    import os
    os.system("CLS")
    while 1:
        formula = input("\n\n - Inserire formula: ")
        if formula in ("-1", "0", "exit", "exit()"):
            os.system("CLS")
            exit()
        try:
            composto = Composto(formula)
            print(" \n - Massa molare di "+formula+": "+ (str)(composto.mm[0]) + " [" + composto.mm[1]+"]")
        except:
            print(" \n - General Error")
        print("\n  __________________________________________________________________")
        print("\n\n", end = " - ")
        os.system("PAUSE")
        os.system("CLS")

if __name__ == "__main__":
    App()
