**Cenário:** Checar se o conteúdo e o formato da mensagem está correto para um produto  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester" participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** "Produto X" entra em promoção de "R$ 10,00" por "R$ 5,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** a mensagem de produtos em promoção é enviada para "Produto X"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** a mensagem deve ter o formato:   
> "Olá Tester, os seguintes produtos que você costuma consumir estão em promoção! Vem conferir: - Produto X: R$ 10,00 por R$ 5,00"  

**Cenário:** Checar se o conteúdo e o formato da mensagem está correto para vários produtos  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester" participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** "Produto X" entra em promoção de "R$ 10,00" por "R$ 5,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** "Produto Y" entra em promoção de "R$ 20,00" por "R$ 15,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** "Produto Z" entra em promoção de "R$ 30,00" por "R$ 25,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras destes produtos ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** aa mensagem de produtos em promoção é enviada para "Produto X, Produto Y e Produto Z"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** a mensagem deve ter o formato:   
> "Olá Tester, os seguintes produtos que você costuma consumir estão em promoção! Vem conferir: - Produto X: R$ 10,00 por R$ 5,00, - Produto Y: R$ 20,00 por R$ 15,00, - Produto Z: R$ 30,00 por R$ 25,00"  

**Cenário:** Checar se clientes não participantes do clube de clientes recebem mensagens promocionais  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester2" *não* participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** "Produto X" entra em promoção de "R$ 2,00" por "R$ 1,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** nenhuma mensagem é enviada para "Produto X"  

**Cenário:** Checar produtos de consumo contínuo no período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester" participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** "Produto X" entra em promoção de "R$ 200,00" por "R$ 100,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram "entre 6 e 90 dias atrás"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** a mensagem sobre a promoção é enviada para "Produto X"  

**Cenário:** Checar produtos de consumo contínuo fora do período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester" participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** "Produto X" entra em promoção de "R$ 200,00" por "R$ 100,00"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** todas as compras deste produto ocorreram {periodo}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** nenhuma mensagem é enviada para "Produto X"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Exemplos**  
| periodo |    
| ------- |  
| 5 ou menos dias atrás |  
| 91 ou mais dias atrás |  
| hoje |  
| amanhã |  

**Cenário:** Checar produtos mostrados na mensagem de acordo com frequencia de consumo  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dado que** o cliente "Tester" participa do clube de clientes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quando** {produto1} entra em promoção de {valor_orig1} por {valor_promo1}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** foi comprado {qtde1} vezes dentro do período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** {produto2} entra em promoção de {valor_orig2} por {valor_promo2}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** foi comprado {qtde2} vezes dentro do período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** {produto3} entra em promoção de {valor_orig3} por {valor_promo3}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** foi comprado {qtde1} vezes dentro do período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** {produto4} entra em promoção de {valor_orig4} por {valor_promo4}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**E** foi comprado {qtde4} vezes dentro do período definido  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Então** a mensagem de produtos em promoção é enviada para {list_prod}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Exemplos**  
produto1 	| valor_orig1 | valor_promo1 | qtde1 	| produto2 	| valor_orig2 | valor_promo2 | qtde2 	| produto3 	| valor_orig3 | valor_promo3 | qtde3 	| produto4 	| valor_orig4 | valor_promo4 | qtde4 	| list_prod 	 	   
----------- | ----------- | ------------ | --------	| --------	| ----------- | ------------ | -------- | --------- | ----------- | ------------ | -------- | --------- | ----------- | ------------ | -------- | ----  
Produto X 	| R$ 10,00 	 | R$ 5,00 	   |10 		|Produto Y 	|R$ 20,00 	 |R$ 15,00 	   |30 		|Produto Z 	|R$ 30,00 	 |R$ 25,00 	   |20 		|Produto W 	|R$ 11,00 	 |R$ 6,00 	   |9 		|Produto Y, Z e X  
Produto X 	| R$ 10,00 	 | R$ 5,00 	   |10 		|Produto Y 	|R$ 20,00 	 |R$ 15,00 	   |30 		|Produto Z 	|R$ 30,00 	 |R$ 25,00 	   |20 		|Produto W 	|R$ 11,00 	 |R$ 6,00 	   |10 		|Produto Y, Z e X  
Produto X 	| R$ 10,00 	 | R$ 5,00 	   |10 		|Produto Y 	|R$ 20,00 	 |R$ 15,00 	   |30 		|Produto Z 	|R$ 30,00 	 |R$ 25,00 	   |20 		|Produto W 	|R$ 11,00 	 |R$ 6,00 	   |11 		|Produto Y, Z e W  
Produto X 	| R$ 10,00 	 | R$ 5,00 	   |10 		|Produto Y 	|R$ 20,00 	 |R$ 15,00 	   |10 		|Produto Z 	|R$ 30,00 	 |R$ 25,00 	   |10 		|Produto W 	|R$ 11,00 	 |R$ 6,00 	   |10 		|Produto W, X e Y  s