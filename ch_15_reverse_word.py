input_word = str(input("Enter a word: "))

input_list = list(input_word)

output_list = []

for _ in range(0, len(input_list)):
    output_list.append(input_list[-1])
    input_list.pop()

output_word = "".join(output_list)
print(f"Here is the output: {output_word}")