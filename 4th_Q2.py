##### Q2. 특정 글자가 전체 글에서 몇개 들어있는지 찾는 함수
#####     변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록

a = """안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다.
안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다.
안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다.
안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다.
안녕하세요. 반갑습니다. 파이썬 공부는 정말 재밌습니다."""

def count_word(a, fword):

    text = open("d:\sample1.txt", 'w', encoding = 'utf-8')
    text.write(a)
    text.close()

    text = open("sample1.txt", 'r', encoding = 'utf-8')
    count = 0

    for line in text:
        words = line.split()

        for word in words:
            if fword in word: 
                count = count + 1

    print(fword, count)

count_word(a, "습니다")