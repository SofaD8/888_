#Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
# за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re


def check_pattern(text):
    pattern = r`[Rr][Bb]+[Rr]`
    return re.findall(pattern, text)


text_to_check = "rRbr R bbr RBBBBBr Rbbr"
matches = check_pattern(text_to_check)
print(matches)


