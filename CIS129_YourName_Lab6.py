# The following code is Python code saved as Lab6.py

# main module
def main():
    # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package

    # Input
    total = getTotalHotDogs()

    # Local variables
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = total // DOGS + (1 if total % DOGS != 0 else 0)
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = total // BUNS + (1 if total % BUNS != 0 else 0)

    # Output
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

# The getTotalHotDogs module
def getTotalHotDogs():
    # Get the number of people attending the cookout
    people = int(input("Enter the number of people attending the cookout: "))
    # Get the number of hot dogs each person will be given
    hotDogs = int(input("Enter the number of hot dogs for each person: "))
    # Calculate the total number of hot dogs needed
    total = people * hotDogs
    return total

# The showResults module
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    # Display the results
    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs left over:", dogsLeft)
    print("Hot dog buns left over:", bunsLeft)

# Call the main function to run the program
if __name__ == "__main__":
    main()
