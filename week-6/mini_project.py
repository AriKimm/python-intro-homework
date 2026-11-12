numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_max(numbers):
    largest=numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)-1):
        for j in range(len(sorted_numbers)-1-i):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]

    return sorted_numbers


def show_menu():
    print('\nNumber Cruncher Menu')
    print('1. Find minimum')
    print('2. Find maximum')
    print('3. Search for a number')
    print('4. Sort numbers')
    print('5. Exit')

    choice = input('Enter your choice: ')

    return choice


def main():
    while True:
        choice = show_menu()

        if choice == '1':
            result = find_min(numbers)
            print('Minimum:', result)

        elif choice == '2':
            result = find_max(numbers)
            print('Maximum:', result)

        elif choice == '3':
            target = int(input('Enter a number to seach for: '))
            result = search(numbers, target)

            if result != -1:
                print(f'Found at index {result}')
            else:
                print('Not found')

        elif choice == '4':
            result = bubble_sort(numbers)
            print('Sorted numbers:', result)

        else:
            print('Invalid choice. Please try again.')

main()