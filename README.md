# qa-teste-pratico

## Respostas

1. Assumindo que:
    1. Há registros tanto das compras feitas por um cliente em lojas físicas quanto na plataforma de comércio eletrônico
    2. Não há distinção entre os registros de produtos comprados em lojas físicas e na plataforma e-commerce
      > Caso contrário (i e ii) apenas produtos de compras online ou físicas poderiam ser usados para as sugestões, por exemplo, sendo necessária a criação de casos de teste para cada um desses cenário 
    3. Produtos de consumo contínuo são aqueles listados em mais compras de um cliente nos últimos 3 meses
      > (iii) Apenas para delimitar o que é um “produto de consumo contínuo” para que, além de garantir que produtos relevantes sejam mostrados, os testes possam ser mais específicos e assertivos
    4. “Produtos relevantes”: São os produtos de uso contínuo mais frequentes em compras recentes (entre 6 e 90 dias atrás). Caso haja mais de um produto de consumo contínuo com a mesma frequência de compra no período, a prioridade é a ordem alfabética
      > É preciso saber essa informação para saber qual é o resultado esperado quando há mais de um produto de consumo contínuo disputando um lugar na lista

    Os cenários possíveis são os descritos em: [Cenários](https://github.com/vgdcarvalho/qa-teste-pratico/blob/main/scenarios.md)  

2. Alguns dos testes unitários para	ajudar o Alex são os descritos aqui: [Testes Unitários](https://github.com/vgdcarvalho/qa-teste-pratico/blob/main/TestPromoMessage.py)	 

3. Para recuperar os 5 produtos de maior incidência basta executar a query abaixo:  
```sql
SELECT id, nome, count(id_produto) AS compras
FROM produto
JOIN produto_compra
	ON id = id_produto
GROUP BY id
ORDER BY compras DESC
LIMIT 5;
```
  
4. Sobre a "Definição de Pronto" algumas coisas poderiam ser adicionadas, outras alteradas e algumas ações em conjunto com o time de desenvolvimento poderiam ser incentivadas:  

**Adicionar:**  
- A funcionalidade/correção passou por testes unitários  
- A funcionalidade/correção passou por revisão de código  
> Pois podem ajudar a encontrar defeitos no código de forma mais rápida, evitando que se propaguem ao longo do processo, diminuindo custos com manutenção e possível diminuição de falhas identificadas durante as atividades de teste posteriores.

**Alterar:**
- A funcionalidade/correção foi testada no ambiente de QA  
> Mudaria para: "A funcionalidade/correção foi testada no ambiente de QA e atende aos critérios de aceitação"
> Pois não basta testar, é preciso garantir que os critérios de aceitação tenham sido atendidos durante as atividades de teste também  

**Ações:**
- Além disso, um dos possíveis motivos para que funcionalidades tenham sido implementadas de forma incompleta é uma pontuação equivocada durante a planning. Talvez os itens escolhidos para a sprint tenham sido mal interpretados e a sprint acabou sendo mais "pesada" para o time do que deveria. Talvez seja necessário que os QAs participem de forma mais ativa na planning, para dar seu ponto de vista com relação às atividades de teste sobre os itens da sprint. É preciso ter consciência que todas as atividades ao longo do processo podem impactar a definição de pronto, não somente a programação.  

- Outra coisa que poderia ajudar a rastrear os erros apontados durante os testes é a garantir que um processo de identificação apropriado destes erros esteja sendo realizado, como algum tipo identificação de projeto/versão/sprint/componente por erro apontado, bem como um registro detalhado e disponível a todos do time. Em conjunto, os próprios QAs poderiam fazer um pré-direcionamento das possíveis causas destes erros, para que desenvolvedores tenham um norte ao tentar encontrar o defeito no código em si. 