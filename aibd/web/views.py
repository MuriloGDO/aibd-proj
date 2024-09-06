from django.shortcuts import render
import web.database_es

def home(request):
    #TODO: Pegar todos os dados de cada Unidade no Banco de dados
    ###Por enquanto vamos so simular um banco de dados
    units = web.database_es.get_units()
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
    lat = -23.222450523442227
    lon = -45.88591053224127
    unit = web.database_es.get_unit(unit_id)
    unit["numero_de_alunos"] = web.database_es.count_students(unit_id)
    unit["distancia_do_aluno"] = web.database_es.get_distance(unit_id, lat, lon)
    unit["professores"] = web.database_es.list_teachers(unit_id)
    unit["voluntarios"] = web.database_es.list_voluntarios(unit_id)
    unit["financiadores"] = web.database_es.list_financiadores(unit_id)
    unit["media_investimento"] = web.database_es.media_investimento(unit_id)

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
    return render(request, 'unit_detail.html', {'unit': unit})
    ###

def subscribe_student_to_unit(request, unit_id):
    if request.method == "POST":
        name = request.POST.get("nome_completo")
        cpf = request.POST.get("cpf")
        date = request.POST.get("data_nascimento")
        renda = request.POST.get("renda")
        parent = request.POST.get("nome_responsavel")
        fone = request.POST.get("telefone_responsavel")

        aluno_json = {
            "nome": name,
            "cpf": cpf,
            "renda": renda,
            "data_de_nascimento": date,
            "instituicao": {"id": unit_id},
        }
        responsavel_json = {
            "nome": parent,
            "telefone": fone
        }
        web.database_es.insert_student(aluno_json, responsavel_json)

def subscribe_to_the_unit(request, unit_id):
    unit = web.database_es.get_unit(unit_id)
    if  request.method == "POST":
        subscribe_student_to_unit(request, unit_id)
        return render(request, 'subscribe_to_the_unit.html', {'unit': unit, "success": True})
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
    return render(request, 'subscribe_to_the_unit.html', {'unit': unit})
    ###