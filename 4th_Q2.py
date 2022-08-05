##### Q2. 특정 글자가 전체 글에서 몇개 들어있는지 찾는 함수
#####     변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록

def count_word(fname, fword):

    text = open(fname, 'r', encoding = 'utf-8')
    count = 0

    for line in text:
        words = line.split()

        for word in words:
            if fword in word: 
                count = count + 1

    print(fword, count)

fname = "sample.txt"       # fname = input("파일명 입력 : ")
fword = "파이썬"           # fword = input("단어   입력 : ")
count_word(fname, fword)
