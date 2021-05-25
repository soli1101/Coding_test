def solution(numbers, hand):
    answer = ""
    one = (0,1)
    two = (0,2)
    three = (0,3)
    four = (1,1)
    five = (1,2)
    six = (1,3)
    seven=(2,1)
    eight=(2,2)
    nine=(2,3)
    star=(3,1)
    zero=(3,2)
    sharp=(3,3)

    left_loc = star
    right_loc = sharp

    id_to_word = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, "*":star, "#":sharp, 0:zero}
    # it would have been greater if I set sets in keys right away
    for i in numbers:
        if i in [1,4,7]:
            answer+="L"
            left_loc = id_to_word[i]
        if i in [3,6,9]:
            answer+="R"
            right_loc= id_to_word[i]
        if i in [2,5,8,0]:
            number = id_to_word[i]
            left_distance = abs(left_loc[0] - number[0])+abs(left_loc[1]-number[1])
            right_distance = abs(right_loc[0]-number[0])+abs(right_loc[1]-number[1])
            # 1: 거리가 같은 경우
            if left_distance == right_distance and hand == 'left':
                answer+="L"
                left_loc = number
            elif left_distance == right_distance and hand == "right":
                answer+="R"
                right_loc = number
            # 2: 거리가 다른 경우
            if left_distance < right_distance:
                answer+="L"
                left_loc = number
            elif left_distance > right_distance: 
                answer+="R"
                right_loc = number

    return answer
