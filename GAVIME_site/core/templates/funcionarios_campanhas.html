{% load static %}

<!DOCTYPE html>

<html lang="pt-br">

	<head>

		<title>GAVIME - Campanhas</title>

		<meta charset="UTF-8">

		<link
			rel="stylesheet"
			href="{% static 'css/style.css' %}"
		>

		<link
			rel="icon"
			href="{% static 'img/icon.ico' %}"
		>

		<meta
			name="viewport"
			content="width=device-width, initial-scale=1.0"
		>

		<link
			rel="stylesheet"
			href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
		>

	</head>

	<body id="topo">

		<header>

			<div class="cabecalho">

				<a href="{% url 'funcionarios_inicio' %}">

					<img
						src="{% static 'img/logoGavime.png' %}"
						class="logo"
						alt="Logo GAVIME"
					>

				</a>

				<nav>

					<a href="{% url 'funcionarios_inicio' %}">
						Painel
					</a>

					<a href="{% url 'funcionarios_atividades' %}">
						Ações
					</a>

					<a href="{% url 'funcionarios_inscritos' %}">
						Inscritos
					</a>

					<a href="{% url 'funcionarios_voluntarios' %}">
						Voluntários
					</a>

					<a href="{% url 'despesas' %}">
						Transparência
					</a>

					<a href="{% url 'funcionarios_newsletter' %}">
						Newsletter
					</a>

					<a href="{% url 'funcionarios_banner' %}">
						Banners
					</a>

					<a href="{% url 'funcionarios_campanhas' %}">
						Campanhas
					</a>

					<a href="{% url 'index' %}">
						Site principal
					</a>

				</nav>

			</div>

		</header>

		<section class="conteudo">

			<div class="topoPainel">

				<h1>
					Gerenciar campanhas
				</h1>

			</div>

			{% if messages %}

				<div class="mensagensSistema">

					{% for message in messages %}

						<div class="mensagemSistema {{ message.tags }}">
							{{ message }}
						</div>

					{% endfor %}

				</div>

			{% endif %}

			<div class="areaTabelaFuncionarios">

				<div class="cabecalhoAreaAdministrativa">

					<div>

						<h2>
							Campanhas cadastradas
						</h2>

						<p>
							Gerencie as campanhas de arrecadação exibidas no site.
						</p>

					</div>

					<a
						href="{% url 'funcionarios_campanha_criar' %}"
						class="botaoCadastrarPainel"
					>
						Cadastrar campanha
					</a>

				</div>

				<form
					method="GET"
					class="formularioFiltrosTabela"
				>

					<input
						type="text"
						name="busca"
						placeholder="Título da campanha"
						value="{{ busca }}"
					>

					<select name="status">

						<option value="">
							Todos os status
						</option>

						<option
							value="ativas"
							{% if status == "ativas" %}selected{% endif %}
						>
							Ativas
						</option>

						<option
							value="inativas"
							{% if status == "inativas" %}selected{% endif %}
						>
							Inativas
						</option>

						<option
							value="concluidas"
							{% if status == "concluidas" %}selected{% endif %}
						>
							Concluídas
						</option>

					</select>

					<button type="submit">
						Filtrar
					</button>

					<a href="{% url 'funcionarios_campanhas' %}">
						Limpar
					</a>

				</form>

				<div class="tabelaContainer">

					<table class="tabelaFuncionarios tabelaCampanhas">

						<thead>

							<tr>

								<th>
									Imagem
								</th>

								<th>
									Campanha
								</th>

								<th>
									Meta
								</th>

								<th>
									Arrecadado
								</th>

								<th>
									Progresso
								</th>

								<th>
									Status
								</th>

								<th>
									Ordem
								</th>

								<th>
									Ações
								</th>

							</tr>

						</thead>

						<tbody>

							{% for campanha in campanhas %}

								<tr>

									<td>

										{% if campanha.imagem %}

											<img
												src="{{ campanha.imagem.url }}"
												alt="{{ campanha.titulo }}"
												class="miniaturaCampanha"
											>

										{% else %}

											<span class="semImagemCampanha">
												Sem imagem
											</span>

										{% endif %}

									</td>

									<td>

										<strong>
											{{ campanha.titulo }}
										</strong>

										{% if campanha.descricao %}

											<small class="descricaoTabelaCampanha">
												{{ campanha.descricao|truncatechars:90 }}
											</small>

										{% endif %}

										{% if campanha.data_inicio or campanha.data_fim %}

											<small class="datasTabelaCampanha">

												{% if campanha.data_inicio %}

													Início:
													{{ campanha.data_inicio|date:"d/m/Y" }}

												{% endif %}

												{% if campanha.data_inicio and campanha.data_fim %}
													•
												{% endif %}

												{% if campanha.data_fim %}

													Fim:
													{{ campanha.data_fim|date:"d/m/Y" }}

												{% endif %}

											</small>

										{% endif %}

									</td>

									<td>

										R$
										{{ campanha.meta|floatformat:2 }}

									</td>

									<td>

										R$
										{{ campanha.valor_arrecadado|floatformat:2 }}

									</td>

									<td>

										<div class="progressoTabelaCampanha">

											<div class="barraProgressoTabelaCampanha">

												<div
													class="preenchimentoProgressoTabelaCampanha"
													style="width: {{ campanha.percentual }}%;"
												>
												</div>

											</div>

											<span>
												{{ campanha.percentual_real|floatformat:1 }}%
											</span>

										</div>

									</td>

									<td>

										{% if campanha.concluida %}

											<span class="statusCampanha statusCampanhaConcluida">
												Concluída
											</span>

										{% elif campanha.ativa %}

											<span class="statusCampanha statusCampanhaAtiva">
												Ativa
											</span>

										{% else %}

											<span class="statusCampanha statusCampanhaInativa">
												Inativa
											</span>

										{% endif %}

									</td>

									<td>
										{{ campanha.ordem }}
									</td>

									<td>

										<div class="acoesTabelaAdministrativa">

											<a
												href="{% url 'funcionarios_campanha_editar' campanha.id %}"
												class="botaoEditarSelecionado botaoAcaoTabela"
											>
												Editar
											</a>

											<form
												method="POST"
												action="{% url 'funcionarios_campanha_alterar_status' campanha.id %}"
											>

												{% csrf_token %}

												<button
													type="submit"
													class="botaoStatusAdministrativo"
												>

													{% if campanha.ativa %}

														Desativar

													{% else %}

														Ativar

													{% endif %}

												</button>

											</form>

											<form
												method="POST"
												action="{% url 'funcionarios_campanha_excluir' campanha.id %}"
												onsubmit="return confirm('Deseja realmente excluir esta campanha?');"
											>

												{% csrf_token %}

												<button
													type="submit"
													class="botaoExcluirSelecionado botaoAcaoTabela"
												>
													Excluir
												</button>

											</form>

										</div>

									</td>

								</tr>

							{% empty %}

								<tr>

									<td
										colspan="8"
										class="mensagemTabelaVazia"
									>
										Nenhuma campanha encontrada.
									</td>

								</tr>

							{% endfor %}

						</tbody>

					</table>

				</div>

			</div>

		</section>

		<footer>

			<div class="footerContainerFuncionarios">

				<div class="footerLogo">

					<a href="#topo">

						<img
							src="{% static 'img/logoGavime.png' %}"
							class="logoFooter"
							alt="Logo GAVIME"
						>

					</a>

				</div>

				<p class="direitos">
					©2026 - GAVIME. Todos os direitos reservados.
				</p>

			</div>

		</footer>

	</body>

</html>
