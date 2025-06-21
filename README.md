# 🔓 MD5 Cracker 🧠

<br>

## 📃 Descrição do Projeto

Este projeto tem como objetivo demonstrar, de forma simples e didática, como funciona o processo de quebra de hashes MD5 utilizando uma wordlist.

<br>O script simula o funcionamento de ferramentas de *cracking* conhecidas, comparando um hash MD5 de entrada com os hashes gerados a partir de cada linha de uma wordlist, até encontrar a correspondência.

<br>Fonte xpsecsecurity: https://www.instagram.com/p/CuDQx60A4Wx/?utm_source=ig_web_copy_link&igsh=YzI0a2FwM2FkeXVy


## ⚙️ Funcionamento

1. O script recebe como entrada um **hash MD5** e uma **wordlist**;
2. Converte cada linha da wordlist para hash MD5;
3. Compara o hash gerado com o hash fornecido pelo usuário;
4. Ao encontrar uma correspondência, exibe a senha em texto claro.


## 🖥️ Tecnologia Utilizada

* Python


## 📌 Exemplo de Uso

```bash
python md5_cracker.py -h 5d41402abc4b2a76b9719d911017c592 -w wordlist.txt
```
