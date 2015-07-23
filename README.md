Two factory lab
===============

Laboratório de Two factory authentication na GaragemHacker.


O que é?
--------

É um processo de segurança em que o usuário fornece dois meios de identificação, que geralmente consiste de 
um código que varia de 6 a 8 números é pode ser gerado por [software](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en) ou [hardware](https://www.yubico.com/products/yubikey-hardware/) dedicado. Para mais informações
veja [wikipedia](https://en.wikipedia.org/wiki/Two-factor_authentication)


Como funciona?
--------------

Ao iniciar uma sessão de autenticação na sua conta duas coisas acontecem:

1. Solicita sua senha como de costume.
2. Solicita um código que gerado via hardware ou enviado via SMS ou chamada de voz.

[Mais informação aqui](https://www.google.com/landing/2step/#tab=how-it-works)

Atividade
=========

Fazer algun hardwar gerador de código de 2-step como:

* http://hackaday.com/2015/07/20/hackaday-prize-entry-two-factor-authentication-key/
* http://hackaday.com/2012/07/11/time-based-one-time-passwords-with-an-arduino/#more-79343

> Outro hardware que pode ser usado é um raspberry pi com um LCD para monstrar os códigos e
> a picamera para ler o QRcode de sincronização.

Alguns exemplos de sofwate e libs:

* https://github.com/lucadentella/ArduinoLib_TOTP
* https://github.com/damico/ARDUINO-OATH-TOKEN
* https://github.com/google/google-authenticator
* https://github.com/google/google-authenticator-android
* https://cryptography.io/en/latest/hazmat/primitives/twofactor/
* https://github.com/google/google-authenticator/wiki/Key-Uri-Format


Sorce code
===========

Aplicação Python no terminal para funcionar como two factory server.

```
mkproject --python=/bin/python3.4 two-factor
git clone https://github.com/Garagem-Hacker/two-factor.git .
pip install -U pip setuptools
pip install -r requirements.txt
```


RFCs
====

* [RFC 6238 - TOTP: Time-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc6238.html)
* [RFC 4226 - HOTP: An HMAC-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc4226.html)
