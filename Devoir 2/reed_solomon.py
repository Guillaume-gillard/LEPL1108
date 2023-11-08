import numpy as np 

class Translation():

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            str_bin (string): Forme binaire de l'entier en string.
        """
        str_bin =''.join(str(1 & int(n) >> i) for i in range(8)[::-1])
        return str_bin

    def toInt(self, str_bin):
        """
        Convertit un string contenant la séquence sur un octet (ou 8 bits) en un entier n.

        Args:
            str_bin (string): Forme binaire de l'entier en string.
        Returns:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        """
        n = int(str_bin, 2)
        return n

    def translateToMachine(self, phrase):
        """
        Convertit une phrase (encodée comme un string) en une liste de strings d'octets (ou 8 bits).

        Args:
            phrase (string): Phrase en français ou en anglais.
        Returns:
            phrase_bin (list of strings): Liste de strings, chaque string représente un octet/8 bits
        """
        phrase_bin = [self.toBinary(ord(char)) for char in phrase]
        return phrase_bin

    def translateToHuman(self, bin_phrase):
        """
        Convertit une liste de strings d'octets (ou 8 bits) en une phrase (encodée comme un string).

        Args:
            bin_phrase (list of strings): Liste de strings, chaque string représente un octet/8 bits
        Returns:
            phrase (string): Phrase en français ou en anglais.
        """
        phrase = ""
        for bin_str in bin_phrase:
            phrase += chr(self.toInt(bin_str))
        return phrase


class BinaryDomains():

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            string: Forme binaire de l'entier en string.
        """
        return ''.join(str(1 & int(n) >> i) for i in range(8)[::-1])

    def add(self, x, y):
        """
        Additionne deux séquences binaires (x+y) reçues sous la forme de string.

        Example : "10111001" + "10010100" = "00101101".

        Args:
            x (string): Premier élément de l'addition.
            y (string): Deuxième élément de l'addition.

        Returns:
            string: Résultat de l'addition x+y en binaire.
        """
        # BEGIN TODO
        add_str = ""
        for i in range(len(x)):
            if x[i] == y[i]:
                add_str += "0" 
            else :
                add_str += "1" 
        return add_str
        # END TODO

    def multiply(self, x, y, pol):
        """
        Multiplie deux séquences binaires (x*y) reçues sous la forme de string, en utilisant
        le polynôme irréductible choisi pour le corps.

        Example : "10111001" * "10010100" = "10110010" avec comme pol: "101001101"

        Args:
            x (string): Premier élément de la multiplication.
            y (string): Deuxième élément de la multiplication.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de la multiplication x*y en binaire.
        """
        # BEGIN TODO
        #### Utilisation de l'ia Copilot comme aide pour rédiger cette fonction ####
        # Converting the binary representation to integers
        x_int = int(x, 2)
        y_int = int(y, 2)
        pol_int = int(pol, 2)
        result_int = 0

        # Executing the algorithm
        # We will use bitwise opperation on int for ex += => ^=, *= => <<=, /= => >>=, % => &=
        while y_int > 0:
            # if y0 = 1
            if y_int & 1:
                result_int ^= x_int # X0R operation = to addition in the binary field => result_int = result_int + x_int
            x_int <<= 1 # Left shift of x_int => x_int = x_int * X where X is "10"
            y_int >>= 1 # Right shift of y_int => y_int = y_int / X where X is "10"

            # Si le bit le plus significatif de x est 1, effectuer la réduction avec le polynôme
            if x_int & (1 << (len(pol) - 1)):
                x_int ^= pol_int
        # Converting result to binary form 
        result_binary = bin(result_int)[2:] # [2:] to remove the "0b" at the beginning of the string
        return result_binary.zfill(len(pol) - 1) # zfill to add 0 at the beginning of the string if needed
        # END TODO




    def inverse(self, x, pol):
        """
        Inverse un élément (x^(-1)) du corps donné sous la forme d'une séquence binaire.

        Example : ("10111001")^(-1) = "10001110" avec comme pol: "101001101"

        Args:
            x (string): Elément à inverser.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de l'inversion en binaire.
        """
        # BEGIN TODO
        l = []
        pol_int = int(pol, 2)
        l.append(self.multiply(x, x, pol))
        x_inverse = bin(1)[2:]
        for i in range(1, 7):
            l.append(self.multiply(l[i - 1], l[i - 1], pol))
        for j in l:
            x_inverse = self.multiply(x_inverse, j, pol)
        # no need to reduce the result because multiply return a result in the born of the polynom :))))
        return x_inverse.zfill(len(pol) - 1)
        # END TODO


class ReedSolomon():
    def __init__(self, k, n, y, pol):
        """
        Args:
            k (int): dimension des messages à transmettre.
            n (int): taille du bloc que l'on souhaite transmettre.
            x (liste de string de taille n): les points Xi.
            pol (string): polynome irréductible.
        """
        self.f = BinaryDomains()
        self.t = Translation()
        self.k = k
        self.n = n
        self.y = y
        self.pol = pol

    def _evaluate(self, polynome, x):
        y = polynome[-1]
        for i in range(len(polynome) - 2, -1, -1):
            y = self.f.add(self.f.multiply(y, x, self.pol), polynome[i])
        return y

    def encoding(self, message_original):
        """
        Encode le message à stocker sous la forme d'une liste comportant n bytes/octets.

        Args:
            message_original (string): Le message original a encodé.

        Returns:
            (liste de string de taille n): Le message encodé.
        """
        # BEGIN TODO
        encoded_message = [self._evaluate(self.t.translateToMachine(message_original), Yi) for Yi in self.y]
        return encoded_message
        # END TODO

    def gaussian_elimination(self, y, Iy):
        """
        Ex: k = 4: retourne les coefficients (ai) de la fonction I(yi) = a0 + a1*yi + a2*yi^2 + a3*yi^3
        en partant de 4 points (ai,I(yi)).

        Ce problème est généralisé pour tout k.
        Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Va = I.
        Avec V la matrice de Vandermonde.

        Args:
            y (liste de string de taille k): Les points yi.
            Iy (liste de string de taille k): Les points I(yi).

        Returns:
            (liste de string de taille k): Les coefficients (ai) de l'interpolation.
        """
        """
        if i != j:
                    y[i] = self.f.add(self.f.multiply(y[i], y[j], self.pol), Iy[j])
        """
        # BEGIN TODO
        k = len(y)
        a = [0] * k
        P = []
        # initizaling P
        for i in range(k):
            P.append([])
            P[i] = [0] * (k+1)
        for i in range (k): 
            P[i][0] = self.t.toBinary(1)
            P[i][1] = y[i]
            P[i][-1] = Iy[i]
            for j in range (2, k):
                P[i][j] = self.f.multiply(P[i][j - 1], y[i], self.pol)    
        
        for i in range (k):
            for j in range (k):
                if i != j :
                    r = self.f.multiply(P[j][i], self.f.inverse(P[i][i], self.pol), self.pol)
                    for m in range(k+1):
                        P[j][m] = self.f.add(P[j][m], self.f.multiply(r, P[i][m], self.pol))
        for i in range(k):
            a[i] = self.f.multiply(P[i][k], self.f.inverse(P[i][i], self.pol), self.pol)
        print(a)
        return a
        # END TODO

    def decoding(self, message_corrupted):
        """
        Décode le message corrompu sous la forme d'une liste comportant k bytes.

        Args:
            message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.

        Returns:
            (bool): True s'il est possible de décoder le message corrompu, False sinon.
            (liste de string de taille k): Le message décodé. (si bool = False, alors retourner []).
        """
        # BEGIN TODO
        char_corrupted = 0
        to_translate = []
        y_to_translate = []
        for i in range(len(message_corrupted)):
            if "x" in message_corrupted[i] :
                char_corrupted += 1
            else : 
                to_translate.append(message_corrupted[i])
                y_to_translate.append(self.y[i])
        if char_corrupted > self.n - self.k :
            return False, []
        else :
            a = self.gaussian_elimination(y_to_translate, to_translate)
            message_decoded = self.t.translateToHuman(a)
            print(message_decoded.strip())
            return True, [message_decoded]
        # END TODO
