# 17. Given a sequence of integer numbers ending with the number 0. Determine the length of the widestfragment where all the elements are equal to each other.

# 5 5 5 3 3 3 3 7 7 0

num_list = [5, 5, 5, 3, 3, 3, 3, 3, 7, 7,7, 7, 7, 7, 0]
c = 1
frag_len = []

for i in range(len(num_list) - 1):
    if num_list[i] == num_list[i + 1]:
        c += 1
    else:
        frag_len.append(c)
        c = 1

frag_len.sort()
frag_len.reverse()

print(f"The Widest Segment of recurring numbers is of length : {frag_len[0]}")
