print ("***********************")
print ("**JOGO DA ADIVINHAÇÃO**")
print ("***********************")

##ENT ESSE PROGRAM TEUM UM NUMERO CHAVE e o usurer tem q ir cutando os numeros de 1 a 10 e quando ele acerta
##uma mensagem aparece na tela dizendo q ele acertou
ne = 5
totalt = 3
rodada = 1

while (totalt > 0):
  print ("Tentativa {} de {}".format(rodada, totalt))
  nc = int(input("digite um numero de 1 a 100:  "))
  print ("voce digitou", nc)


  acertou = (nc == ne)
  nmaior = (nc > ne)
  nmenor = (nc < ne)

  if (acertou):
    print ("voce acertou!!!!")
  elif (nmaior):
    print ("errou seu chute foi maior que o numero secreto")
  elif (nmenor):
    print ("seu chute foi menor que o numero secreto")

  totalt = totalt -1


print ("Fim de Jogo (◉ω◉)" )
