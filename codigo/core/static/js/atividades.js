function selecionarAtividade(linha, id){
	var linhas = document.querySelectorAll('.linhaAtividade');

	linhas.forEach(function(item){
		item.classList.remove('linhaSelecionada');
	});

	linha.classList.add('linhaSelecionada');
	document.getElementById('atividadeSelecionada').value = id;
}


function editarSelecionado(){
	var id = document.getElementById('atividadeSelecionada').value;

	if(id == ''){
		alert('Selecione uma ação na tabela antes de editar.');
		return;
	}
	window.location.href = '/funcionarios/atividades/editar/' + id + '/';
}


function excluirSelecionado(){
	var id = document.getElementById('atividadeSelecionada').value;

	if(id == ''){
		alert('Selecione uma ação na tabela antes de excluir.');
		return;
	}
	var confirmar = confirm('Tem certeza que deseja excluir a ação selecionada?');

	if(confirmar){
		window.location.href = '/funcionarios/atividades/excluir/' + id + '/';
	}
}

function confirmarAlteracao(){
	return confirm('Deseja salvar as alterações desta ação?');

}