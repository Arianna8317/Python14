import numbers
# добавила проверку на ввод не чисел в матрицу

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
        
        result = Matrix()
        sum_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_2.append (self.matrix[i][j] + other.matrix[i][j])
            result.matrix.append(sum_2) 
            sum_2 = []      
        return result

    def mult(self, b):
        
        result = Matrix()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
               result.matrix.append (self.matrix[i][j] *2)
        return result
            
    def __eq__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True         

    def __mul__(self, other):
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
    


#mat_1 = Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])
#mat_1 = Matrix(['fw', 3, 4], [3, 5, 8], [1, 0, 2])
#mat_3 = Matrix([1, 3, 4], [3, 5, -8], [1, 0, 0])  
#print(mat_3)

'''
print()
mat_2 = Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])  
print(mat_2)
print("\n Сумма матриц \n")
print(f"{mat_1 + mat_2}") 
print("\n Сравнение матриц \n")
print(mat_1 == mat_2)
print(mat_1 != mat_3)
print("\n Умножение матриц \n")
'''
#print(f"{mat_1 * mat_1}")

#print(mat_2.mult(2))