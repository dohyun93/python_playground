# https://programmers.co.kr/learn/courses/30/lessons/17683

# 1. 멜로디가 원본음악의 끝/처음 부분
# 2. 멜로디중 일부분만 원본음악에 존재
# C#, D#, F#, G#, A# -> 하나로 바꿔줘야.
# H, I, J, K, L 로 바꿔주자.
# 정답!!!!
def change(m):
    newM = m.replace("C#", "H")
    newM = newM.replace("D#", "I")
    newM = newM.replace("F#", "J")
    newM = newM.replace("G#", "K")
    newM = newM.replace("A#", "L")
    return newM

def checkMiddle(totalMelody, m):
    return totalMelody.find(m)

def calcTime(sh, sm, eh, em):
    if sh == eh:
        return em - sm
    elif sh < eh:
        if sm <= em:
            return 60*(eh-sh) + (em-sm)
        else:
            return 60*(eh-1-sh) + (em+60-sm)

def solution(m, musicinfos):
    m = change(m)
    sp_music = [s.split(",") for s in musicinfos]
    for i in sp_music:
        i[3] = change(i[3])

    # 음악 시간만큼 전체 길이 늘리기
    # 전체 시간, 조건일치할 경우 재생 시간, 시간동안 전체 멜로디
    answer = '(None)'
    ansLen = 0
    for ele in range(len(sp_music)):
        starts, ends = sp_music[ele][0], sp_music[ele][1]
        akbo = sp_music[ele][3]

        starts_h, starts_m = starts.split(":")
        ends_h, ends_m = ends.split(":")

        totalTime = calcTime(int(starts_h), int(starts_m), int(ends_h), int(ends_m))

        if len(akbo) >= totalTime >= 0:
            totalMelody = akbo[:totalTime]
        else:
            totalMelody = akbo * (totalTime // len(akbo)) + akbo[:totalTime % len(akbo)]
        print(totalMelody)
        ck_middle = checkMiddle(totalMelody, m)
        if ck_middle != -1:
            if len(totalMelody) > ansLen:
                answer = sp_music[ele][2]
                ansLen = len(totalMelody)

    return answer

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
ans = solution(m, musicinfos)