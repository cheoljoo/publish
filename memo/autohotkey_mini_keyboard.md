- description : 구매한 autohotkey와 mini keyboard의 사용 조합에 대한 페이지이다.
- tag : autohotkey , mini-keyboard
- date : 2024-01-01
- 
TOC
- [1. mini keyboard](#1-mini-keyboard)
- [2. autohotkey](#2-autohotkey)


-----------------------

# 1. mini keyboard
- mini keyboard download : https://drive.google.com/drive/folders/1uSfp62Uia9s6A395sJeHKCcPng3XLcJK
  - ![](../../img/mini_keyboard.png)

# 2. autohotkey
- youtube Ctrl+Mouse_left_click
- vpc minimize when you move the bar into top-left on the screen
- youtube click the 'LIKE'
```
^!e::
{
    Send "^{Click}"
    ;MouseClick "right",10,10,R
    ;if WinExist("ahk_class Notepad")
        ;WinActivate  ; Activate the window found above
    ;else
        ;Run "notepad"  ; Open a new Notepad window
}

count := 0
^!F10:: ; Ctrl + ALT+ F10 (로컬전환)  
        ;MouseGetPos prevX, prevY
                ;CoordMode Mouse, Screen
                ;MouseMove -836, 100, 10
                ;MouseMove 200, 0, 0
                ;MouseMove 53, 3, 10
                ;CoordMode Tooltip, Screen
                ;MouseMove 53, 0, 0
                ;Click ; 현재 마우스 위치에서 왼쪽 버튼 클릭
                ;MouseClick left, 53, 3

                CoordMode Mouse, Screen
	  MouseMove 0, 0
                MouseClick Right, -835, -2159 ,1, R
                MouseClick Left, -788 , -2138 ,1, R
                MouseMove 10, 10
return

^!F9:: ; Ctrl + ALT+ F9
                CoordMode Mouse, Screen
	  MouseMove 200, 200
                ;MouseClick Right, -835, -2159 ,2, R
                MouseClick Left, 868 , 948 ,1, R
                MouseMove 200, 200
return
```