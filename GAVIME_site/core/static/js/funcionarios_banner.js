document.addEventListener('DOMContentLoaded', function () {
    const linhas = Array.from(
        document.querySelectorAll('.linhaBanner')
    );

    const botaoEditar = document.getElementById(
        'editarBannerSelecionado'
    );

    const botaoExcluir = document.getElementById(
        'excluirBannerSelecionado'
    );

    const botaoStatus = document.getElementById(
        'statusBannerSelecionado'
    );

    const formularioExcluir = document.getElementById(
        'formExcluirBanner'
    );

    const formularioStatus = document.getElementById(
        'formStatusBanner'
    );

    let linhaSelecionada = null;

    function atualizarBotoes() {
        const possuiSelecao = linhaSelecionada !== null;

        if (botaoEditar) {
            botaoEditar.disabled = !possuiSelecao;
        }

        if (botaoExcluir) {
            botaoExcluir.disabled = !possuiSelecao;
        }

        if (botaoStatus) {
            botaoStatus.disabled = !possuiSelecao;
        }
    }

    function selecionarLinha(linha) {
        linhas.forEach(function (item) {
            item.classList.remove(
                'linhaBannerSelecionada'
            );
        });

        const radio = linha.querySelector(
            '.seletorBanner'
        );

        if (radio) {
            radio.checked = true;
        }

        linha.classList.add(
            'linhaBannerSelecionada'
        );

        linhaSelecionada = linha;

        atualizarBotoes();
    }

    linhas.forEach(function (linha) {
        linha.addEventListener(
            'click',
            function (evento) {
                if (
                    evento.target.closest('a') ||
                    evento.target.closest('button')
                ) {
                    return;
                }

                selecionarLinha(linha);
            }
        );

        const radio = linha.querySelector(
            '.seletorBanner'
        );

        if (radio) {
            radio.addEventListener(
                'change',
                function () {
                    selecionarLinha(linha);
                }
            );
        }
    });

    if (botaoEditar) {
        botaoEditar.addEventListener(
            'click',
            function () {
                if (!linhaSelecionada) {
                    return;
                }

                window.location.href =
                    linhaSelecionada.dataset.editarUrl;
            }
        );
    }

    if (botaoStatus) {
        botaoStatus.addEventListener(
            'click',
            function () {
                if (!linhaSelecionada) {
                    return;
                }

                const confirmar = window.confirm(
                    'Deseja alterar o status deste banner?'
                );

                if (!confirmar) {
                    return;
                }

                formularioStatus.action =
                    linhaSelecionada.dataset.statusUrl;

                formularioStatus.submit();
            }
        );
    }

    if (botaoExcluir) {
        botaoExcluir.addEventListener(
            'click',
            function () {
                if (!linhaSelecionada) {
                    return;
                }

                const confirmar = window.confirm(
                    'Deseja realmente excluir o banner selecionado? Essa ação não poderá ser desfeita.'
                );

                if (!confirmar) {
                    return;
                }

                formularioExcluir.action =
                    linhaSelecionada.dataset.excluirUrl;

                formularioExcluir.submit();
            }
        );
    }

    atualizarBotoes();
});