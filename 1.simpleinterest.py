def simpleinterest(principal, rate, time):
    simpleinterest = (principal * rate * time) / 100
    return simpleinterest


principalamount = float(input("Enter the principal amount: "))
interestrate = float(input("Enter the interest rate (per annum): "))
timeperiod = float(input("Enter the time period (in years): "))


result = simpleinterest(principalamount, interestrate, timeperiod)
print("Simple Interest:", result)
