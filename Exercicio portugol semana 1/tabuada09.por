programa {
  funcao inicio() {
    inteiro numero

    escreva("Digite um numero para ver sua tabuada at� 100: ")
    leia(numero)

    para(inteiro i = 1; i <= 100; i++)
    {
      escreva(numero, "x", i, "=", numero * i, "\n")
    }


  }
}
