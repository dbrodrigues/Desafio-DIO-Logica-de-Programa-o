print("**Classificador de nível de Herói**")
nomeHeroi = input("Qual é o nome do seu herói? ")
itensComuns = int(input("Quantos itens comuns você conseguiu? (0/40) "))
xpItensComuns = itensComuns * 30
itensRaros = int(input("Quantos itens raros você conseguiu? (0/20) "))
xpItensRaros = itensRaros * 120
itensEpicos = int(input("Quantos itens épicos você conseguiu? (0/10) "))
xpItensEpicos = itensEpicos * 320
xpTotalItens = xpItensComuns + xpItensRaros + xpItensEpicos

xpPorMissao = 32  # XP padrão por missão
xpPorMissaoCincoEstrelas = 64  # XP por missão com 5 estrelas
numMissoes = 100

while True:
    MissoesPergunta = int(input("Você cumpriu todas as missões do jogo? ([1] para sim ou [2] para não) "))

    if MissoesPergunta == 1:
        MissoesCincoS = int(input("Dessas missões, em quantas você conseguiu 5 estrelas? "))
        xpMissoes = numMissoes * xpPorMissao  # Considerando todas as missões padrão
        xpMissoes += MissoesCincoS * xpPorMissaoCincoEstrelas  # Adicionando XP extra para missões de 5 estrelas
        break
        
    elif MissoesPergunta == 2: 
        QuantMissoesConcluidas = int(input("Quantas Missoes você conclui? "))
        xpMissoes = QuantMissoesConcluidas * xpPorMissao  # Considerando todas as missões padrão
        break
    else:
        break

totalXp = xpTotalItens + xpMissoes

if totalXp < 1000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é FERRO")
elif totalXp > 1001 and totalXp < 2000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é BRONZE")
elif totalXp > 2001 and totalXp < 5000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é PRATA")
elif totalXp > 5001 and totalXp < 7000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é OURO")
elif totalXp > 7001 and totalXp < 8000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é PLATINA")
elif totalXp > 8001 and totalXp < 9000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é ASCENDENTE")
elif totalXp > 9001 and totalXp < 10000:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é IMORTAL ")
elif totalXp >= 10001:
    print("O herói " + nomeHeroi + " tem um total de " + str(totalXp))
    print("Seu nível atual é RADIANTE")