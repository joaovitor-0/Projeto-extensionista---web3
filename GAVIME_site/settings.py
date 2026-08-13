{% load static %}

<!DOCTYPE html>
<html>
	<head>
		<title>Login - GAVIME</title>
		<meta charset = 'UTF-8'>
		<link rel = "stylesheet" href = "{% static 'css/style.css' %}">
		<link rel = "icon" href = "{% static 'img/icon.ico' %}">
		<meta name = 'viewport' content = 'width=device-width, initial-scale=1.0'>
	</head>

	<body>
		<section class = 'conteudo'>
			<div class = 'topoPainel'>
				<h1>Área de Funcionários</h1>
			</div>

			<form method = 'POST' class = 'formularioPagina'>
				{% csrf_token %}

				<div class = 'campo'>
					<label>Usuário</label>
					<input type = 'text' name = 'username' required>
				</div>

				<div class = 'campo'>
					<label>Senha</label>
					<input type = 'password' name = 'password' required>
				</div>

				{% if form.errors %}
					<div class = 'mensagemErro'>
						Usuário ou senha inválidos.
					</div>
				{% endif %}

				<button class = 'botaoEnviar' type = 'submit'>
					Entrar
				</button>
			</form>
		</section>
	</body>
</html>