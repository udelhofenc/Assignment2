"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR



def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER

def cost_of_skipped_classes(annual_cost, credits, skipped_classes):
    return cost_per_class(annual_cost, credits) * skipped_classes


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: "))
    credits = int(input("Enter the number of credits taken this semester: "))

    while True:
        print()
        print("\nThe Cost of College Menu")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class meeting")
        print("6. Cost of skipped classes")
        print("Q. Quit")

        choice = input("Choose an option: ")


        if choice == "Q" or choice == "q":
            print("Thank you for using the Cost of College calculator!")
            break

        elif choice == "1":
            print(f"${cost_per_semester(annual_cost):,.2f}")

        elif choice == "2":
            print(f"${cost_per_month(annual_cost):,.2f}")

        elif choice == "3":
            print(f"${cost_per_day(annual_cost):,.2f}")

        elif choice == "4":
            print(f"${cost_per_credit(annual_cost, credits):,.2f}")

        elif choice == "5":
            print(f"${cost_per_class(annual_cost, credits):,.2f}")

        elif choice == "6":
            skipped_classes = int(input("Enter the number of classes skipped: "))
            print(f"${cost_of_skipped_classes(annual_cost, credits, skipped_classes):,.2f}")

        else:
            print("Invalid choice")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()


