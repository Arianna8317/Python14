from matrix import Matrix, TextError
import unittest

class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.m_1 = Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])
        self.m_2 = Matrix([1, -3, 5], [7, -5, -1], [3, -2, 2])  
        self.m_3 = Matrix([-5, 2, 18], [-31, 6, 38], [-5, -3, 21] )     
        self.m_4 = Matrix([2, -6, 10], [14, -10, -2], [6, -4, 4])  

    def test_1(self):
     
        self.assertEqual(self.m_1, self.m_2)

    def test_2(self):
        self.assertEqual(self.m_1 + self.m_2, self.m_4)  

    def test_3(self):
        self.assertTrue(self.m_1 * self.m_2 == self.m_3)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

