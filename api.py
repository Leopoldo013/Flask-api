from flask import Flask, jsonify, render_template
from flask_jwt import JWT, jwt_required
from conection import connect
from securite import authenticate, identity

app = Flask(__name__)

app.secret_key = 'aPi-proDesp@$&3535'

jwt = JWT(app, authenticate, identity)

COURSE_NAME = """select  dados.person_id, dados.duration_sum, dados.interaction_cnt,
                dados.first_accessed_time, curso.id, curso.course_number, curso.name,
                pessoa.first_name, pessoa.last_name, pessoa.email, pessoa.birth_date
                from BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.course_activity as dados
                inner join BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.course as curso
                on dados.course_id = curso.id
                inner join BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.person as pessoa
                on pessoa.id = dados.person_id
                where curso.course_number like '%00016%'
                or curso.course_number like '%0009%'
                and curso.name not like '%Projeto Integrador%' 
                order by pessoa.id, first_accessed_time"""

COURSE_NAME_1 = """select  dados.person_id, dados.duration_sum, dados.interaction_cnt,
                dados.first_accessed_time, dados.last_accessed_time, curso.id, curso.course_number, curso.name,
                pessoa.first_name, pessoa.last_name, pessoa.email, pessoa.birth_date
                from BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.course_activity as dados
                inner join BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.course as curso
                on dados.course_id = curso.id
                inner join BLACKBOARD_DATA_2D3D65372DD04D7291A3E70BEF3A2F5C.CDM_LMS.person as pessoa
                on pessoa.id = dados.person_id
                where curso.course_number like '%00016%' 
                    and curso.name not like '%Projeto Integrador%' 
                order by pessoa.id, first_accessed_time desc"""


@app.route('/doc')
def index():
    return render_template('index.html')


@app.route('/api/total', methods=['GET'])
@jwt_required()
def dadosApi():
    dados = connect(COURSE_NAME_1)
    print(dados)
    lista_de_alunos = []
    for item in dados:
        # print(conteudo)
        # if item[conteudo] "= None:
        content = {}

        content = {'PERSON_ID': item[0], 'DURATION_SUM': int(item[1] / 60), 'INTERACTION_CNT': item[2],
                   'FIRST_ACCESSED_TIME': str(item[3].strftime('%d-%m-%Y')),
                   'TIME': str(item[3].strftime('%H:%M')),
                   'LAST_ACCESSED_TIME': str(item[4].strftime('%d-%m-%Y')),
                   'TIME_LAST': str(item[4].strftime('%H:%M')),
                   'ID_COURSE': str(item[5]),
                   'COURSE_NUMBER': item[6],
                   'NAME_COURSE': item[7], 'FIRST_NAME': item[8],
                   'LAST_NAME': item[9], 'EMAIL': item[10], 'BIRTH_DATE': str(item[11])}

        id_content = content.get('COURSE_NUMBER')

        if not lista_de_alunos or course_lista != id_content:
            lista_de_alunos.append(content)
        course_lista = lista_de_alunos[len(lista_de_alunos) - 1]['COURSE_NUMBER']

        content = {}

    return jsonify({'dados': lista_de_alunos}), 200 if dados else 400


@app.route('/api/<string:curso>', methods=['GET'])
@jwt_required()
def curso(curso):
    dados = connect(COURSE_NAME)
    lista_de_alunos = []

    for item in dados:
        # print(conteudo)
        if item[5] == curso:
            content = {}
            content = {'PERSON_ID': item[0], 'DURATION_SUM': item[1], 'INTERACTION_CNT': item[2],
                       'FIRST_ACCESSED_TIME': str(item[3].strftime('%d-%m-%Y')),
                       'TIME': str(item[3].strftime('%H:%M')),
                       'ID_COURSE': str(item[4]),
                       'COURSE_NUMBER': item[5],
                       'NAME_COURSE': item[6], 'FIRST_NAME': item[7],
                       'LAST_NAME': item[8], 'EMAIL': item[9], 'BIRTH_DATE': str(item[10])}
            id_content = content.get('PERSON_ID')

            if not lista_de_alunos or id_lista != id_content:
                lista_de_alunos.append(content)

            id_lista = lista_de_alunos[len(lista_de_alunos) - 1]['PERSON_ID']

            content = {}
    return jsonify({'dados': lista_de_alunos}), 200 if dados else 400


@app.route('/api/<string:curso>/<string:aluno>', methods=['GET'])
@jwt_required()
def aluno(curso, aluno):
    dados = connect(COURSE_NAME)
    lista_de_alunos = []

    for item in dados:
        if item[5] == curso and item[0] == int(aluno):
            content = {}
            content = {'PERSON_ID': item[0], 'DURATION_SUM': item[1], 'INTERACTION_CNT': item[2],
                       'FIRST_ACCESSED_TIME': str(item[3].strftime('%d-%m-%Y')),
                       'TIME': str(item[3].strftime('%H:%M')),
                       'ID_COURSE': str(item[4]),
                       'COURSE_NUMBER': item[5],
                       'NAME_COURSE': item[6], 'FIRST_NAME': item[7],
                       'LAST_NAME': item[8], 'EMAIL': item[9], 'BIRTH_DATE': str(item[10])}
            id_content = content.get('PERSON_ID')

            if not lista_de_alunos or id_lista != id_content:
                lista_de_alunos.append(content)

            id_lista = lista_de_alunos[len(lista_de_alunos) - 1]['PERSON_ID']

            content = {}
    return jsonify({'dados': lista_de_alunos}), 200 if dados else 400


#
@app.route('/api/v1/<string:curso_bt>', methods=['GET'])
@jwt_required()
def curso_bt(curso_bt):
    dados = connect(COURSE_NAME_1)
    lista_de_alunos = []

    for item in dados:
        # print(conteudo)
        if item[6] == curso_bt:
            content = {}
            content = {'PERSON_ID': item[0], 'DURATION_SUM': int(item[1] / 60), 'INTERACTION_CNT': item[2],
                       'LAST_ACCESSED_TIME': str(item[4].strftime('%d-%m-%Y')),
                       'TIME_LAST': str(item[4].strftime('%H:%M')),
                       'ID_COURSE': str(item[5]),
                       'COURSE_NUMBER': item[6],
                       'NAME_COURSE': item[7], 'FIRST_NAME': item[8],
                       'LAST_NAME': item[9], 'EMAIL': item[10], 'BIRTH_DATE': str(item[11])}
            id_content = content.get('PERSON_ID')

            if not lista_de_alunos or id_lista != id_content:
                lista_de_alunos.append(content)

            id_lista = lista_de_alunos[len(lista_de_alunos) - 1]['PERSON_ID']

            content = {}
    return jsonify({'dados': lista_de_alunos}), 200 if dados else 400


@app.route('/api/v1/<string:curso_bt>/<string:aluno_bt>', methods=['GET'])
@jwt_required()
def aluno_bt(curso_bt, aluno_bt):
    dados = connect(COURSE_NAME_1)
    lista_de_alunos = []

    for item in dados:
        if item[6] == curso_bt and item[0] == int(aluno_bt):
            content = {}
            content = {'PERSON_ID': item[0], 'DURATION_SUM': int(item[1] / 60), 'INTERACTION_CNT': item[2],
                       'LAST_ACCESSED_TIME': str(item[4].strftime('%d-%m-%Y')),
                       'TIME_LAST': str(item[4].strftime('%H:%M')),
                       'ID_COURSE': str(item[5]),
                       'COURSE_NUMBER': item[6],
                       'NAME_COURSE': item[7], 'FIRST_NAME': item[8],   
                       'LAST_NAME': item[9], 'EMAIL': item[10], 'BIRTH_DATE': str(item[11])}
            id_content = content.get('PERSON_ID')

            if not lista_de_alunos or id_lista != id_content:
                lista_de_alunos.append(content)

            id_lista = lista_de_alunos[len(lista_de_alunos) - 1]['PERSON_ID']

            content = {}
    return jsonify({'dados': lista_de_alunos}), 200 if dados else 400


if __name__ == '__main__':
    #    app.run()
    app.run(host='0.0.0.0', port=6666)
