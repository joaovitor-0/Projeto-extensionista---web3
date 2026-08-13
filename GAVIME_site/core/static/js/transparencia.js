let linhaSelecionada = null;

const linhas = document.querySelectorAll('.linhaTransparencia');

const botaoEditar = document.getElementById('editarTransparencia');

const botaoExcluir = document.getElementById('excluirTransparencia');

linhas.forEach(linha => {
    linha.addEventListener('click', () => {
        linhas.forEach(l => l.classList.remove('linhaSelecionada'));
        linha.classList.add('linhaSelecionada');
        linhaSelecionada = linha;

    });

});

botaoEditar.addEventListener('click', () => {
    if (linhaSelecionada) {
        window.location.href = linhaSelecionada.dataset.editar;
    }

    else {
        alert('Selecione um registro primeiro.');
    }

});

botaoExcluir.addEventListener('click', () => {
    if (linhaSelecionada) {
        const confirmar = confirm('Tem certeza que deseja excluir este registro?');

        if (confirmar) {
            window.location.href = linhaSelecionada.dataset.excluir;
        }

    }

    else {

        alert('Selecione um registro primeiro.');

    }

});