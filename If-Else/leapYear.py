# Problem: Determine whether a given year is a leap year
# Platform: HackerRank
# Concepts: Conditional statements, modulo operator
# Approach: Apply standard leap year rules (divisible by 4, 100, 400)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    try:
        year=int(input("Enter year (format: YYYY) :"))
        print(f"Is {year} a leap year: {is_leap(year)}")
    except:
        print("Please enter a valid year")
        