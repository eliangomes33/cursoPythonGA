with open("arquivo.txt","w") as arquivo:
	arquivo.write("Eligol gameplay")
arquivo.close()

with open("arquivo.txt","a") as arquivo:
        arquivo.writelines("\n Eligol gameplay")
arquivo.close()

with open("arquivo.txt", "r") as arquivo:
        arquivo.read()
arquivo.close()


