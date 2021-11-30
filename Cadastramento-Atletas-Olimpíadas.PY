MENU =0
idade_media = 0
quantidade_atletas = 0
sintomaticos = 0
assintomaticos = 0
idade_sintomaticos = 0
idade_assintomaticos = 0
maior_temperatura = 0
maior_idade = 0
menor_idade = 100
contador_kit_masc = 0
contador_kit_femi = 0
kit_sintomas_masc = 0
kit_sintomas_femi = 0
kit_sem_sinto_masc = 0
kit_sem_sinto_femi = 0
ouro_masc_sem_sinto = 0
prata_masc_sem_sinto = 0
bronze_masc_sem_sinto = 0
ouro_masc_com_sinto = 0
prata_masc_com_sinto = 0
bronze_masc_com_sinto = 0
ouro_femi_sem_sinto = 0
prata_femi_sem_sinto = 0
bronze_femi_sem_sinto = 0
ouro_femi_com_sinto = 0
prata_femi_com_sinto = 0
bronze_femi_com_sinto = 0
homem_com_sinto_medalha =0
homem_sem_sinto_medalha =0
mulher_com_sinto_medalha =0
mulher_sem_sinto_medalha =0

while MENU!= 3:
#====================MENU DE ENTRADA ===============================
 print('='*30)
 print('''        MENU
 1- Cadastrar-se
 2- Relatório
 3- Sair
 4- Relatório Geral''')
 MENU = int(input('Escolha um numero: '))
 print('='*30)

# ========================CADASTRAMENTO=============================
 if MENU == 1:
     idade = int(input('Digite sua idade: '))
     sexo = input('Qual seu sexo?(M/F) ').upper()
     febre = input('Teve febre?(S/N) ').upper()
     if febre == 'S':
        temperatura = float(input('Qual a temperatura mais alta atingiada desde que voltou de Tóquio? '))
        sintomas = 'Nao apresentados'
     elif febre == 'N':
         sintomas = input('Apresentou outro sintoma?(S/N) ').upper()
         temperatura = 36.5
     kit_covid = input('Usou o Kit Covid ao retornar ao Brasil?(S/N) ').upper()
     medalhas = input('Ganhou medalhas?(S/N) ').upper()
     if medalhas == 'S':
         ouro = int(input('Quantas de ouro? '))
         prata = int(input('Quantas de prata? '))
         bronze = int(input('Quantas de bronze? '))
         total_medalhas = ouro+prata+bronze
     elif medalhas == 'N':
         ouro = 0
         prata = 0
         bronze = 0
         total_medalhas = 0 
    #====================== DADOS PARA RELATÓRIO GERAL ================

    #HOMES SEM SINTOMAS QUE GANHARAM MEDALHAS
     if sexo == 'M' and sintomas == 'N' and medalhas == 'S':
         homem_sem_sinto_medalha += 1
         ouro_masc_sem_sinto += ouro
         prata_masc_sem_sinto += prata
         bronze_masc_sem_sinto += bronze

    #HOMENS COM SINTOMAS QUE GANHARM MEDALHAS
     if sexo == 'M' and medalhas == 'S' and sintomas == 'S':
         homem_sem_sinto_medalha += 1
         ouro_masc_com_sinto += ouro
         prata_masc_com_sinto += prata
         bronze_masc_com_sinto += bronze

    #MULHERES SEM SINTOMAS QUE GANHARAM MEDALHAS
     if sexo == 'F' and sintomas == 'N' and medalhas == 'S':
         mulher_sem_sinto_medalha += 1
         ouro_femi_sem_sinto += ouro
         prata_femi_sem_sinto += prata
         bronze_femi_sem_sinto += bronze

    #MULHERES COM SINTOMAS QUE GANHARAM MEDALHAS
     if sexo == 'F' and sintomas == 'S' and medalhas == 'S':
         mulher_com_sinto_medalha += 1
         ouro_femi_com_sinto += ouro
         prata_femi_com_sinto += prata
         bronze_femi_com_sinto += bronze

    # HOMENS QUE TOMARAM KIT COVID
     if sexo == 'M' and kit_covid == 'S':
         contador_kit_masc += 1

    #MULHERES QUE TOMARAM O KIT COVID
     if sexo == 'F' and kit_covid == 'S':
         contador_kit_femi += 1
        
    # HOMENS QUE USARAM KIT COVID E TIVERAM SINTOMAS
     if febre == 'S' and sintomas == 'S' and kit_covid == 'S':
         kit_sintomas_masc += 1

    #HOMENS QUE USARAM KIT COVID E NÃO TIVERAM SINTOMAS
     if febre =='N' and sintomas == 'N' and kit_covid == 'S':
          kit_sem_sinto_masc +=1
        
    #MULHERES QUE USARAM KIT COVID E TIVERAM SINTOMAS
     if febre == 'S' and sintomas == 'S' and kit_covid =='S':
         kit_sintomas_femi += 1

    #MULHERES QUE USARAM KIT COVID E NÃO TIVERAM SINTOMAS
     if febre == 'N' and sintomas == 'N' and kit_covid=='S':
         kit_sem_sinto_femi += 1


     #TEMPERATURA MAIS ALTA

     if temperatura > maior_temperatura:
       maior_temperatura = temperatura

    #QUANTIDADE DE ATLETAS MONITORADOS

     quantidade_atletas += 1

    #IDADE MEDIA DOS ATLETAS

     idade_media +=idade

     #QUANTIDADE QUE APRESENTOU SINTOMAS E IDADE DOS COM SINTOMAS E SEM SINTOMAS

     if febre == 'S' or sintomas == 'S':
         sintomaticos += 1
         idade_sintomaticos += idade
         #MAIS VELHO E MAIS NOVO QUE TEVE SINTOMAS
         if idade > maior_idade:
             maior_idade = idade
         if idade < menor_idade:
             menor_idade = idade
     elif febre =='N' or sintomas =='N':
         assintomaticos +=1
         idade_assintomaticos +=idade 
    
 #===================== RELATÓRIO INDIVIDUAL =======================

 if MENU == 2:
     print('='*30)
     print('idade:', idade)
     print('sexo:',sexo)
     print('Teve febre? ',febre)
     print('Maior teperatura atingida: ', temperatura)
     print('Outros sintomas: ', sintomas)
     print('Tomou kit covid? ', kit_covid)
     print('Ganhou medalhas? ', medalhas)
     print(ouro, ' medalhas de ouro, ', prata, ' medalhas de prata e ', bronze, ' medalhas de bronze.' )
     print('Total de medalhas: ', total_medalhas)
     print('='*30)
#======================= SAIR DO PROGRAMA ===========================
 elif MENU == 3:
     print('='*30)
     print('Fim do sistema!!!')
     print('='*30)
 #======================= RELATÓRIO GERAL DOS ATLETAS ===============
 elif MENU == 4:
     print('='*60)
     print('Idade media dos atletas: %.1f' %(idade_media/quantidade_atletas))
     print('Quantidade de atletas: ', quantidade_atletas)
     print('Quantidade que tiveram sintomas: ', sintomaticos)
     print('Idade media dos assintomaticos: %.1f ' %(idade_assintomaticos/ assintomaticos))
     print('Idade media dos sintomaticos: %.1f' %(idade_sintomaticos/ sintomaticos))
     print('Maior temperatura:', maior_temperatura)
     print('Maior idade dos sintomaticos:', maior_idade)
     print('Menor idade dos sintomaticos: ', menor_idade)
     print('Homens que usaram kit covid: ', contador_kit_masc)
     print('Muleheres que usaram kit covid: ', contador_kit_femi)
     print('Homens que usaram kit covid e não tiveram sintomas: ', kit_sem_sinto_masc)
     print('Homens que usaram kit covid e tiveram sintomas: ', kit_sintomas_masc)
     print('Mulheres que usaram kit covid e não tiveram sintomas: ', kit_sem_sinto_femi)
     print('Mulheres que usaram kit covid e tiveram sintomas: ', kit_sintomas_femi)
     print('Homens sem sintomas que ganharam medalhas: ', homem_sem_sinto_medalha)
     print('Homens com sintomas que ganharam medalhas: ', homem_com_sinto_medalha)
     print('Mulheres sem sintomas que ganharam medalhas: ', mulher_sem_sinto_medalha)
     print('Mulheres com sintomas que ganharam medalhas: ', mulher_com_sinto_medalha)
     print('Medalhas de ouro ganhas por homens com sintomas:', ouro_masc_com_sinto)     
     print('Medalhas de prata ganhas por homens com sintomas:', prata_masc_com_sinto) 
     print('Medalhas de bronze ganhas por homens com sintomas:', bronze_masc_com_sinto) 
     print('Medalhas de ouro ganhas por homens sem sintomas:', ouro_masc_sem_sinto) 
     print('Medalhas de prata ganhas por homens sem sintomas:', prata_masc_sem_sinto) 
     print('Medalhas de bronze ganhas por homens sem sintomas:', bronze_masc_sem_sinto) 
     print('Medalhas de ouro ganhas por mulheres com sintomas:', ouro_femi_com_sinto) 
     print('Medalhas de prata ganhas por mulheres com sintomas:', prata_femi_com_sinto)
     print('Medalhas de bronze ganhas por mulheres com sintomas:', bronze_femi_com_sinto)
     print('Medalhas de ouro ganhas por mulheres sem sintomas:', ouro_femi_sem_sinto)
     print('Medalhas de prata ganhas por mulheres sem sintomas:', prata_femi_sem_sinto)
     print('Medalhas de bronze ganhas por mulheres sem sintomas:', bronze_femi_sem_sinto)
     print('='*60)