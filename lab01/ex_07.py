#print(f"{a*25} \nPython : Guido van Rossum \nC++ : Bjarne Stroustrup \nJava : Jame Gosling \nPascal : Niklaus Wirth\n{a*25}")


lang1 = "Python"
lang2 = "C++"
lang3 = "Java"
lang4 = "Pascal"
author1 = "Guido van Rossum"
author2 = "Bjarne Stroustrup"
author3 = "Jame Gosling"
author4 = "Niklaus Wirth"
sep = ":"

print("#" * 25)
print(lang1 + sep + author1)
print(lang2 + sep + author2)
print(lang3 + sep + author3)
print(lang4 + sep + author4)
print("#" * 25)

# 가운데 정렬
print("#" * 25)
print(f"{lang1:>7}{sep}{author1}")
print(f"{lang2:>7}{sep}{author2}")
print(f"{lang3:>7}{sep}{author3}")
print(f"{lang4:>7}{sep}{author4}")
print("#" * 25)
