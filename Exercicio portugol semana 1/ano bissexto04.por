programa {
  funcao inicio() {
    inteiro ano
    escreva("Digite um ano para saber se ele � bissexto ou n�o bissexto:")
    leia(ano)
    
    se((ano % 4 == 0) e (ano % 100 == 0) ou (ano % 400 == 0))
    {
      escreva("O ano � bissexto")
    }senao{
      escreva("O ano n�o � bissexto")
    }

  
  }
}
