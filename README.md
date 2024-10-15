<p align=center><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=4000&pause=1000&color=F70000&width=435&lines=THIS+BOT+IS+WRITTEN+IN+PY-CORD" alt="Typing SVG" /></a></p>
<p align=center>
<a href="https://github.com/Simoneeeeeeee/Discord-Select-Menu-Ticket-Bot"><img src="https://img.shields.io/github/stars/Simoneeeeeeee/Discord-Select-Menu-Ticket-Bot?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
<a href="https://github.com/Simoneeeeeeee/Discord-Select-Menu-Ticket-Bot/archive/refs/heads/main.zip"><img src="https://custom-icon-badges.demolab.com/badge/-Download-F25278?style=for-the-badge&logo=download&logoColor=white"><a>
<a href="https://discord.com/invite/ycZDpat7dB" target="blank">
<img src="https://img.shields.io/discord/1096820059940331530?label=Join%20Community&logo=discord&style=flat-square" alt="Join Discord Server"/></a>
</p>
<p align=center>這是一個簡單的Ticket機器人，帶有選擇菜單，並且易於定制</p>

- ### 預覽
    <a align=left href='https://imgur.com/a/Z3wAn4c' target="_blank">Imgur Website</a>
- ### 更新 v.1.8
 - 修復了錯誤
 - 在日誌中新增建立/關閉時間戳
- ### 安裝所有必要的功能插件
  ```sh
        pip install py-cord==2.4.0

        pip install asyncio

        pip install pytz

        pip install datetime

        pip install chat-exporter

        or you can use pip install -r requirements.txt
    ``` 
- ### 如何設定`config.json`
    ```sh
        {
      "token": "",                 <- Your Bot Token from https://discord.dev
      "guild_id": 123,             <- Your Server ID aka Guild ID  
      "ticket_channel_id": 123,    <- Ticket Channel where the Bot should send the SelectMenu + Embed
      "category_id_1": 123,        <- Category 1 where the Bot should open the Ticket for the Ticket option 1
      "category_id_2": 123,        <- Category 2 where the Bot should open the Ticket for the Ticket option 2
      "team_role_id_1": 123,       <- Staff Team role id
      "team_role_id_2": 123,       <- Staff Team role id
      "log_channel_id": 123,       <- Where the Bot should log everything 
      "timezone": "CET"            <- Timezone use https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List and use the Category 'Time zone abbreviation' for example: Europe = CET, America = EST so you put in EST or EST ...
      "embed_title": "Support-Tickets",
      "embed_description": "Here you can open a Support Ticket!"
    ```
- ### All Commands
  - `/ticket`
  - `/delete`
  - `/add`
  - `/remove`

- ### How to use Custom emojis from your Discors Server in the Select Menu
  - `Type in the Chat \ but do not send it, now Choose one Emoji that is one your server and press on it. Now it should look like that \<:emoji_name:emoji_id> now just remove the \ and paste the rest in your Code and here you go.`
- ### Discord
  - <a href="https://discord.gg/ycZDpat7dB">Join my DC Server for help and create an Ticket</a>
  - <a>If you want to Support me give this Project a Star </a>
  - https://discord.gg/ycZDpat7dB
  
<p align="center">Apache License 2.0</p>
