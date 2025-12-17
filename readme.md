## Sistema de validacao de CEP

Mini-projeto de validacao de CEP via API ViaCep do IBGE.
O projeto consiste em uma classe no qual valida os CEPs enviados pelos usuarios.

---

## Funcionalidades

### Classe

**CepConsult** -> Esta classe tem o proposito de conseguir validar, os CEPs de todo o Brasil usando a API ViaCep.

#### Atributo

* **cep_ (tupla):** Uma tupla de CEPs brasileiros para ser validados.

#### Metodos

* **validate_cep()** -> Valida e consulta os CEPs pela API. O retorno do metodo e uma `lista de dicionarios` com os valores sendo "cep (int)", "Not found" e "Invalid", dentro dos valor no qual o cep e a chave tem todos os dados referente ao cep, ja nos valores "Not found" e "Invalid" contem apenas uma lista de numeros.

* **return_cep_validate()** -> Exibe o resultado dos CEPs no terminal e chama o metodo **_save_in_json_file()** passando uma lista no qual contem os CEPs validos, invalidos e nao encontrados. O retorno deste metodo é `None`.

* **_save_in_json_file()** -> Este metodo salva o resultado da consulta em um arquivo JSON. A estrutura do arquivo JSON é um dicionario com 3 chaves sendo elas: "Valid CEPs" no qual contem todos os CEPs validos, "Invalid CEPs" contendo todos os CEPs invalidos e por ultimo "Not Found CEPs" no qual guarda todos os CEPs no qual nao foi possivel encontrar nenhum tipo de dados. O retorno deste metodo é `None`

---

## Tecnologias

* Python 3.13

---

## Site oficial da API ViaCep

* [https://viacep.com.br/](https://viacep.com.br/)
