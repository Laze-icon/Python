#Eugen Mboya
#BSCIT-05-0003/2024

# Prompt the user to enter names
names_input = input("Enter a list of names (separated by commas): ")

# Convert input string to a list and remove extra spaces
names_list = [name.strip() for name in names_input.split(",")]

# Count total number of names entered
total_names = len(names_list)

# Remove duplicates and sort alphabetically
unique_sorted_names = sorted(set(names_list))

# Display results
print("\nTotal number of names entered:", total_names)
print("Final sorted list without duplicates:")
for name in unique_sorted_names:
    print(name)
