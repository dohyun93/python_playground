import re

# https://whatisthenext.tistory.com/116 -> 좋은 참고.

# 파이썬 메타문자
# . ^ $ * + ? { } \ | ( )
# . -> \n을 제외하고 모든 문자와 매칭. 단, re.DOTALL 옵션을 주면 이마저도 포함.
# ^ -> not의 의미를 갖는다. 또 re.compile과 함께 어떤 문자열로 시작하는 것들을 추릴 수 있다.(findall)
# $ -> 위 ^와 반대로 어떤 문자열로 끝나는 것들을 추릴 수 있다.
# * -> 반복 (0회 이상) ca*t
# + -> 반복 (1회 이상) ca+t
# {숫자1, 숫자2} -> 반복 (숫자 1이상 숫자 2이하 반복. 숫자 하나만 있는경우 해당 숫자만큼 반복인지 매치여부 결정)
# ? -> {0, 1}과 동일. 없거나 있거나.
# \ -> 만약 \section 이라는 문자열을 포함하는 문자열을 찾기위해서는 \\section 이라고 compile옵션을 줘야함.
# () -> 그룹핑. 추출할 패턴 지정.

p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# 위 패턴객체 'p'를 아래처럼 주석과 함께 가독성좋게 바꿔사용할 수도 있다.
p = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
