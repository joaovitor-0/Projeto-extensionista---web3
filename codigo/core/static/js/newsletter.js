function selecionarNewsletter(linha, id){

	var linhas = document.getElementsByClassName('linhaNewsletter');

	for(var i = 0; i < linhas.length; i++){
		linhas[i].classList.remove('linhaSelecionada');
	}

	linha.classList.add('linhaSelecionada');

	document.getElementById('newsletterSelecionado').value = id;

}

function editarNewsletterSelecionado(){

	var id = document.getElementById('newsletterSelecionado').value;

	if(id == ''){
		alert('Selecione um cadastro da newsletter para editar.');
		return;
	}

	window.location.href = '/funcionarios/newsletter/editar/' + id + '/';

}

function excluirNewsletterSelecionado(){

	var id = document.getElementById('newsletterSelecionado').value;

	if(id == ''){
		alert('Selecione um cadastro da newsletter para excluir.');
		return;
	}

	if(confirm('Tem certeza que deseja excluir este cadastro da newsletter?')){
		window.location.href = '/funcionarios/newsletter/excluir/' + id + '/';
	}

}