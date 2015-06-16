construcao de dados
	le xml (!)
		monta arvore (!)
	identifica as tags que se deseja (Uriel)
		monta objeto de dados com a arvore
		adiciona objeto a fila que sera consumida pela thread de adicao ao banco

criacao do esquema do banco de dados
	tabela de Dados Gerais(Nome, localNasc, morreu, permissaoDeDivulg)
	tabela de numeros(nArtigosPublicados, nOrientacoes, nTrabalhosEmEventos)

thread de mensageria
	popula fila com objetos
	consome de acordo com a label do objeto adicionado

persistencia
	abre conexao com o banco (!)
	inicia thread para salvar dados no banco
		comeca a consumir da lista
		salva dados

#Como mostrar os dados?
opcao de pesquisa de dados?
interface?
	
