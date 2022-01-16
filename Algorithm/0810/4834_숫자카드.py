TC = int(input())


sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def many_number(numbers): # numbers = [4, 9, 6, 7, 9]
    result = {}

    for number in numbers:
        if number not in result:
            result[number] = 1
        else:
            result[number] += 1
    
    rev_result = {}
    keys = list(result.keys())
    values = list(result.values())
    
    for value in values:
        if value not in result:
            rev_result[(value)] = []
    for key in keys:
        rev_result[result[key]].append(key)
    
    many_num = max(rev_result.keys())
    answer1 = max(rev_result[many_num])

    answer = []
    answer.append(answer1)
    answer.append(many_num)

    return answer

result = []
for i in range(TC):
    length_of_num = int(input())
    number = list(input())
    answer = many_number(number)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {str(result[i][0])} {result[i][1]}')