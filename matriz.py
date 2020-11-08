# Resultado: 1 28 6 12 9 26 3 29 5 21 2 20 10 4 15 18 14 17 22 11 19 25 7 23 8 27 16 13 24

class ExampleMatrix:

    def __init__(self):
        self.matrix = None
        self.tri_matrix = [
            [  97, 205, 139,  86,  60, 220,  65, 111, 115, 227,  95,  82, 225, 168, 103, 266, 205, 149, 120,  58, 257, 152,  52, 180, 136,  82,  34, 145 ],
            [ 129, 103,  71, 105, 258, 154, 112,  65, 204, 150,  87, 176, 137, 142, 204, 148, 148,  49,  41, 211, 226, 116, 197,  89, 153, 124,  74 ],
            [ 219, 125, 175, 386, 269, 134, 184, 313, 201, 215, 267, 248, 271, 274, 236, 272, 160, 151, 300, 350, 239, 322,  78, 276, 220,  60 ],
            [ 167, 182, 180, 162, 208,  39, 102, 227,  60,  86,  34,  96, 129,  69,  58,  60, 120, 119, 192, 114, 110, 192, 136, 173, 173 ],
            [  51, 296, 150,  42, 131, 268,  88, 131, 245, 201, 175, 275, 218, 202, 119,  50, 281, 238, 131, 244,  51, 166,  95,  69 ],
            [ 279, 114,  56, 150, 278,  46, 133, 266, 214, 162, 302, 242, 203, 146,  67, 300, 205, 111, 238,  98, 139,  52, 120 ],
            [ 178, 328, 206, 147, 308, 172, 203, 165, 121, 251, 216, 122, 231, 249, 209, 111, 169,  72, 338, 144, 237, 331 ],
            [ 169, 151, 227, 133, 104, 242, 182,  84, 290, 230, 146, 165, 121, 270,  91,  48, 158, 200,  39,  64, 210 ],
            [ 172, 309,  68, 169, 286, 242, 208, 315, 259, 240, 160,  90, 322, 260, 160, 281,  57, 192, 107,  90 ],
            [ 140, 195,  51, 117,  72, 104, 153,  93,  88,  25,  85, 152, 200, 104, 139, 154, 134, 149, 135 ],
            [ 320, 146,  64,  68, 143, 106,  88,  81, 159, 219,  63, 216, 187,  88, 293, 191, 258, 272 ],
            [ 174, 311, 258, 196, 347, 288, 243, 192, 113, 345, 222, 144, 274, 124, 165,  71, 153 ],
            [ 144,  86,  57, 189, 128,  71,  71,  82, 176, 150,  56, 114, 168,  83, 115, 160 ],
            [  61, 165,  51,  32, 105, 127, 201,  36, 254, 196, 136, 260, 212, 258, 234 ],
            [ 106, 110,  56,  49,  91, 153,  91, 197, 136,  94, 225, 151, 201, 205 ],
            [ 215, 159,  64, 126, 128, 190,  98,  53,  78, 218,  48, 127, 214 ],
            [  61, 155, 157, 235,  47, 305, 243, 186, 282, 261, 300, 252 ],
            [ 105, 100, 176,  66, 253, 183, 146, 231, 203, 239, 204 ],
            [ 113, 152, 127, 150, 106,  52, 235, 112, 179, 221 ],
            [  79, 163, 220, 119, 164, 135, 152, 153, 114 ],
            [ 236, 201,  90, 195,  90, 127,  84,  91 ],
            [ 273, 226, 148, 296, 238, 291, 269 ],
            [ 112, 130, 286,  74, 155, 291 ],
            [ 130, 178,  38,  75, 180 ],
            [ 281, 120, 205, 270 ],
            [ 213, 145,  36 ],
            [  94, 217 ],
            [ 162 ],
            []
        ]

    def setTriangularMatrix(self, tri_matrix):
        if(tri_matrix != None):
            self.tri_matrix = tri_matrix
    
    def setMatrix(self, matrix):
        self.matrix = matrix
    
    def getMatrix(self):
        if(self.matrix == None):
            self.convertTriMatrixToMatrix()

        return self.matrix

    def convertTriMatrixToMatrix(self, inputMatrix=None):
        if(inputMatrix != None):
            self.tri_matrix = inputMatrix        

        # lista de vertices
        V = set(range(len(self.tri_matrix)))
        
        # matriz de distancias completa
        matrix = [[0 if i == j 
                else self.tri_matrix[i][j-i-1] if j > i
                else self.tri_matrix[j][i-j-1] for j in V] for i in V]
        self.matrix = matrix
        return matrix

    def __str__(self):
        m = self.getMatrix()        
        value = ""
        for i in range(len(m)):
            value += "[ "
            for j in range(len(m[i])):
                value += f"{m[i][j]}".zfill(3)
                if j != len(m[i])-1:
                    value += ", " 
            value += " ]\n"
        return value