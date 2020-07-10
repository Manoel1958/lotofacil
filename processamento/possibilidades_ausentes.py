from pandas import read_csv


URL = './base/resultados.csv'
DEZENAS = [i for i in range(1, 26)]


def criar_nao_sorteados(dz=DEZENAS, base=URL, atualizar_base_resultados=False):
	"""
	Cria uma lista com todos as dezenas não sorteadas em cada concurso.

	:param dz: Lista com as dezenas da lotofácil (default: {DEZENAS})
	:param base: CSV com todos os resultados da lotofácil (default: {URL})
	:param atualizar_resultado: True atualiza a base, do contrário, não.
	(default: {False})
	
	return: Lista com as dezenas não sorteadas de cada concurso.	
	"""

	if atualizar_base_resultados:
		# Atualiza o arquivo com todos os resultados dos sorteios já realizados
		from dados import scrapping_resultados

	dados = read_csv(base, sep=';', encoding='utf-8')
	resultados = dados.iloc[:, 2:17].values

	nao_sorteados = list()

	for resultado in resultados:
		resultado.sort()
		diferenca = set(dz).difference(resultado)
		nao_sorteados.append(list(diferenca))

	return nao_sorteados