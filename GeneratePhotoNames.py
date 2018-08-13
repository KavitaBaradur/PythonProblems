from collections import Counter

def solution(S):
    a = S.split("\n")

    photo_name = [i.split(', ')[0] for i in a]
    photo_city = [i.split(', ')[1] for i in a]
    photo_time = [i.split(', ')[2] for i in a]

    sorted_pics = sorted(zip(sorted(photo_time), photo_city, photo_name))
    print(sorted_pics)
    city_counter = Counter(photo_city)

    for i in range(len(sorted_pics)):
        count = city_counter[sorted_pics[i][1]]
        # for j in range(len(photo_time)):
        #     if photo_time[j] == sorted_pics[i][0]:
        #         count = j
        print(sorted_pics[i][1] + str(count) + "." + sorted_pics[i][2].split('.')[1])



S ="photo.jpg, Warsaw, 2013-09-05 14:08:15\n" \
   "john.png, London, 2015-06-20 15:13:22\n" \
   "myFriends.png, Warsaw, 2013-09-05 14:07:13\n" \
   "Eiffel.jpg, Paris, 2015-07-23 08:03:02\n" \
   "pisatower.jpg, Paris, 2015-07-22 23:59:59\n" \
   "BOB.jpg, London, 2015-08-05 00:02:03\n" \
   "notredame.png, Paris, 2015-09-01 12:00:00\n" \
   "me.jpg, Warsaw, 2013-09-06 15:40:22\n" \
   "a.png, Warsaw, 2016-02-13 13:33:50\n" \
   "b.jpg, Warsaw, 2016-01-02 15:12:22\n" \
   "c.jpg, Warsaw, 2016-01-02 14:34:30\n" \
   "d.jpg, Warsaw, 2016-01-02 15:15:01\n" \
   "e.png, Warsaw, 2016-01-02 09:49:09\n" \
   "f.png, Warsaw, 2016-01-02 10:55:32\n" \
   "g.jpg, Warsaw, 2016-02-29 22:13:11"

solution(S)