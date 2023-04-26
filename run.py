import unidecode 

limpo = ''

with open('nomes.txt', "r") as arquivo:
    conteudo = arquivo.read()
    linhas = conteudo.split("\n")
    for i in linhas:
        temp = i.split(" 0044.")[0].upper() + "\n"
        temp = unidecode.unidecode(temp)
        limpo += temp

with open('nomes.txt', "w") as arquivo:
    arquivo.write(limpo)

limpo = ''

# -- 

with open('efetivo.txt', "r") as arquivo:
    conteudo = arquivo.read()
    linhas = conteudo.split("\n")
    for i in linhas:
        temp = i.split(" ")
        # print(temp)
        string_nova = ''
        for j, k in enumerate(temp):
            if j > 2:
                string_nova += k + ' '
                
        limpo += string_nova.split(" 6º")[0].upper() + "\n"

with open('efetivo-limpo.txt', "w") as arquivo:
    arquivo.write(limpo)

# --
arquivo_um = ''
arquivo_dois = ''
with open('efetivo-limpo.txt', "r") as arquivo:
    arquivo_um = arquivo.read()

with open('nomes.txt', "r") as arquivo:
    arquivo_dois = arquivo.read()

diferentes = []

arquivo_um = arquivo_um.split("\n")
for i in arquivo_um:
    if not i in arquivo_dois:
        diferentes.append(i)

print(diferentes)
print(len(diferentes))