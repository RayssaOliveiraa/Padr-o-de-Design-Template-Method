# Padrão de Design : Template-Method
 Aplicar o padrão Template Method para definir a quantidade de dados da defesa e do ataque.
 Foi ultilizada a logica do jogo WAR para lançantos de Dados:
 O ataque e a defesa ira jogar os dados de acordo com a quantidade de exercito, se limitando a no maximo 3 dados,
 Se o atacante e/ou defesa tiver: 
                Exercitos >= 3   - Jogara 3 Dados
                Exercitos =  2   - Jogara 2 Dados
                Exercitos =  1   - Jogara 1 Dados
                Exercitos =  0   - Jogara 0 Dados (Game over)
                
![image](https://github.com/RayssaOliveiraa/Padr-o-de-Design-Template-Method/assets/87939812/99631eed-cdcb-4096-813f-d9da374dc759)


 Exemplo: Para testes temos duas rotas URL : 
  Ataque: http://localhost:5000/batalha/agressiva/<valor>
  Onde tem Valor, substituia por um numero inteiro na qual corresponderá a quantidade  de exército.

  Defesa: http://localhost:5000/batalha/defensiva/2
  Onde tem Valor, substituia por um numero inteiro na qual corresponderá a quantidade  de exército.

  Exemplo: http://localhost:5000/batalha/agressiva/4
  ![image](https://github.com/RayssaOliveiraa/Padr-o-de-Design-Template-Method/assets/87939812/e7813f14-8eb4-4cc9-a865-403e1aafd223)

                
 
