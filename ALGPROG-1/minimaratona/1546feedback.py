N = int(input())

for i in range(N):
    K = int(input())
    for j in range(K):
        feedback = input()
        if feedback == "1":
            print("Rolien")
        elif feedback == "2":
            print("Naej")
        elif feedback == "3":
            print("Elehcim")
        elif feedback == "4":
            print("Odranoel")
            
#Desafio: Modifique para que a estrutura de saída seja:
'''
2
4
1 1 3 4
3
3 3 2
'''