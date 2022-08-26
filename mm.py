

class Composto:
    
    # Attributi statici privati
    __elements = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og")
    __dict = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067, 'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98977, 'Mg': 24.305, 'Al': 26.981538, 'Si': 28.0855, 'P': 30.973761, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078, 'Sc': 44.95591, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938049, 'Fe': 55.845, 'Co': 58.9332, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64, 'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585, 'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42, 'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.90447, 'Xe': 131.293, 'Cs': 132.90545, 'Ba': 137.327, 'La': 138.9055, 'Ce': 140.116, 'Pr': 140.90765, 'Nd': 144.24, 'Pm': 145, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.92534, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04, 'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217, 'Pt': 195.078, 'Au': 196.96655, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.98038, 'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.0381, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 261, 'Db': 262, 'Sg': 266, 'Bh': 264, 'Hs': 277, 'Mt': 268, 'Ds': 281, 'Rg': 272, 'Cn': 285, 'Nh': 286, 'Fl': 289, 'Mc': 289, 'Lv': 293, 'Ts': 294, 'Og': 294}

    # Costruttore riceve formula composto
    def __init__(self, formula):
        self.Formula = formula
        self.Mm = self.__mm() # la massa molare (Mm) è un attributo della classe Composto 

    # ESEMPIO  input - output  funzione split:
    # split(CH4) => [['C', 1],['H', 4]]
    # split(CCl3COOH) => [['C', 1], ['Cl', 3], ['C', 1], ['O', 1], ['O', 1], ['H', 1]] 
    
    def __split(self):
        
        # Se ci sono caratteri speciali => errore
        for f in self.Formula:
            if f not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                return -1
        
        # Se formula è un singolo elemento
        if self.Formula in self.__elements:
            return [self.Formula,1]
        
        splitted = []
        
        # Iterazione formula
        for i in range(len(self.Formula)):

            obj = []

            # Se trova numero salta il giro
            if self.Formula[i].isnumeric():
                continue
            
            # Se nelle posizioni [i, i+2] è contenuto un elemento.. (elemento con due lettere) 
            if self.Formula[i:i+2] in self.__elements and len(self.Formula[i:i+2]) > 1:

                # Il try except serve per catturare l'eccezione in questo caso l'overflow (quando i+2 va oltre index dell'array)
                try:
                    # Se dopo l'elemento di 2 lettere c'è un numero (atomo), trova le n cifre (solitamente solo una)
                    if (self.Formula[i+2].isnumeric()):
                        num = ""
                        j = 0
                        while self.Formula[i+2+j].isnumeric():
                            num += (str)(self.Formula[i+2+j])
                            j+=1
                            if len(self.Formula) <= i+2+j:
                                break
                        obj += [self.Formula[i:i+2],(int)(num)]

                    # Niente numeri allora si avrà esempio: Na con 1 solo atomo
                    else:
                        obj += [self.Formula[i:i+2],1]
                
                # C'è stato un overflow, significa che dopo l'elem non ci sono cifre, allora ci sarà solo 1 atomo
                except:
                    obj += [self.Formula[i:i+2],1]
            
            # Altrimenti potrebbe essere elemento con una lettera
            else:
                # Niente elementi trovati => salta il giro
                if self.Formula[i:i+1] not in self.__elements:
                    continue
                    
                # Il try except serve per catturare l'eccezione in questo caso l'overflow (quando i+1 va oltre index dell'array)
                try:

                    # Se dopo l'elemento di 1 lettera c'è un numero (atomo), trova le n cifre (solitamente solo una)
                    if (self.Formula[i+1].isnumeric()):
                        num = ""
                        j = 0
                        while self.Formula[i+1+j].isnumeric():
                            num += (str)(self.Formula[i+1+j])
                            j+=1
                            if len(self.Formula) <= i+1+j:
                                break
                        obj += [self.Formula[i:i+1],(int)(num)]
                    
                    # Niente numeri allora si avrà esempio: C con 1 solo atomo
                    else:
                        obj += [self.Formula[i:i+1],1]
                    
                # C'è stato un overflow, significa che dopo l'elem non ci sono cifre, allora ci sarà solo 1 atomo 
                except:
                    obj += [self.Formula[i:i+1],1]

            # Concateno l'oggetto (obj) [elemento, numero atomi] all'array con tutta la formula
            splitted += [obj] 
        
        # Se non sono stati trovati elementi ritorna errore (-1) altrimenti ok
        return -1 if splitted == [] else splitted
    
    def __semplifica(self, f):
        buffer = []
        visited = []
        for i in range(len(f)):
            atm = f[i][1]
            if f[i][0] in visited:
                continue
            visited += f[i][0]
            for j in range(i+1,len(f)):
                if f[i][0] == f[j][0]:
                    atm += f[j][1]
            buffer += [[f[i][0], atm]]

        f = buffer
        del buffer
        return f

    # Calcola la massa molare partendo dalla formula splittata
    def __mm(self):
        splitted = self.__semplifica(self.__split())
        if splitted == -1:
            raise Exception()
        else:
            mm = 0
            self.Formula = "" # Ricalcola la formula del composto in base agli elementi trovati dal metodo split
            for obj in splitted:
                mm += self.__dict[obj[0]] * obj[1]
                self.Formula += obj[0]
                self.Formula += (str)(obj[1]) if obj[1] > 1 else ""
            return {"Val":mm, "Unit":"g/mol"}

#---------------------------------------------------------------------------------------------------------------------------------------

import os

def App():
    os.system("CLS")
    while 1:
        formula = input("\n\n - Inserire formula: ")
        if formula in ("0", "exit"):
            os.system("CLS")
            exit()
        try:
            composto = Composto(formula) # Crea istanza da classe Composto
            print(" \n - Massa molare di "+composto.Formula+": "+ (str)(composto.Mm["Val"]) + " [" + composto.Mm["Unit"]+"]")
        except:
            print(" \n - General error")
        print("\n __________________________________________________________________")
        print("\n\n", end = " - ")
        os.system("PAUSE")
        os.system("CLS")

#---------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    App()
