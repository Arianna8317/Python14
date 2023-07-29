import numbers
import doctest


class TextError(Exception): 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'В матрицу можно записывать только числа!! Вы указали {self.value}'

class Matrix:
    
    def __init__(self, *args):
        self.matrix = list(args)
        for elem in self.matrix:
            for i in range(len(elem)):
                if not isinstance(elem[i], numbers.Number):
                    raise TextError(elem[i])
        
    def __str__(self):
        res = '\n'.join(map(str, self.matrix))
        res = res.replace(",", "").replace("[", "").replace("]", "")        
        return res
   
    def __add__(self, other):
        """
        >>> Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) + Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) ==  Matrix([2, -6, 10], [14, -10, -2], [6, -4, 4])
        True
        """
        result = Matrix()
        sum_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_2.append (self.matrix[i][j] + other.matrix[i][j])
            result.matrix.append(sum_2) 
            sum_2 = []      
        return result
        
    def __eq__(self, other):
        """
        >>> Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) == Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])
        True
        """
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True         

    def __mul__(self, other):

        """
        >>> Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) * Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2]) == Matrix([-5, 2, 18], [-31, 6, 38], [-5, -3, 21] ) 
        True
        """
        
        p = len(self.matrix[0])

        if p != len(other.matrix):
            ''' Матрицы разной размерности '''
            return False  # raise ValueError
        else:
            result = Matrix()
            sum_2 = [] 
            for i in range(len(self.matrix)):  # по строкам 1 матрицы
                for j in range(len(other.matrix[i])):  
                    sum = 0
                    for k in range(p):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    sum_2.append(sum)    
                result.matrix.append(sum_2)   
                sum_2 = [] 
        return result
    
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)