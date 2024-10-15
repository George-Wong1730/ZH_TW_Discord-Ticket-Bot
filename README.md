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

        或者使用 `pip install -r requirements.txt`
    ``` 
- ### 設定`config.json`
    ```sh
        {
      "token": "",                 <- 你的機器人 Token from https://discord.dev
      "guild_id": 123,             <- 你的伺服器 ID aka Guild ID  
      "ticket_channel_id": 123,    <- 機器人應發送 SelectMenu + Embed 的工單通道
      "category_id_1": 123,        <- 類別 1，機器人應開啟工單選項 1 的工單
      "category_id_2": 123,        <- 類別 2，機器人應開啟工單選項 2 的工單
      "team_role_id_1": 123,       <- 員工團隊角色 ID
      "team_role_id_2": 123,       <- 員工團隊角色 ID
      "log_channel_id": 123,       <- 機器人應該記錄所有內容的地方
      "timezone": "CET"            <- 時區使用
     https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List and use the Category 'Time zone abbreviation' for example: Europe = CET, America = EST so you put in EST or EST ...
      "embed_title": "Support-Tickets",
      "embed_description": "Here you can open a Support Ticket!"
    ```
- ### 所有指令
  - `/ticket`
  - `/delete`
  - `/add`
  - `/remove`

- ### 如何在選擇選單中使用 Discord 伺服器中的自訂表情符號
  - `輸入聊天 \ 但不要發送它，現在選擇一個屬於您的伺服器的表情符號並按下它。現在它應該看起來像 \<:emoji_name:emoji_id> 現在只需刪除 \ 並將其餘部分貼到您的程式碼中即可。`
- ### Discord
  - <a href="https://discord.gg/ycZDpat7dB">Join my DC Server for help and create an Ticket</a>
  - <a>If you want to Support me give this Project a Star </a>
  - https://discord.gg/ycZDpat7dB
  
<p align="center">Apache License 2.0</p>
