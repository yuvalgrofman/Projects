IDEAL
MODEL small
STACK 100h
jumps
p186
DATASEG

;initializing variables 
;Cursor location 
y db 0
x db 0

;@ 
@_x db 0
@_y db 0

;make symbol 
xSymbol db 0
ySymbol db 0
Symbol db '0'

;Num Loops Invert
numLoopsInvert db 0
shouldInvert db 0

p1_or_p2_plus db 0

moveLoopCounter db 0

;drawPlayer
color db 1

;Delay
delayTimeHighWord db 2
delayTimeLowWord dw 4240h

;randomNum
randomNum db 0

counter db 0

;movePlayer Up/Right/Down/Left
x_move db 0
y_move db 0
col_move db 0

p1LostString db 'Blue Player lost  ',10,13,'$'
p2LostString db 'Green Player lost ',10,13,'$'

y1_row db 0
x1_column db 0 
p1_dir db 's'
p1_col db 1
p1_wins db 0 

y2_row db 0
x2_column db 0 
p2_dir db 's'
p2_col db 2
p2_wins db 0 

colorPlayerone db 1 
colorPlayerTwo db 2 

line db 10, 13, '$'

numLoopsWaitForCharacter db 0

plus_x db 0 
plus_y db 0

menu	db '    _      _   _                  ', 10, 13
        db '   /_\  __| |_| |_ _  _ _ _  __ _ ', 10, 13
        db '  / _ \/ _|   \  _| || |   \/ _` |', 10, 13
        db ' /_/ \_\__|_||_\__|\_,_|_||_\__, |', 10, 13
        db '                            |___/', 10,13,10,13
        db '> press p to play', 10, 13,10,13
        db '> press Esc to close', 10, 13,'$'

credits db 'Made by Yuval Grofman','$' 



explanation	db 'How to play?                ', 10, 13, 10, 13
        db 'move around the map, ', 10, 13
        db 'Without touching the stars -> *', 10, 13
        db 'Also eating "orbs" give special effects.   ', 10, 13, 10, 13
        db '@ - This will speed or slow both players', 10,13
        db '+ - This will clear the map ', 10,13,10,13 
        db '> Press any key to continue ', '$'
    
EndGameStr db 10,13,'Good Game, Hope everybody had fun!',10,13,'$'

playAgain db 'Do you want to play again?' ,10,13 
          db ' (y to play, esc to quit)','$'

otherButton db ' press p to play and Esc to Leave :)','$'

scoreP1 db 'The Score is Blue: ','$'

scoreP2 db ' ,Green: ','$'

CODESEG

proc printChar 
pusha 
mov ah, 2
int 21h
popa
ret 
endp printchar

proc delay
pusha 
mov cx, 0 ;High Word
mov cl, [delayTimeHighWord]
mov dx, [delaytimelowword] ;Low Word
mov al, 0
mov ah, 86h ;Wait
int 15h
popa 
ret 
endp delay

proc graphicMode
;puts the screen in graphic mode 40 on 25 
pusha
mov ax, 13h
int 10h
popa
ret 
endp graphicMode

proc waitForInput
;waits for user input then puts the key pressed in al 
mov ah,0h
int 16h
ret 
endp waitforinput

proc textMode
;puts the screen in text mode 80 on 25
pusha
mov al, 03h
mov ah,0
int 10h
popa
ret
endp textMode

proc printStr
;prints the string thats in dx
push ax
mov ah, 9
int 21h
pop ax
ret
endp printStr

proc newLine
; print a new line
pusha
mov dx, offset line
mov ah, 9
int 21h
popa
ret
endp newLine

proc make@ 
;makes a star sign at the location x_column, y_row
pusha 
mov bh, 0
mov dh, [@_y] ; in row
mov dl, [@_x]
mov ah, 2
int 10h

mov ah, 9
mov al, '@' ;AL = character to display
mov bh, 0h ;BH=Page
mov bl, 5; BL = Foreground
mov cx, 1 ; number of times to write character
int 10h ; Bois -&gt; show the character
popa 
ret
endp make@

proc makeSymbol 
;makes a star sign at the location x_#, y_#
pusha 
mov bh, 0
mov dh, [ysymbol]; in row
mov dl, [xsymbol] 
mov ah, 2
int 10h

mov ah, 9
mov al, [symbol] ;AL = character to display
mov bh, 0h ;BH=Page
mov bl, 5; BL = Foreground
mov cx, 1 ; number of times to write character
int 10h ; Bois -&gt; show the character
popa 
ret
endp makeSymbol

proc makePlus 
;makes a plus sign at the location x_column, y_row
pusha 
mov bh, 0
mov dh, [plus_y] ; in row
mov dl, [plus_x]
mov ah, 2
int 10h

mov ah, 9
mov al, '+' ;AL = character to display
mov bh, 0h ;BH=Page
mov bl,  12; BL = Foreground
mov cx, 1 ; number of times to write character
int 10h ; Bois -&gt; show the character
popa 
ret
endp makePlus

proc Cursor_Location
pusha 
;Place the cursor on the screen
mov bh, 0
mov dh, [y] ; in row
mov dl, [x]
mov ah, 2
int 10h
popa 
ret
endp Cursor_Location

proc DrawPlayer
pusha
; draw player in cursor position
mov ah, 9
mov al, 2Ah ;AL = character to display
mov bh, 0h ;BH=Page
mov bl, [color] ; BL = Foreground
mov cx, 1 ; number of times to write character
int 10h ; Bois -&gt; show the character
popa
ret
endp DrawPlayer

proc movePlayerRight 
;moves the player right except if there is a plus or star 
;if there is a star it ends the game 
;if there is a plus it doesnt move
inc [x_move]

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place
;check the character on coordinates
mov bh, 0h ; Page=1
mov ah, 08h ; Read character function
int 10h ;Return the character value to AL
cmp al, '+'
jne MoveRight; Jump to draw player
call clearBoard
call make@
MoveRight:
cmp al,'*'
je AplayerLost

cmp al, '@'
je callChangeSpeedRight
jmp dontCallChangeSpeedRight 
callChangeSpeedRight:
call changeSpeed
dontCallChangeSpeedRight:

cmp al, '#'
je callinvertmovementRight 
jmp dontcallinvertmovementright 
callInvertMovementRight:
call invertMovement
dontCallInvertMovementRight:

mov al, [x_move]
mov [x], al
mov al, [y_move]
mov [y], al

call Cursor_Location; move cursor to new place

mov al, [col_move] 
mov [color], al
call DRAWPLAYER

ret
endp movePlayerRight 

proc MovePlayerLeft
;moves the player left except if there is a plus or star 
;if there is a star it ends the game 
;if there is a plus it doesnt move
dec [x_move] 

mov al, [x_move] 
mov [x], al 
mov al, [y_move]  
mov [y], al 

call Cursor_Location; move cursor to new place
;check the character on coordinates
mov bh, 0h ; Page=1
mov ah, 08h ; Read character function
int 10h ;Return the character value to AL
cmp al, '+'
jne MoveLeft; Jump to draw player
call clearBoard
call make@
MoveLeft:
cmp al,'*'
je AplayerLost  

cmp al, '@'
je callChangeSpeedLeft
jmp dontCallChangeSpeedLeft 
callChangeSpeedLeft:
call changeSpeed
dontCallChangeSpeedLeft:

cmp al, '#'
je callinvertmovementLeft 
jmp dontcallinvertmovementLeft 
callInvertMovementLeft:
call invertMovement
dontCallInvertMovementLeft:

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place

mov al, [col_move] 
mov [color], al
call DRAWPLAYER

ret
endp MovePlayerLeft

proc MovePlayerDown
;moves the player down except if there is a plus or star 
;if there is a star it ends the game 
;if there is a plus it doesnt move
inc [y_move] 

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place
;check the character on coordinates
mov bh, 0h ; Page=1
mov ah, 08h ; Read character function
int 10h ;Return the character value to AL
cmp al, '+'
jne MoveDown; Jump to draw player
call clearBoard
call make@
MoveDown:
cmp al,'*'
je AplayerLost 

cmp al, '@'
je callChangeSpeedDown
jmp dontCallChangeSpeedDown 
callChangeSpeedDown:
call changeSpeed
dontCallChangeSpeedDown:

cmp al, '#'
je callinvertmovementDown 
jmp dontcallinvertmovementDown 
callInvertMovementDown:
call invertMovement
dontCallInvertMovementDown:

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place

mov al, [col_move] 
mov [color], al

call DRAWPLAYER
ret
endp MovePlayerDown

proc MovePlayerUp 
;moves the player up except if there is a plus or star 
;if there is a star it ends the game 
;if there is a plus it doesnt move
dec [y_move] 

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place
;check the character on coordinates
mov bh, 0h ; Page=1
mov ah, 08h ; Read character function
int 10h ;Return the character value to AL
cmp al, '+'
jne MoveUp; Jump to draw player
call clearBoard
call make@
MoveUp:
cmp al,'*'
je AplayerLost 

cmp al, '@'
je callChangeSpeedUp
jmp dontCallChangeSpeedUp 
callChangeSpeedUp:
call changeSpeed
dontCallChangeSpeedUp:

cmp al, '#'
je callinvertmovementUp 
jmp dontcallinvertmovementUp 
callInvertMovementUp:
call invertMovement
dontCallInvertMovementUp:

mov al, [x_move] 
mov [x], al
mov al, [y_move]  
mov [y], al

call Cursor_Location; move cursor to new place

mov al, [col_move] 
mov [color], al

call DRAWPLAYER

ret
endp MovePlayerUp 

proc clearBoard
pusha 
call graphicmode
call createframe
popa 
ret
endp clearBoard

proc invertMovement
mov [shouldinvert], 1
mov [numloopsinvert], 10
ret 
endp invertmovement

proc uninvertMovement
mov [shouldinvert], 0
ret 
endp uninvertmovement

proc changeSpeed 
pusha 
call getrandonNum

mov ah, 0
mov al, [randomnum]

mov bl, 2
div bl 

mov ah, 1
cmp ah, 0
je faster
jmp slower
faster:
mov [delayTimeHighWord], 1
jmp endOfChangeSpeed
slower:
mov [delaytimehighword], 3
endOfChangeSpeed:

;spawning # on map 
mov [xsymbol], 20
mov [ysymbol], 17
mov [symbol], '#'

call makesymbol

popa 
ret
endp changeSpeed

proc createFrame 
pusha 

mov [color], 8

mov [x],0
mov [counter], 0

mov cx, 40 

loop1: 

mov al, [counter]
mov [x], al 
mov [y], 0 

call cursor_location
call drawplayer

mov [x], al  
mov [y], 24

call cursor_location
call drawplayer

inc [counter]

loop loop1

mov cx, 25
mov [counter], 0

loop2: 

mov [x], 0
mov al, [counter]
mov [y], al

call cursor_location
call drawplayer

mov [x], 39
mov [y], al 

call cursor_location
call drawplayer

inc [counter]

loop loop2

popa 
ret
endp createframe

proc getrandonNum
pusha 
MOV AH, 00h  ; interrupts to get system time        
INT 1AH      ; CX:DX now hold number of clock ticks since midnight      

mov  ax, dx
xor  dx, dx
mov  cx, 10    
div  cx       ; here dx contains the remainder of the division - from 0 to 9
mov [randomnum], dl
popa
ret
endp getrandonNum
    

proc movePlayerOne 
pusha 

mov al, [x1_column]
mov [x_move], al
mov al, [y1_row]
mov [y_move], al
mov al, [p1_col]
mov [col_move], al

cmp [p1_dir], 'e'
je movePOneRight

cmp [p1_dir], 'w'
je movePOneLeft

cmp [p1_dir], 's'
je movePOneDown

cmp [p1_dir], 'n'
je movePOneUp

movePOneRight:
call movePlayerRight
jmp endOfMovePlayerOne

movePOneLeft:
call moveplayerleft
jmp endOfMovePlayerOne

movePOneDown:
call moveplayerdown
jmp endOfMovePlayerOne

movePOneUp:
call moveplayerup
jmp endOfMovePlayerOne

EndOfMovePlayerOne:

mov al, [x_move] 
mov [x1_column], al 
mov al, [y_move] 
mov [y1_row], al 
mov al, [col_move]
mov [p1_col], al

popa
ret
Endp movePlayerOne

proc movePlayerTwo 
pusha 

mov al, [x2_column]
mov [x_move], al
mov al, [y2_row]
mov [y_move], al
mov al, [p2_col]
mov [col_move], al

cmp [p2_dir], 'e'
je movePTwoRight

cmp [p2_dir], 'w'
je movePTwoLeft

cmp [p2_dir], 's'
je movePTwoDown

cmp [p2_dir], 'n'
je movePTwoUp

movePTwoRight:
call movePlayerRight
jmp endOfMovePlayerTwo

movePTwoLeft:
call moveplayerleft
jmp endOfMovePlayerTwo

movePTwoDown:
call moveplayerdown
jmp endOfMovePlayerTwo

movePTwoUp:
call moveplayerup
jmp endOfMovePlayerTwo

EndOfMovePlayerTwo:

mov al, [x_move] 
mov [x2_column], al 
mov al, [y_move] 
mov [y2_row], al 
mov al, [col_move]
mov [p2_col], al

popa
ret
Endp movePlayerTwo

start:
    mov ax, @data
    mov ds, ax	

;initializing the screen and printing the menu 
call getrandonNum;calling as soon as psb because this function needs user input
;between calls to run properly 

startOfCode: 

call graphicmode
mov dx, offset menu
call printstr

;a loop which ends when p or esc are received by the user
;p starts the game 
;esc end the code
WaitForCharacter: 
inc [numLoopsWaitForCharacter]
call waitforinput

cmp al, 27
je TheEnd

cmp al, 'p'
je explainGame 

cmp [numLoopsWaitForCharacter],1
je printMessage 

jmp WaitForCharacter

printMessage:
;printing a message incase p or esc werent placed 
call newline
mov dx, offset otherButton 
call printstr
jmp waitForCharacter

explainGame:
call textmode

mov dx, offset explanation
call printstr

call waitforinput
cmp al, 27
je startOfCode


startGame:
;initializing the board and variables before the player can move
mov [delayTimeHighWord],2
mov [xsymbol], 0
mov [ysymbol], 0
mov [symbol], '0'

mov [plus_x], 20
mov [plus_y], 8

mov [moveloopcounter], 0

mov [y1_row] , 13
mov [x1_column], 38
mov [colorplayerone], 1
mov [p1_dir], 'w'

mov [y2_row], 13 
mov [x2_column],2 
mov [colorplayertwo], 2
mov [p2_dir], 'e'

;reseting screen for game 
call graphicmode
call createframe


mov al, [x1_column]
mov ah, [y1_row]
mov [x], al
mov [y], ah 
call cursor_location

mov al, [p1_col]
mov [color], al
call drawplayer

mov al, [x2_column]
mov ah, [y2_row]
mov [x], al
mov [y], ah 

call cursor_location

mov al, [p2_col]
mov [color], al

call DRAWPLAYER

jmp Move


Move: 
cmp [numloopsinvert], 0
je unInvertMovementJmp
dec [numloopsinvert]

afterDecInvertCounter: 
cmp [moveloopcounter], 6
je startSpawnPlus 
beforeCheckInputMove: 

;checking if the user has sent any input 
mov ah, 1h
int 16h

jz movePlayers

mov ah, 0
int 16h

;Checks which key player One pressed if he pressed
cmp ah, 4dh
je RightKeyOne

cmp ah, 4bh 
je LeftKeyOne

cmp ah, 50h 
je DownKeyOne

cmp ah,48h
je UpKeyOne


;Checks which key player Two pressed if he pressed
cmp al, 'd'
je RightKeyTwo

cmp al, 'a' 
je LeftKeyTwo

cmp al, 's' 
je DownKeyTwo

cmp al, 'w'
je UpKeyTwo

movePlayers: 

mov [p1_or_p2_plus], 1
call movePlayerOne

mov [p1_or_p2_plus], 2
call movePlayerTwo

call delay

inc [moveloopcounter]
;end of loop 
jmp move 

;Changing player one dir
RightKeyOne:
cmp [p1_dir], 'w'
je movePlayers 
cmp [shouldinvert], 1
je invertOneRight 
mov [p1_dir], 'e'
jmp endRightKeyOne
invertOneRight: 
mov [p1_dir], 'w'
endRightKeyOne:
jmp movePlayers 

; LeftKeyOne:
; cmp [p1_dir], 'e' 
; je movePlayers
; mov [p1_dir], 'w'
; jmp movePlayers 
LeftKeyOne:
cmp [p1_dir], 'e'
je movePlayers 
cmp [shouldinvert], 1
je invertOneLeft 
mov [p1_dir], 'w'
jmp endLeftKeyOne
invertOneLeft: 
mov [p1_dir], 'e'
endLeftKeyOne:
jmp movePlayers 

; DownKeyOne:
; cmp [p1_dir], 'n'
; je movePlayers
; mov [p1_dir], 's'
; jmp movePlayers 
DownKeyOne:
cmp [p1_dir], 'n'
je movePlayers 
cmp [shouldinvert], 1
je invertOneDown 
mov [p1_dir], 's'
jmp endDownKeyOne
invertOneDown: 
mov [p1_dir], 'n'
endDownKeyOne:
jmp movePlayers 

; UpKeyOne:
; cmp [p1_dir], 's'
; je movePlayers
; mov [p1_dir], 'n'
; jmp movePlayers
UpKeyOne:
cmp [p1_dir], 's'
je movePlayers 
cmp [shouldinvert], 1
je invertOneUp 
mov [p1_dir], 'n'
jmp endUpKeyOne
invertOneUp: 
mov [p1_dir], 's'
endUpKeyOne:
jmp movePlayers 



;Changing player two dir
RightKeyTwo:
cmp [p2_dir], 'w'
je movePlayers 
cmp [shouldinvert], 1
je invertTwoRight 
mov [p2_dir], 'e'
jmp endRightKeyTwo
invertTwoRight: 
mov [p2_dir], 'w'
endRightKeyTwo:
jmp movePlayers 

; LeftKeyTwo:
; cmp [p2_dir], 'e' 
; je movePlayers
; mov [p2_dir], 'w'
; jmp movePlayers 
LeftKeyTwo:
cmp [p2_dir], 'e'
je movePlayers 
cmp [shouldinvert], 1
je invertTwoLeft 
mov [p2_dir], 'w'
jmp endLeftKeyTwo
invertTwoLeft: 
mov [p2_dir], 'e'
endLeftKeyTwo:
jmp movePlayers 

; DownKeyTwo:
; cmp [p2_dir], 'n'
; je movePlayers
; mov [p2_dir], 's'
; jmp movePlayers 
DownKeyTwo:
cmp [p2_dir], 'n'
je movePlayers 
cmp [shouldinvert], 1
je invertTwoDown 
mov [p2_dir], 's'
jmp endDownKeyTwo
invertTwoDown: 
mov [p2_dir], 'n'
endDownKeyTwo:
jmp movePlayers 

; UpKeyTwo:
; cmp [p2_dir], 's'
; je movePlayers
; mov [p2_dir], 'n'
; jmp movePlayers
UpKeyTwo:
cmp [p2_dir], 's'
je movePlayers 
cmp [shouldinvert], 1
je invertTwoUp 
mov [p2_dir], 'n'
jmp endUpKeyTwo
invertTwoUp: 
mov [p2_dir], 's'
endUpKeyTwo:
jmp movePlayers 

; RightKeyTwo:
; cmp [p2_dir], 'w'
; je movePlayers
; mov [p2_dir], 'e'
; jmp movePlayers 

; LeftKeyTwo:
; cmp [p2_dir], 'e'
; je movePlayers
; mov [p2_dir], 'w'
; jmp movePlayers 

; DownKeyTwo:
; cmp [p2_dir], 'n'
; je movePlayers
; mov [p2_dir], 's'
; jmp movePlayers 

; UpKeyTwo:
; cmp [p2_dir], 's'
; je movePlayers
; mov [p2_dir], 'n'
; jmp movePlayers

unInvertMovementJmp: 
mov [shouldinvert], 0
jmp afterDecInvertCounter 


startSpawnPlus:
mov al, [randomnum]
add [plus_y], al
call makePlus

call getrandonNum
mov al, [randomnum]
mov ah, 0

mov bl, 4
div bl

cmp ah, 0
je firstQuarter

cmp ah, 1
je secondQuarter

cmp ah, 2
je thirdQuarter

cmp ah, 3 
je fourthQuarter

firstQuarter:
mov [@_x], 7 
mov [@_y], 5 
jmp coordOfSpawnSet 

secondQuarter:
mov [@_x], 32 
mov [@_y], 5 
jmp coordOfSpawnSet 

thirdQuarter:
mov [@_x], 32 
mov [@_y], 19 
jmp coordOfSpawnSet  

fourthQuarter:
mov [@_x], 7 
mov [@_y], 19 
jmp coordOfSpawnSet  
coordOfSpawnSet :

jmp beforeCheckInputMove

AplayerLost:

cmp [p1_or_p2_plus], 1
je p1lost
jmp p2Lost

p1Lost:
call textmode
inc [p2_wins]
mov dx, offset p1LostString 
call printstr


jmp EndGame

p2Lost:
call textmode
inc [p1_wins]
mov dx, offset p2LostString 
call printstr
jmp EndGame

;asks if user wants to play again 
;behaves accordingly 
EndGame:

;print match ended string and tells the user which key to play again/quit
;printing the score 
mov dx, offset scoreP1 
call printstr
mov dx, 0
mov dl, [p1_wins]
add dl, '0'
call printchar
mov dx, offset scoreP2
call printstr
mov dx, 0
mov dl, [p2_wins]
add dl, '0'
call printchar
mov dx, offset endGameStr
call printstr
call newline
mov dx, offset playagain
call printstr

waitingForValidInput: 

call waitforinput
cmp al, 'y'
je startgame
cmp al, 27
je theEnd
jmp waitingForValidInput 

;returns to textmode and ends code
TheEnd:
call textmode

exit:
    mov ax, 4c00h
    int 21h
END start