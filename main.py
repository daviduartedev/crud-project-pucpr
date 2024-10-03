nome_estudante = input("Olá! Qual o seu nome? ")

print(f"Bem vindo, {nome_estudante}. Para prosseguir, escolha uma das opções:")
print("1 - estudante ")
print("2 - disciplina ")
print("3 - professor ")
print("4 - turma ")
print("5 - matrícula ")

valor = input("Digite o valor referente à opção desejada: ");
if (valor == "1") :
    print(f"Você escolheu a opção: estudante...");
    print(f"Sair");
elif (valor == "2") : 
    print(f"Você escolheu a opção: disciplina...");
    print(f"Sair");
elif (valor == "3") :
    print(f"Você escolheu a opção: professor...");
    print(f"Sair");
elif (valor == "4") :
    print(f"Você escolheu a opção: turma...");
    print(f"Sair");
elif (valor == "5") :
    print(f"Você escolheu a opção: matrícula...");
    print(f"Sair");
else :
    print("Opção inválida, por favor, tente novamente.");

print("Certo, para prosseguir, escolha uma das opções que deseja:")

print("1 - incluir ")
print("2 - listar ")
print("3 - excluir ")
print("4 - alterar ")

opcao = input("Digite o valor referente à opção desejada: ");

if (opcao == "1") :
    print(f"Tudo bem {nome_estudante}, o que você quer incluir?");
    print(f"Voltar");
    print(f"Sair");
elif (opcao == "2") : 
    print(f"Tudo bem {nome_estudante}, o que você quer listar?");
    print(f"Voltar");
    print(f"Sair");
elif (opcao == "3") :
    print(f"Tudo bem {nome_estudante}, o que você quer excluir?");
    print(f"Voltar");
    print(f"Sair");
elif (opcao == "4") :
    print(f"Tudo bem {nome_estudante}, o que você quer excluir?");
    print(f"Voltar");
    print(f"Sair");
else :
    print("Opção inválida, por favor, tente novamente.");



