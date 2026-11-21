###
# Prints test statistics
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Calculates the total number of test questions
total_question_number = len(test_results)

# Calculates the number of correct answers
correct_answers = 0

for answer in test_results:
    if answer:
        correct_answers += 1

# Calculates the number of incorrect answers
incorrect_answers = total_question_number - correct_answers

# Calculates the percentage of correct answers
percentage = correct_answers / total_question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', total_question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage:.2f}%')