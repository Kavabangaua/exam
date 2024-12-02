import unittest
def calculate_credit_interest(amount, annual_rate):
    if amount < 0:
        raise ValueError("Сума кредиту не може бути менше 0!")
    
    interest = amount * (annual_rate / 100)
    return interest

class TestCreditInterestCalculation(unittest.TestCase):

    def test_positive_case(self):
        self.assertAlmostEqual(calculate_credit_interest(10000, 2), 1200)
        self.assertAlmostEqual(calculate_credit_interest(5000, 5), 250)

    def test_zero_amount(self):
        self.assertAlmostEqual(calculate_credit_interest(0, 10), 0)

    def test_zero_interest_rate(self):
        self.assertAlmostEqual(calculate_credit_interest(10000, 0), 0)

    def test_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            calculate_credit_interest(-10000, 10)
        self.assertEqual(str(context.exception), "Сума кредиту не може бути менше 0!")

    def test_large_values(self):
        self.assertAlmostEqual(calculate_credit_interest(1e6, 15), 150000)

if __name__ == "__main__":
    unittest.main()