import re


def find_hex_numbers(text):
	# Поиск шестнадцатеричных чисел с одной F в начале или в конце
	pattern = r'\b(?:0x)?[0-9a-eA-E]*F[0-9a-fA-F]*\b'
	hex_numbers = re.findall(pattern, text)
	return hex_numbers


def main():
	with open('data.txt', 'r') as file:
		text = file.read()

	print("Входные данные:")
	print(text)

	hex_numbers = find_hex_numbers(text)

	if hex_numbers:
		# Отфильтровать числа с одной F в начале или в конце
		filtered_hex_numbers = [num for num in hex_numbers if num.count('F') == 1 and (num[0] == 'F' or num[-1] == 'F')]

		if filtered_hex_numbers:
			# Найти максимальное число
			max_hex = max(int(num, 16) for num in filtered_hex_numbers)
			max_hex_str = hex(max_hex)
			print("\nМаксимальное число с одной F в начале или в конце:", str(max_hex_str).upper()[2:])

			# Определить количество чисел
			count_hex = len(filtered_hex_numbers)
			print("Количество таких чисел:", count_hex)
		else:
			print("\nШестнадцатеричные числа с одной F в начале или в конце не найдены.")
	else:
		print("\nШестнадцатеричные числа не найдены в файле.")


if __name__ == "__main__":
	main()