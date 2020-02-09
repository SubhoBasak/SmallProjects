def comp_time(t1, t2):
    if t1 == t2:
        return 0
    else:
        t1 = t1.split(':')
        t2 = t2.split(':')

        h1 = int(t1[0])
        h2 = int(t2[0])

        m1 = int(t1[1])
        m2 = int(t2[1])

        if h1 > h2:
            return -1
        elif h1 < h2:
            return 1
        elif m1 > m2:
            return -1
        elif m1 < m2:
            return 1

def sum_time(times):
    hh = 0
    mm = 0
    for i in times:
        t1 = i[0].split(':')
        t2 = i[1].split(':')

        h1 = int(t1[0])
        h2 = int(t2[0])

        m1 = int(t1[1])
        m2 = int(t2[1])

        while True:
            if h1 == h2 and m1 == m2:
                break
            m1 += 1
            mm += 1
            if m1 == 60:
                h1 += 1
                m1 = 0
            if mm == 60:
                hh += 1
                mm = 0

    return str(hh)+':'+str(mm)

def get_free_time(time):
    result = []

    prv_time = time[0][0];
    for i in time[1:]:
        x = comp_time(prv_time, i[0])
        if x < 0:
            return 0
        elif x > 0:
            result.append([prv_time, i[0]])
        if len(i) == 2:
            prv_time = i[1]

    return result

def get_same_free_time(time1, time2):
    if len(time1) < 2 or len(time2) < 2:
        return 0

    result = []

    time1 = get_free_time(time1)
    time2 = get_free_time(time2)

    print('Free time of user1 :', time1)
    print('\nFree time of user2 :', time2)

    count = 0
    for i in time1:
        for j in time2[count:]:
            x = comp_time(i[0], j[0])
            y = comp_time(i[1], j[1])

            tmp_start = None
            tmp_end = None
            
            if x < 0:
                tmp_start = i[0]
            elif x > 0:
                tmp_start = j[0]
            else:
                tmp_start = i[0]

            if tmp_start == None:
                continue

            if y < 0:
                tmp_end = j[1]
            elif y > 0:
                tmp_end = i[1]
            else:
                tmp_end = i[1]

            if comp_time(tmp_start, tmp_end) > 0:
                result.append([tmp_start, tmp_end])
                count += 1
                break

    return result

if __name__ == '__main__':
    target = '00:30'
    user1 = [['8:00'], ['8:00', '9:15'], ['10:00', '10:23'], ['10:23', '10:49'], ['11:00']]
    user2 = [['9:15'], ['9:30', '10:11'], ['11:00', '11:22'], ['11:30']]

    meeting_times = get_same_free_time(user1, user2)

    if len(meeting_times) == 0:
        print('They have no same free time')
    else:
        total_time = sum_time(meeting_times)
        
        print('\nThey both can meet at :', meeting_times)

        x = comp_time(target, total_time)
        if x < 0:
            print('\nThe target time is not reached. They can meat for only', total_time)
        elif x > 0:
            print('\nThey can meat for the target time and they will also get some more time. Total they will get :', total_time)
        else:
            print('\nThey can meat for the target time :', total_time)
