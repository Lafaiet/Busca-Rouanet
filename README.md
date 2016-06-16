# Busca Rouanet

[![Gitter](https://badges.gitter.im/Lafaiet/Busca-Rouanet.svg)](https://gitter.im/Lafaiet/Busca-Rouanet?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Lafaiet/Busca-Rouanet/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/gpl/gpl.svg?v=102)](http://www.gnu.org/licenses/gpl.html)



Portal para buscas de dados referentes a Lei Rouanet.
Esse portal serve como alternativa ao já existente [SALIC](http://novosalic.cultura.gov.br/cidadao/consultar).
A ideia é fazer uso da [API](https://github.com/Lafaiet/salicapi) do SALIC (ainda em desenvolvimento) para compor uma base de dados local e prover acesso de forma mais direta, fácil e intuitiva. Trata-se de um projeto **independente**, sem vinculação direta com órgãos governamentais.

## Execução

Faça um clone desse repositório e execute:

```bash
$ sudo pip install -r requirements.txt
```

Dentro da pasta ```src``` execute:

```bash
python manage.py runserver
```

Acesse a página inicial em:

[http://localhost:8000](http://localhost:8000)

A página de admin está em:

[http://localhost:8000/admin](http://localhost:8000/admin)

O usuário e senha padrão é ```admin```


## License

Licensed under the [GPL License](http://www.gnu.org/licenses/gpl.html).
