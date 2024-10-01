class Venda:
  def __init__(self, produto, quantidade, valor):
    self.produto = produto
    self.quantidade = quantidade
    self.valor = valor

class Relatorio:
  def __init__(self):
    self.vendas = []

  def adicionar_venda(self, venda):
   if isinstance(venda, Venda):
    self.vendas.append(venda)
   else:
    raise ValueError("O Objeto deve ser uma instancia da classe venda")
    # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
    # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
     

  def calcular_total_vendas(self):
    total = 0
    for venda in self.vendas:
      total += venda.quantidade * venda.valor
    return total
      # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
       
       # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
       
    


def main():
  relatorio = Relatorio()
   
  for i in range(3):
    produto = input()
    quantidade = int(input())
    valor = float(input())
    venda = Venda(produto, quantidade, valor)
    relatorio.adicionar_venda(venda)
     
  total = relatorio.calcular_total_vendas()
  print(f"Total de Vendas: {total: .1f}")
   
  # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
  # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
   


if __name__ == "__main__":
  main()