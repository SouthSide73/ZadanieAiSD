import re
def find_hex_nums(text):
	# Поиск шестнадцатеричных чисел с F в любом месте и кол-ве
	reg = r'\b(?:F[0-9a-eA-E]*\b|[0-9a-eA-E]*F)\b'
	hex_num = re.findall(reg, text)
	return hex_num
def main():
	count_hex = 0
	with open('data.txt', 'r') as file:
		text = file.read()
	print("Входные данные:")
	print(text)
	hex_numbers = find_hex_nums(text)
	if hex_numbers:
		# Найти максимальное число
		max_hex = max(int(num, 16) for num in hex_numbers)
		max_hex_str = hex(max_hex)
		print("\nМаксимальное число с одной F в начале или в конце:", str(max_hex_str).upper()[2:])
		# Определить количество чисел максимальных
		count = len(hex_numbers)
		for i in range(count):
			if str(hex_numbers[i]) == str(max_hex_str).upper()[2:]:
				count_hex += 1
		print("Количество таких чисел (максимальных):", count_hex)
	else:
		print("\nШестнадцатеричных чисел, подходящих к условию, не найдено.")
if __name__ == "__main__":
	main()
