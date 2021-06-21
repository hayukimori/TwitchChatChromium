# TwitchChatChromium


Este é um script simples em python pra facilitar o popup de chats da twitch. O script usa chromium;



### Requisitos
-Chromium 
-Sistema UNIX

Você pode instalar o chromium com:
`sudo apt-get install chromium-browser`


### Uso
Para usar via linha de comando, pode escrever
`
./popupchat_twitch {nome_do_canal}
`
dentro da pasta. Ou você pode copiar o arquivo [bin](https://github.com/hayukimori/TwitchChatChromium/releases/download/v_01/popupchat_twitch) para `/usr/bin/` para usar sem estar na pasta:

` chmod +x ./popupchat_twitch && sudo cp ./popupchat_twitch /usr/bin/`



OBS:: Este programa é apenas um "atalho" para o comando ```chromium --chrome-frame --window-size=400,640 --app=https://www.twitch.tv/popout/{nome_do_canal}/chat```

