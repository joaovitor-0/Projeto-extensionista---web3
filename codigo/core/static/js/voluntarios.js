function selecionarVoluntario(linha, id){
	var linhas = document.querySelectorAll('.linhaVoluntario');

	linhas.forEach(function(item){
		item.classList.remove('linhaSelecionada');
	});

	linha.classList.add('linhaSelecionada');

	document.getElementById('voluntarioSelecionado').value = id;
}

function editarVoluntarioSelecionado(){
	var id = document.getElementById('voluntarioSelecionado').value;

	if(id == ''){
		alert('Selecione um vínculo na tabela antes de editar.');
		return;
	}

	window.location.href = '/funcionarios/voluntarios/editar/' + id + '/';

}

function excluirVoluntarioSelecionado(){
	var id = document.getElementById('voluntarioSelecionado').value;

	if(id == ''){
		alert('Selecione um vínculo na tabela antes de remover.');
		return;
	}

	var confirmar = confirm('Tem certeza que deseja remover este vínculo?');

	if(confirmar){
		window.location.href = '/funcionarios/voluntarios/excluir/' + id + '/';
	}

}

function confirmarAlteracaoVoluntario(){
	return confirm('Deseja salvar as alterações deste vínculo?');

}