import re


def find_hex_nums(text):
	# Поиск шестнадцатеричных чисел с одной F в начале или в конце
	reg = r'\b(?:0x)?[0-9a-eA-E]*F[0-9a-fA-F]*\b'
	hex_num = re.findall(reg, text)
	return hex_num


def main():
	with open('data.txt', 'r') as file:
		text = file.read()

	print("Входные данные:")
	print(text)

	hex_numbers = find_hex_nums(text)

	if hex_numbers:
		# Отфильтровать числа с одной F в начале или в конце
		filtered = [num for num in hex_numbers if num.count('F') == 1 and (num[0] == 'F' or num[-1] == 'F')]

		if filtered:
			# Найти максимальное число
			max_hex = max(int(num, 16) for num in filtered)
			max_hex_str = hex(max_hex)
			print("\nМаксимальное число с одной F в начале или в конце:", str(max_hex_str).upper()[2:])

			# Определить количество чисел
			count_hex = len(filtered)
			print("Количество таких чисел:", count_hex)
		else:
			print("\nШестнадцатеричные числа с одной F в начале или в конце не найдены.")
	else:
		print("\nШестнадцатеричные числа не найдены в файле.")


if __name__ == "__main__":
	main()
