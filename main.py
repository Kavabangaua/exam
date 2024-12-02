def calculate_credit_interest(amount, annual_rate):
    if amount < 0:
        raise ValueError("Сума кредиту не може бути менше 0!")
    interest = amount * (annual_rate / 100)
    return interest

try:
    amount = float(input("Введіть суму кредиту: "))
    annual_rate = float(input("Введіть річну процентну ставку (%): "))
    interest = calculate_credit_interest(amount, annual_rate)
    print(f"Відсотки за кредитом для суми {amount} грн за ставкою {annual_rate}%: {interest:.2f} грн")
except ValueError as e:
    print(f"Помилка: {e}")