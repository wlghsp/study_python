
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a' )
f.write(user_input)
f.write("\n")
f.close()