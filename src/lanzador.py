import os

# Ejercicio 2
# for i in range(2, 11, 2):
# 	os.system("python main.py ../data/and.txt 1 0.1 " + str(i) + " 01/and_" + str(i) + ".txt")
# 	os.system("python main.py ../data/xor.txt 1 0.1 " + str(i) + " 01/xor_" + str(i) + ".txt")

# 	os.system("python main.py ../data/and.txt 1 0.01 " + str(i) + " 001/and_" + str(i) + ".txt")
# 	os.system("python main.py ../data/xor.txt 1 0.01 " + str(i) + " 001/xor_" + str(i) + ".txt")

# 	os.system("python main.py ../data/and.txt 1 0.001 " + str(i) + " 0001/and_" + str(i) + ".txt")
# 	os.system("python main.py ../data/xor.txt 1 0.001 " + str(i) + " 0001/xor_" + str(i) + ".txt")

# for i in range(10, 51, 10):
# 	os.system("python main.py ../data/problema_real2.txt 0.6 0.1 " + str(i) + " 01/problema_real2_" + str(i) + ".txt")

# 	os.system("python main.py ../data/problema_real2.txt 0.6 0.01 " + str(i) + " 001/problema_real2_" + str(i) + ".txt")

# Ejercicio 3
# for i in range(10, 51, 10):
# 	os.system("python main.py ../data/problema-real-3clases.txt 0.6 0.1 " + str(i) + " 01/problema-real-3clases-" + str(i) + ".txt")

# 	os.system("python main.py ../data/problema-real-3clases.txt 0.6 0.01 " + str(i) + " 001/problema-real-3clases-" + str(i) + ".txt")

# Ejercicio 4
for i in range(10, 51, 10):
	os.system("python main.py ../data/problema-real4.txt 0.6 0.1 " + str(i) + " 01/problema-real-norm-4-" + str(i) + ".txt")

	os.system("python main.py ../data/problema-real4.txt 0.6 0.01 " + str(i) + " 001/problema-real-norm-4-" + str(i) + ".txt")