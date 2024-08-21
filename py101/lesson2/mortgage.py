# input are:
# - loan amount
# - annual percentage rate
# - loan duration in years

# interest is compounded monthly
# determine:
# - monthly interest rate
# - loan duration in months

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True
    return False

# constraints on inputs: APR has to be a positive float
# loan amount has to be a positive float
# loan_duration_year has to be a positive float

prompt('Please input the amount that you would like to borrow (in USD)')
loan_amount = input()
while invalid_number(loan_amount):
    prompt('Your input is invalid')
    loan_amount = input()

prompt('Please input your APR in % (e.g., 23 for 23%)')
apr = input()
while invalid_number(apr):
    prompt('Your input is invalid')
    apr = input()

prompt('''Please input your loan duration in years
        (e.g., 2.5 for 2 years and a half)''')
loan_duration_yrs = input()
while invalid_number(loan_duration_yrs):
    prompt('Your input is invalid')
    loan_duration_yrs = input()

monthly_rate = float(apr) / (12 * 100)
loan_duration_months = float(loan_duration_yrs) * 12
monthly_payment = float(loan_amount) * (
    monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration_months))
)

prompt(f'''Your monthly payment is ${monthly_payment:.2f} over
    {loan_duration_months} months.''')