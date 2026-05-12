# ==========================================
# Project Name : NumPy Analyzer
# Developed By : Jayesh Dhingra
# Description  : NumPy Analyzer Project using
#                Python and NumPy Library
# ==========================================

# Import NumPy Library
import numpy as np


# ==========================================
# NumPy Analyzer Class
# ==========================================
class NumPyAnalyzer:

    # Constructor
    def __init__(self):

        # Empty NumPy array
        self.array = np.array([])

    # ==========================================
    # Create Array Function
    # ==========================================
    def create_array(self):

        print("\nChoose Array Type")
        print("1. 1D Array")
        print("2. 2D Array")

        choice = int(input("Enter your choice: "))

        # Create 1D Array
        if choice == 1:

            elements = list(map(int, input(
                "Enter elements separated by space: ").split()))

            self.array = np.array(elements)

            print("\n1D Array Created Successfully!")
            print(self.array)

        # Create 2D Array
        elif choice == 2:

            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            data = []

            print("\nEnter matrix elements row-wise:")

            for i in range(rows):

                row = list(map(int, input().split()))
                data.append(row)

            self.array = np.array(data)

            print("\n2D Array Created Successfully!")
            print(self.array)

        else:
            print("Invalid Choice!")

    # ==========================================
    # Display Array Function
    # ==========================================
    def display_array(self):

        print("\nCurrent Array:")
        print(self.array)

    # ==========================================
    # Insert Element Function
    # ==========================================
    def insert_element(self):

        value = int(input("Enter value to insert: "))
        position = int(input("Enter position: "))

        # Insert value at given index
        self.array = np.insert(self.array, position, value)

        print("\nUpdated Array:")
        print(self.array)

    # ==========================================
    # Delete Element Function
    # ==========================================
    def delete_element(self):

        position = int(input("Enter position to delete: "))

        # Delete element from array
        self.array = np.delete(self.array, position)

        print("\nUpdated Array:")
        print(self.array)

    # ==========================================
    # Search Element Function
    # ==========================================
    def search_element(self):

        value = int(input("Enter value to search: "))

        # Search element index
        result = np.where(self.array == value)

        if len(result[0]) > 0:
            print(f"\nElement found at index: {result[0]}")
        else:
            print("\nElement not found!")

    # ==========================================
    # Sort Array Function
    # ==========================================
    def sort_array(self):

        sorted_array = np.sort(self.array)

        print("\nSorted Array:")
        print(sorted_array)

    # ==========================================
    # Filter Array Function
    # ==========================================
    def filter_array(self):

        value = int(input("Show elements greater than: "))

        # Filter condition
        filtered = self.array[self.array > value]

        print("\nFiltered Array:")
        print(filtered)

    # ==========================================
    # Mathematical Operations Function
    # ==========================================
    def mathematical_operations(self):

        print("\nChoose Mathematical Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        second_array = np.array(
            list(map(int, input(
                "Enter second array elements separated by space: ").split()))
        )

        # Addition
        if choice == 1:

            result = self.array + second_array

            print("\nAddition Result:")
            print(result)

        # Subtraction
        elif choice == 2:

            result = self.array - second_array

            print("\nSubtraction Result:")
            print(result)

        # Multiplication
        elif choice == 3:

            result = self.array * second_array

            print("\nMultiplication Result:")
            print(result)

        # Division
        elif choice == 4:

            result = self.array / second_array

            print("\nDivision Result:")
            print(result)

        else:
            print("Invalid Choice!")

    # ==========================================
    # Combine Arrays Function
    # ==========================================
    def combine_arrays(self):

        second_array = np.array(
            list(map(int, input(
                "Enter second array elements separated by space: ").split()))
        )

        # Combine arrays
        combined = np.concatenate((self.array, second_array))

        print("\nCombined Array:")
        print(combined)

    # ==========================================
    # Reshape Array Function
    # ==========================================
    def reshape_array(self):

        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        try:

            reshaped = self.array.reshape(rows, cols)

            print("\nReshaped Array:")
            print(reshaped)

        except:
            print("\nReshape not possible!")

    # ==========================================
    # Aggregation Functions
    # ==========================================
    def aggregation_functions(self):

        print("\nAggregation Results")

        print("Sum:", np.sum(self.array))
        print("Mean:", np.mean(self.array))
        print("Maximum:", np.max(self.array))
        print("Minimum:", np.min(self.array))

    # ==========================================
    # Statistical Functions
    # ==========================================
    def statistical_functions(self):

        print("\nStatistical Analysis")

        print("Variance:", np.var(self.array))
        print("Standard Deviation:", np.std(self.array))
        print("Median:", np.median(self.array))
        print("50th Percentile:", np.percentile(self.array, 50))

    # ==========================================
    # Main Menu Function
    # ==========================================
    def menu(self):

        while True:

            print("\n========== NumPy Analyzer ==========")
            print("1. Create Array")
            print("2. Display Array")
            print("3. Insert Element")
            print("4. Delete Element")
            print("5. Search Element")
            print("6. Sort Array")
            print("7. Filter Array")
            print("8. Mathematical Operations")
            print("9. Combine Arrays")
            print("10. Reshape Array")
            print("11. Aggregation Functions")
            print("12. Statistical Functions")
            print("13. Exit")

            choice = int(input("\nEnter your choice: "))

            # Menu Conditions
            if choice == 1:
                self.create_array()

            elif choice == 2:
                self.display_array()

            elif choice == 3:
                self.insert_element()

            elif choice == 4:
                self.delete_element()

            elif choice == 5:
                self.search_element()

            elif choice == 6:
                self.sort_array()

            elif choice == 7:
                self.filter_array()

            elif choice == 8:
                self.mathematical_operations()

            elif choice == 9:
                self.combine_arrays()

            elif choice == 10:
                self.reshape_array()

            elif choice == 11:
                self.aggregation_functions()

            elif choice == 12:
                self.statistical_functions()

            elif choice == 13:

                print("\nThank You For Using NumPy Analyzer!")
                break

            else:
                print("\nInvalid Choice! Please Try Again.")


# ==========================================
# Main Program
# ==========================================

# Object Creation
analyzer = NumPyAnalyzer()

# Calling Menu Function
analyzer.menu()