function copiarPix(){

	var chavePix = document.getElementById('chavePix').innerText.trim();

	navigator.clipboard.writeText(chavePix);

	var mensagem = document.getElementById('mensagemPix');

	mensagem.style.opacity = '1';

	setTimeout(function(){
		mensagem.style.opacity = '0';
	}, 2000);

}