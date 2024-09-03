from django.shortcuts import render
import web.database_es

def home(request):
    #TODO: Pegar todos os dados de cada Unidade no Banco de dados
    ###Por enquanto vamos so simular um banco de dados
    units = web.database_es.get_units()
    print (units)
    # unit_alfa = {'Name': 'Unidade Alfa', 'Description': 'Descrição da unidade Alfa', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '1'}
    # unit_beta = {'Name': 'Unidade Beta', 'Description': 'Descrição da unidade Beta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '2'}
    # unit_gama = {'Name': 'Unidade Gama', 'Description': 'Descrição da unidade Gama', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '3'}
    # unit_epsilon = {'Name': 'Unidade Épsilon', 'Description': 'Descrição da unidade Épsilon', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '4'}
    # unit_delta = {'Name': 'Unidade Delta', 'Description': 'Descrição da unidade Delta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '5'}
    # unit_zeta = {'Name': 'Unidade Zeta', 'Description': 'Descrição da unidade Zeta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'Id': '6'}
    # units = []
    # units.append(unit_alfa)
    # units.append(unit_beta)
    # units.append(unit_gama)
    # units.append(unit_epsilon)
    # units.append(unit_delta)
    # units.append(unit_zeta)
    ###
    return render(request, 'web_home.html', {'units': units})

def unit_detail(request, unit_id):
    units = web.database_es.get_units()
    # #TODO: Recuperar os dados do cursinho pelo Id
    # ###Por enquanto vamos so simular um banco de dados
    # unit_alfa = {'Name': 'Unidade Alfa', 'Description': 'Descrição da unidade Alfa', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 3, 'Id': '1'}
    # unit_beta = {'Name': 'Unidade Beta', 'Description': 'Descrição da unidade Beta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 5, 'Id': '2'}
    # unit_gama = {'Name': 'Unidade Gama', 'Description': 'Descrição da unidade Gama', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 6, 'Id': '3'}
    # unit_epsilon = {'Name': 'Unidade Épsilon', 'Description': 'Descrição da unidade Épsilon', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 2, 'Id': '4'}
    # unit_delta = {'Name': 'Unidade Delta', 'Description': 'Descrição da unidade Delta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 1, 'Id': '5'}
    # unit_zeta = {'Name': 'Unidade Zeta', 'Description': 'Descrição da unidade Zeta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 0, 'Id': '6'}
    # units = []
    # units.append(unit_alfa)
    # units.append(unit_beta)
    # units.append(unit_gama)
    # units.append(unit_epsilon)
    # units.append(unit_delta)
    # units.append(unit_zeta)
    ###
    ###Por enquanto simulando uma busca no banco de dados
    for unit in units:
        if unit['id'] == str(unit_id):
            return render(request, 'unit_detail.html', {'unit': unit})
    ###

def subscribe_to_the_unit(request, unit_id):
    #TODO: Recuperar os dados do cursinho pelo Id
    ###Por enquanto vamos so simular um banco de dados
    unit_alfa = {'Name': 'Unidade Alfa', 'Description': 'Descrição da unidade Alfa', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 3, 'Id': '1'}
    unit_beta = {'Name': 'Unidade Beta', 'Description': 'Descrição da unidade Beta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 5, 'Id': '2'}
    unit_gama = {'Name': 'Unidade Gama', 'Description': 'Descrição da unidade Gama', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 6, 'Id': '3'}
    unit_epsilon = {'Name': 'Unidade Épsilon', 'Description': 'Descrição da unidade Épsilon', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 2, 'Id': '4'}
    unit_delta = {'Name': 'Unidade Delta', 'Description': 'Descrição da unidade Delta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 1, 'Id': '5'}
    unit_zeta = {'Name': 'Unidade Zeta', 'Description': 'Descrição da unidade Zeta', 'Fone': '(XX) XXXXX-XXXX', 'Address': 'Rua Exemplo, 123 - Cidade, Estado', 'NumberOfVailableVacancy': 0, 'Id': '6'}
    units = []
    units.append(unit_alfa)
    units.append(unit_beta)
    units.append(unit_gama)
    units.append(unit_epsilon)
    units.append(unit_delta)
    units.append(unit_zeta)
    ###
    ###Por enquanto simulando uma busca no banco de dados
    for unit in units:
        if unit['id'] == str(unit_id):
            return render(request, 'subscribe_to_the_unit.html', {'unit': unit})
    ###