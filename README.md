# Covid Contamination

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo**: 03<br>
**Paradigma**: SMA<br>

## Alunos
|Matrícula | Aluno |
| ---------- | ------------------------------- |
| 19/0063441 | Ana Carolina Carvalho da Silva  |
| 18/0113151 | Eduardo Nunes Picolo            |
| 18/0113861 | Kleidson Alves Corrêa           |
| 18/0125770 | Lucas Gabriel Bezerra           |
| 18/0114077 | Lucas Rodrigues Fonseca         |
| 18/0106970 | Matheus Gabriel Alves Rodrigues |
| 18/0129058 | Paulo Victor da Silva           |
| 18/0129287 | Pedro Henrique Vieira Lima      |
| 18/0130722 | Samuel Nogueira                 |

## Sobre 
Utilizando o paradigma SMA e pensando no contexto da pandemia, o grupo decidiu construir um sistema que simula o processo de contaminação de Covid-19 em uma população. 
No início da simulação o ponto de partida é uma pessoa contaminada, após o paciente zero contrair o vírus é possível visualizar o processo de contato e contaminação entre as outras pessoas até se alastrar, podendo ocorrer reincidência da infecção e até mesmo aqueles que não contraíram mesmo com o contato. 
Resumidamente, apresentamos como se comporta um surto de contaminação como o que ocorreu com o Covid. 

## Screenshots

Tela principal da aplicação 

![Tela principal](/media/tela_principal.jpeg) 

Cada bola amarela representa um indivíduo que pode ser identificado pelo número atribuído a cada um deles.

Quadro de contaminação

![Contaminacao](/media/quadro_contaminacao.jpeg) 

Quando o indivíduo é contaminado ele recebe a cor vermelha.

Simulação

![Simulacao](/media/covid.gif) 

Como pode ser visto no gif acima, os indivíduos em vermelho são aqueles contaminados, quando ganham a cor verde é porque se recuperaram da doença, entretanto, quando ganham a cor cinza é porque o mesmo faleceu. 
No momento em que nenhum paciente possui a cor vermelha é porque a doença foi extinta. Apesar disso, aqueles que ganharam a cor cinza, ou seja, que faleceram, não são alterados e permanecem no mesmo lugar.

## Instalação
**Linguagens**: Python <br>
**Tecnologias**: Python <br>

Pré-requisito para rodar a aplicação é ter o Python instalado.

## Uso
Para executar o projeto basta instalar as dependências   

```
pip  install -r requirements.txt
````

Após instalar as dependências, basta usar o seguinte comando

```
python main.py
```

## Vídeo
O vídeo do projeto está no seguinte [link](https://youtu.be/yD-6Cup9MtU)

## Fontes
Para desenvolver o projeto o time usou algumas fontes de referência:
Para validar os dados sobre o Covid-19 e ajustar os parâmetros foram usadas duas fontes.

<b> CONTE, J. Como funciona o ciclo da covid-19 no organismo?. </b> <https://drauziovarella.uol.com.br/coronavirus/como-funciona-o-ciclo-da-covid-19-no-organismo/>. Acesso em: 11 abr. 2022.

<b>World Health Organization. Mask use in the context of COVID-19. </b> <https://www.who.int/publications/i/item/advice-on-the-use-of-masks-in-the-community-during-home-care-and-in-healthcare-settings-in-the-context-of-the-novel-coronavirus-(2019-ncov)-outbreak>. Acesso em: 11 abr. 2022.

Usamos a documentação do framework Mesa para implementá-lo no projeto. 

<b> Mesa: Agent-based modeling in Python 3+ </b> <https://mesa.readthedocs.io/en/latest/index.html>. Acesso em 13 abr.