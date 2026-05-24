const telefone = document.getElementById('telefone');

telefone.addEventListener('input', function(e){
	let valor = e.target.value;
	valor = valor.replace(/\D/g, '');
	valor = valor.replace(/^(\d{2})(\d)/g, '($1) $2');
	valor = valor.replace(/(\d{5})(\d)/, '$1-$2');
	e.target.value = valor;

});