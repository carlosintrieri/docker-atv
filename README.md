<h1>Formulário de Cadastro</h1>
<p>Desenvolvido em HTMLS, CSS, Flask e integrado ao banco de dados MySQL</p>

![Interface](https://user-images.githubusercontent.com/98194579/185707053-28db23d8-49eb-49cf-8181-f96f56341d2c.png)

<h2>Validators</h2>

![Validators](https://user-images.githubusercontent.com/98194579/185708161-2cbf7dbd-a50a-4780-ba9d-50f17e3a460b.png)

<p>Basicamente, os validators inseridos não deixam que haja usuários duplicados com mesmo username ou email, não deixa que seja inserido algum e-mail inválido e também confere se a senha é igual a confirmação.</p>

<h2>Integração MySQL</h2>

![MySQL](https://user-images.githubusercontent.com/98194579/185709033-3f478e3a-30ae-4664-ad1d-9873aa9ddf77.png)

<p>Estando os validators ok, o usuário é cadastrado no banco de dados com sua senha criptografada. <strong>PS: </strong>Usei a Lib Bcrypt para criptografar as senhas no banco de dados. (Todos os e-mails são fictícios)</p>

<p>Estando cadastrado o usuário é retornado para uma página que confirma que tudo funcionou de forma correta.</p>

![Home Page](https://user-images.githubusercontent.com/98194579/185711215-32b8f3d6-ea7d-4493-9bf2-866d2dffcca6.png)

<p>Simples mas integra várias funcionalidades legais do flask e do MySQL, espero que gostem.</p>
<h3>Desenvolvido por Rychard Mazarin</h3>

