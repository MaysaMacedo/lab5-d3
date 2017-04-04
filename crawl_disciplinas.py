# -*- coding: utf-8 -*-

import subprocess, time

cursos = ["administracao_d_cg", "administracao_n_ss", "administracao_n_cg", "agronomia_d_pl", \
    "arquitetura_e_urbanismo_d_cg", "arte_e_midia_d_cg", "ciencia_da_computacao_d_cg", "ciencias_biologicas_lic_d_ct", \
    "ciencias_biologicas_lic_d_pt", "ciencias_biologicas_lic_m_cz", "ciencias_biologicas_lic_n_ct", \
    "ciencias_biologicas_lic_n_pt", "ciencias_contabeis_n_ss", "ciencias_economicas_m_cg", "ciencias_economicas_n_cg", \
    "ciencias_sociais_lic_d_cg", "ciencias_sociais_lic_n_sm", "comunicacao_social_d_cg", "comunicacao_social_n_cg", \
    "curso_sup_de_tecn_em_agroecologia_d_sm", "curso_sup_de_tecn_em_gestao_publica_n_sm", "design_d_cg", \
    "educacao_do_campo_lic_d_sm", "enfermagem_d_ct", "enfermagem_d_cz", "enfermagem_d_cg", \
    "eng_de_biotecnologia_e_bioprocessos_d_sm", "engenharia_agricola_d_cg", "engenharia_ambiental_d_pl", \
    "engenharia_civil_d_cg", "engenharia_de_alimentos_d_pl", "engenharia_de_biossistemas_d_sm", \
    "engenharia_de_materiais_d_cg", "engenharia_de_minas_d_cg", "engenharia_de_petroleo_d_cg", \
    "engenharia_de_producao_d_sm", "engenharia_de_producao_d_cg", "engenharia_eletrica_cg", "engenharia_florestal_d_pt", \
    "engenharia_mecanica_d_cg", "engenharia_quimica_d_cg", "estatistica_d_cg", "farmacia_d_ct", "filosofia_bac_n_cg", \
    "filosofia_lic_n_cg", "fisica_lic_d_cg", "fisica_lic_d_ct", "fisica_lic_n_cz", "fisica_lic_n_ct", \
    "geografia_lic_d_cg", "geografia_lic_n_cg", "geografia_licenciatura_m_cz", "geografia_licenciatura_n_cz", \
    "historia_lic_d_cg", "historia_lic_d_parfor_cg", "historia_lic_m_cz", "historia_lic_n_cz", "historia_lic_n_cg", \
    "letras_espanhol_licenciatura_n_cg", "letras_ling_port_ling_franc_lic_d_cg", "letras_lingua_inglesa_lic_d_cz", \
    "letras_lingua_inglesa_lic_d_cg", "letras_lingua_portuguesa_lic_m_cz", "letras_lingua_portuguesa_lic_n_cz", \
    "letras_lingua_portuguesa_lic_n_cg", "letras_lingua_portuguesa_lic_d_cg", "matematica_bac_d_cg", \
    "matematica_lic_d_ct", "matematica_lic_d_cz", "matematica_lic_d_cg", "matematica_lic_d_parfor_cg", \
    "matematica_lic_n_ct", "matematica_lic_n_cg", "medicina_d_cg", "medicina_d_cz", "medicina_veterinaria_d_pt", \
    "meteorologia_d_cg", "musica_bac_d_cg", "musica_lic_d_cg", "nutricao_d_ct", "nutricao_n_ct", "odontologia_d_pt", \
    "pedagogia_lic_m_cg", "pedagogia_lic_n_cg", "pedagogia_licenciatura_m_cz", "pedagogia_licenciatura_n_cz", \
    "psicologia_n_cg", "quimica_lic_d_ct", "quimica_lic_n_ct", "quimica_lic_n_cz", "quimica_lic_n_parfor_cg", \
    "servico_social_m_ss"]


p = subprocess.Popen(["mkdir", "dados_disciplinas"], stdout=subprocess.PIPE)

for curso in cursos:
    p = subprocess.Popen(["curl", "http://analytics.lsd.ufcg.edu.br/pre/" + curso + "/disciplinas"], stdout=subprocess.PIPE)
    out, err = p.communicate()

    with open("dados_disciplinas/" + curso + ".json", "w+") as file:
        file.write(out)

    time.sleep(10)

