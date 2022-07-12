# sesac_python_basic
___
### git add . 할때 'warning ~~~, LF will be replaced by CRLF the next time Git touches it'의미
    #### LF(Line Feed)
        - mac, linux 줄바꿈 문자열은 \n
        - ascii code는 10
        - 커서 위치는 그대로 두고 종이의 한 라인 위로 올리는 동작
    #### CR(Carriage-Return)
        - mac 초기 모델 줄바꿈 문자열 \r
        - ascii code는 13
        - 커서 위치를 맨 앞으로 옮김
    #### CRLF(CR + LF)
        - windows, dos 줄바꿈 문자열 \r\n
        - 커서를 다음라인 맨 앞으로 옮김

    - 플랫폼(mac, linux, windows, dos)마다 줄바꿈을 바라보는 문자열이 달라 git이 둘 중 어느 곳을 선택할 지 몰라 경고 메시지를 띄우는 것.
    - 즉, LF will be replaced by CRLF the next time Git touches it은 '너 windows(dos) 쓰는거로 간주한다?'라는 의미
