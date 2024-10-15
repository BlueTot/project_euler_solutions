from math import log10, floor

def first_three_digits_of(n):
    d = 1 + floor(n *log10(2))
    return floor(10** (n * log10(2) - d + 3))

# lst = []
# for n in range(100000):
#     if str(first_three_digits_of(n)) == "123":
#         lst.append(n)
#         # print(n)
#     if n % 10000 == 0:
#         print(n)
# print(lst)
# print(len(lst))
# print([lst[i+1]-lst[i] for i in range(1, len(lst)-1)])

# print(lst.index(12710))

lst = [90]
for _ in range(678910-1):
    print(_)
    for jump in [196, 289, 485]:
        next_num = lst[-1] + jump
        if str(first_three_digits_of(next_num)) == "123":
            lst.append(next_num)
            break
print(lst[678910-1])

'''
[90, 379, 575, 864, 1060, 1545, 1741, 2030, 2226, 2515, 2711, 3000, 3196, 3681, 3877, 4166, 4362, 4651, 4847, 5136, 5332, 5817, 6013, 6302, 6498, 6787, 6983, 7272, 7468, 7953, 8438, 8634, 8923, 9119, 9408, 9604, 10089, 10574, 10770, 11059, 11255, 11544, 11740, 12225, 12710, 12906, 13195, 13391, 13680, 13876, 14361, 14846, 15042, 15331, 15527, 15816, 16012, 16301, 16497, 16982, 17178, 17467, 17663, 17952, 18148, 18437, 18633, 19118, 19314, 19603, 19799, 20088, 20284, 20573, 20769, 21254, 21450, 21739, 21935, 22224, 22420, 22709, 22905, 23390, 23875, 24071, 24360, 24556, 24845, 25041, 25526, 26011, 26207, 26496, 26692, 26981, 27177, 27662, 28147, 28343, 28632, 28828, 29117, 29313, 29602, 29798, 30283, 30479, 30768, 30964, 31253, 31449, 31738, 31934, 32419, 32615, 32904, 33100, 33389, 33585, 33874, 34070, 34555, 34751, 35040, 35236, 35525, 35721, 36010, 36206, 36691, 37176, 37372, 37661, 37857, 38146, 38342, 38827, 39312, 39508, 39797, 39993, 40282, 40478, 40963, 41448, 41644, 41933, 42129, 42418, 42614, 43099, 43584, 43780, 44069, 44265, 44554, 44750, 45039, 45235, 45720, 45916, 46205, 46401, 46690, 46886, 47175, 47371, 47856, 48052, 48341, 48537, 48826, 49022, 49311, 49507, 49992, 50477, 50673, 50962, 51158, 51447, 51643, 52128, 52613, 52809, 53098, 53294, 53583, 53779, 54264, 54749, 54945, 55234, 55430, 55719, 55915, 56400, 56885, 57081, 57370, 57566, 57855, 58051, 58340, 58536, 59021, 59217, 59506, 59702, 59991, 60187, 60476, 60672, 61157, 61353, 61642, 61838, 62127, 62323, 62612, 62808, 63293, 63489, 63778, 63974, 64263, 64459, 64748, 64944, 65429, 65914, 66110, 66399, 66595, 66884, 67080, 67565, 68050, 68246, 68535, 68731, 69020, 69216, 69701, 70186, 70382, 70671, 70867, 71156, 71352, 71641, 71837, 72322, 72518, 72807, 73003, 73292, 73488, 73777, 73973, 74458, 74654, 74943, 75139, 75428, 75624, 75913, 76109, 76594, 76790, 77079, 77275, 77564, 77760, 78049, 78245, 78730, 79215, 79411, 79700, 79896, 80185, 80381, 80866, 81351, 81547, 81836, 82032, 82321, 82517, 83002, 83487, 83683, 83972, 84168, 84457, 84653, 85138, 85623, 85819, 86108, 86304, 86593, 86789, 87078, 87274, 87759, 87955, 88244, 88440, 88729, 88925, 89214, 89410, 89895, 90091, 90380, 90576, 90865, 91061, 91350, 91546, 92031, 92227, 92516, 92712, 93001, 93197, 93486, 93682, 94167, 94652, 94848, 95137, 95333, 95622, 95818, 96303, 96788, 96984, 97273, 97469, 97758, 97954, 98439, 98924, 99120, 99409, 99605, 99894]'''