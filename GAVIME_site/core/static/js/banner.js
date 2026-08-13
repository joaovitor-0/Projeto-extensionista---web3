document.addEventListener('DOMContentLoaded', function () {

    const banner = document.getElementById('bannerPrincipal');

    if (!banner) {
        return;
    }

    const slides = Array.from(
        banner.querySelectorAll('[data-banner-slide]')
    );

    const indicadores = Array.from(
        banner.querySelectorAll('[data-banner-indicador]')
    );

    const botaoAnterior = document.getElementById('bannerAnterior');
    const botaoProximo = document.getElementById('bannerProximo');

    const temporizador = banner.querySelector(
        '.bannerTemporizador'
    );

    if (slides.length <= 1) {
        return;
    }

    const duracaoSlide = 6000;

    let indiceAtual = 0;

    let bannerPausado = false;
    let paginaOculta = document.hidden;

    let toqueInicial = null;

    let animacaoContagem = null;
    let inicioContagem = null;
    let tempoRestante = duracaoSlide;

    function mostrarSlide(indice) {

        if (indice < 0) {
            indice = slides.length - 1;
        }

        if (indice >= slides.length) {
            indice = 0;
        }

        slides.forEach(function (slide, posicao) {

            const ativo = posicao === indice;

            slide.classList.toggle(
                'bannerSlideAtivo',
                ativo
            );

            slide.setAttribute(
                'aria-hidden',
                ativo ? 'false' : 'true'
            );

        });

        indicadores.forEach(function (indicador, posicao) {

            indicador.classList.toggle(
                'bannerIndicadorAtivo',
                posicao === indice
            );

        });

        indiceAtual = indice;

    }

    function proximoSlide() {
        mostrarSlide(indiceAtual + 1);
    }

    function slideAnterior() {
        mostrarSlide(indiceAtual - 1);
    }

    function atualizarProgresso() {

        if (!temporizador) {
            return;
        }

        const tempoPassado =
            duracaoSlide - tempoRestante;

        const percentual =
            Math.min(
                100,
                Math.max(
                    0,
                    (tempoPassado / duracaoSlide) * 100
                )
            );

        temporizador.style.setProperty(
            '--progresso-banner',
            percentual + '%'
        );

    }

    function cancelarAnimacao() {

        if (animacaoContagem !== null) {

            cancelAnimationFrame(animacaoContagem);
            animacaoContagem = null;

        }

    }

    function executarContagem(timestamp) {

        if (bannerPausado || paginaOculta) {
            return;
        }

        if (inicioContagem === null) {
            inicioContagem = timestamp;
        }

        const tempoDecorrido =
            timestamp - inicioContagem;

        const tempoAtual =
            Math.max(
                0,
                tempoRestante - tempoDecorrido
            );

        const percentual =
            Math.min(
                100,
                Math.max(
                    0,
                    (
                        (
                            duracaoSlide - tempoAtual
                        ) / duracaoSlide
                    ) * 100
                )
            );

        if (temporizador) {

            temporizador.style.setProperty(
                '--progresso-banner',
                percentual + '%'
            );

        }

        if (tempoAtual <= 0) {

            proximoSlide();

            tempoRestante = duracaoSlide;
            inicioContagem = timestamp;

            if (temporizador) {

                temporizador.style.setProperty(
                    '--progresso-banner',
                    '0%'
                );

            }

        }

        animacaoContagem =
            requestAnimationFrame(executarContagem);

    }

    function iniciarContagem() {

        cancelarAnimacao();

        if (bannerPausado || paginaOculta) {
            return;
        }

        inicioContagem = null;

        animacaoContagem =
            requestAnimationFrame(executarContagem);

    }

    function pausarContagem() {

        if (inicioContagem !== null) {

            const agora = performance.now();

            const tempoDecorrido =
                agora - inicioContagem;

            tempoRestante =
                Math.max(
                    0,
                    tempoRestante - tempoDecorrido
                );

        }

        inicioContagem = null;

        cancelarAnimacao();
        atualizarProgresso();

    }

    function reiniciarContagem() {

        cancelarAnimacao();

        tempoRestante = duracaoSlide;
        inicioContagem = null;

        if (temporizador) {

            temporizador.style.setProperty(
                '--progresso-banner',
                '0%'
            );

        }

        iniciarContagem();

    }

    if (botaoAnterior) {

        botaoAnterior.addEventListener(
            'click',
            function () {

                slideAnterior();
                reiniciarContagem();

            }
        );

    }

    if (botaoProximo) {

        botaoProximo.addEventListener(
            'click',
            function () {

                proximoSlide();
                reiniciarContagem();

            }
        );

    }

    indicadores.forEach(function (indicador) {

        indicador.addEventListener(
            'click',
            function () {

                const indice = Number(
                    indicador.dataset.bannerIndicador
                );

                mostrarSlide(indice);
                reiniciarContagem();

            }
        );

    });

    banner.addEventListener(
        'mouseenter',
        function () {

            bannerPausado = true;

            banner.classList.add(
                'bannerPausado'
            );

            pausarContagem();

        }
    );

    banner.addEventListener(
        'mouseleave',
        function () {

            bannerPausado = false;

            banner.classList.remove(
                'bannerPausado'
            );

            iniciarContagem();

        }
    );

    banner.addEventListener(
        'touchstart',
        function (evento) {

            toqueInicial =
                evento.changedTouches[0].clientX;

        },
        {
            passive:true
        }
    );

    banner.addEventListener(
        'touchend',
        function (evento) {

            if (toqueInicial === null) {
                return;
            }

            const toqueFinal =
                evento.changedTouches[0].clientX;

            const diferenca =
                toqueInicial - toqueFinal;

            if (Math.abs(diferenca) > 50) {

                if (diferenca > 0) {

                    proximoSlide();

                } else {

                    slideAnterior();

                }

                reiniciarContagem();

            }

            toqueInicial = null;

        },
        {
            passive:true
        }
    );

    document.addEventListener(
        'visibilitychange',
        function () {

            paginaOculta = document.hidden;

            if (paginaOculta) {

                pausarContagem();

            } else if (!bannerPausado) {

                iniciarContagem();

            }

        }
    );

    mostrarSlide(0);
    reiniciarContagem();

});
