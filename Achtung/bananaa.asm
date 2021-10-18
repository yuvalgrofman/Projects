IDEAL
MODEL small
jumps
p186
STACK 1000h
DATASEG

; --------------------------
; Your variables here
mea dw 100
black dw 0
color  dw 4
bcolor dw 0
x0	dw	160
y0	dw	100
x	dw	160
y	dw	100
counter dw 50
top dw 200
xtop dw 100
times0 dw 10
timess dw 10
youx dw 100
youy dw 5
borgirx dw 0
borgiry dw 200
borgirx2 dw 0
borgiry2 dw 200
borgirx3 dw 0
borgiry3 dw 200
borgircolor dw 0
borgircolor2 dw 0
borgircolor3 dw 0
borgirscaught dw 0
lastd db 'w'
ycolor dw 1
ycolor2 dw 0
randomnum dw 0
loo1p dw 2
delayTimeHighWord db 2
delayTimeLowWord dw 4240h
good db 13,10,' you caught more than 10 borgirs ',13,10,'$'
bad db 13,10,' you caught less than 10 borgirs ',13,10,'$'

intro db 13,10,' Welcome to BorgirTown! ',13,10
		db 13,10,'press p to start ',13,10,'$'
mesg_done db 13,10,'you lost,press q to quit ',13,10,'$'


newLine db 13,10,'$'
; --------------------------

CODESEG

proc aPixel 

push ax 
push bx 
push cx 
push dx


	mov bh,0h 
	mov cx, [x]
	mov dx, [y] 
	mov ax, [color]
	mov ah,0ch 
	int 10h 

pop dx
pop cx
pop bx
pop ax

ret 
endp aPixel 
proc aPixelb 

push ax 
push bx 
push cx 
push dx


	mov bh,0h 
	mov cx, [youx]
	mov dx, [youy] 
	mov ax, [ycolor]
	mov ah,0ch 
	int 10h 

pop dx
pop cx
pop bx
pop ax

ret 
endp aPixelb
proc random
    pusha 
    MOV AH, 00h  ; interrupts to get system time
    INT 1AH      ; CX:DX now hold number of clock ticks since midnight

    mov  ax, dx
    xor  dx, dx
    mov  cx, 10
    div  cx       ; here dx contains the remainder of the division - from 0 to 9
	mov dh,0
    mov [randomnum], dx
	add [randomnum],1
    popa
    ret
endp random

proc newborgir
push ax 
push bx 
push cx 
push dx
mov [borgiry],0
call random
mov ax,[randomnum]
mov bx, 10
mul bx
mov [borgirx],ax
call random
mov ax,[randomnum]
mov [borgircolor],ax
mov ax,[borgirx]
mov [x],ax
mov ax,[borgiry]
mov [y],ax
add [borgircolor2],1
mov ax,[borgircolor]
mov [color],ax

mov cx,10

paintb0:
    call aPixel
    add [x], 1
    loop paintb0
pop dx
pop cx
pop bx
pop ax
ret
endp newborgir

proc newborgir2
push ax 
push bx 
push cx 
push dx
mov [borgiry2],0
call random
mov ax,[randomnum]
mov bx, 20
mul bx
mov [borgirx2],ax
call random
mov ax,[randomnum]
mov [borgircolor2],ax
mov ax,[borgirx2]
mov [x],ax
mov ax,[borgiry2]
mov [y],ax
add [borgircolor2],2
mov ax,[borgircolor2]
mov [color],ax

mov cx,10

paintb12:
    call aPixel
    add [x], 1
    loop paintb12
pop dx
pop cx
pop bx
pop ax
ret
endp newborgir2

proc newborgir3
 push ax 
push bx 
push cx 
push dx

mov [borgiry3],0
call random
mov ax,[randomnum]
mov bx, 30 
mul bx
mov [borgirx3],ax
call random
mov ax,[randomnum]
mov [borgircolor3],ax
mov ax,[borgirx3]
mov [x],ax
mov ax,[borgiry3]
mov [y],ax
add [borgircolor3],5
mov ax,[borgircolor3]
mov [color],ax

mov cx,10

paintb13:
    call aPixel
    add [x], 1
    loop paintb13
pop dx
pop cx
pop bx
pop ax
ret
endp newborgir3

proc dropborgir
  push ax 
push bx 
push cx 
push dx

paintgirs:
mov cx,10
mov [color],0
mov ax,[borgirx]
mov [x],ax
mov ax,[borgiry]
mov [y],ax
paintblack:
  call aPixel
    add [x], 1
    loop paintblack
	add [borgiry], 1
	mov ax,[borgirx]
mov [x],ax
mov ax,[borgiry]
mov [y],ax
mov ax,[borgircolor]
mov [color],ax

mov cx,10

paintb012:
    call aPixel
    add [x], 1
    loop paintb012
	
mov cx,10
mov [color],0
mov ax,[borgirx2]
mov [x],ax
mov ax,[borgiry2]
mov [y],ax
paintblack2:
  call aPixel
    add [x], 1
    loop paintblack2
	add [borgiry2], 1
	mov ax,[borgirx2]
mov [x],ax
mov ax,[borgiry2]
mov [y],ax
mov ax,[borgircolor2]
mov [color],ax

mov cx,10

paintb0123:
    call aPixel
    add [x], 1
    loop paintb0123
	
	mov cx,10
mov [color],0
mov ax,[borgirx3]
mov [x],ax
mov ax,[borgiry3]
mov [y],ax
paintblack3:
  call aPixel
    add [x], 1
    loop paintblack3
	add [borgiry3], 1
	mov ax,[borgirx3]
mov [x],ax
mov ax,[borgiry3]
mov [y],ax
mov ax,[borgircolor3]
mov [color],ax

mov cx,10

paintb01234:
    call aPixel
    add [x], 1
    loop paintb01234
	
 	pop dx
pop cx
pop bx
pop ax
ret
endp dropborgir
proc paintyou
  push ax 
push bx 
push cx 
push dx
mov cx,10
mov [youy],180
painty:
 call aPixelb
 add [youx], 1
 loop painty
 sub [youx], 10
 mov [youy],181
 mov bx,[ycolor]
 mov ax,[ycolor2]
 mov [ycolor],ax
 mov cx,10
 painty2:
 call aPixelb
 add [youx], 1
 loop painty2
 sub [youx], 10
 mov [youy],180
  mov [ycolor],bx
 	pop dx
pop cx
pop bx
pop ax
ret
endp paintyou

proc sof  

push ax 
push bx 
push cx 
push dx

	mov dx, offset mesg_done

	mov ah,9
	int 21h	 
	
	cmp [borgirscaught],10
	jl lessca
	mov dx, offset good

	mov ah,9
	int 21h 

	jmp wait1

	lessca:
	mov dx, offset bad

	mov ah,9
	int 21h 

	wait1:
	mov ah, 00h
	int 16h
	cmp al,'q'
	jne wait1

pop dx
pop cx
pop bx
pop ax
ret
endp sof
   

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
start:
	mov ax, @data
	mov ds, ax

	; Graphic mode 
	mov ax, 13h 
	int 10h 
	
	mov dx, offset intro

	mov ah,9
	int 21h 
	wait11:
	mov ah, 00h
	int 16h
	cmp al,'p'
	jne wait11
	mov ah, 0
	mov al, 2
	int 10h
	mov ax, 13h 
	int 10h 

	jmp realstart

catchburger: 
add [borgirscaught],1
mov ax,[ycolor]
mov [ycolor2],ax
mov bx,[borgircolor]
	mov [ycolor],bx
	mov [borgircolor],0
	call dropborgir

		call paintyou
	call newborgir
	jmp get_direction
    
catchburger2:
add [borgirscaught],1
mov ax,[ycolor]
mov [ycolor2],ax 
	mov bx,[borgircolor2]
	mov [ycolor],bx
	mov [borgircolor2],0
call dropborgir
		call paintyou
	call newborgir2
	jmp get_direction

catchburger3: 
add [borgirscaught],1
mov ax,[ycolor]
mov [ycolor2],ax
	mov bx,[borgircolor3]
	mov [ycolor],bx
	mov [borgircolor3],0
call dropborgir
		call paintyou
	call newborgir3
	jmp get_direction
	
	
	

	xcheck:

	mov ax,[borgirx]

    cmp ax, [youx] 
    jl borgirxIsLess 

    mov ax, [borgirx]
    sub ax, [youx]

    cmp ax, 10
    jl catchburger 
	jmp get_direction
    
borgirxisless:

    mov ax, [youx]
    sub ax, [borgirx]

    cmp ax, 10
    jl catchburger 
	jmp get_direction

    xcheck2:

	mov ax,[borgirx2]

    cmp ax, [youx] 
    jl borgirx2IsLess 

    mov ax, [borgirx2]
    sub ax, [youx]

    cmp ax, 10
    jl catchburger2 
	jmp get_direction
    
borgirx2isless:

    mov ax, [youx]
    sub ax, [borgirx2]

    cmp ax, 10
    jl catchburger2 
jmp get_direction

    xcheck3:

	mov ax,[borgirx3]

    cmp ax, [youx] 
    jl borgirx3IsLess 

    mov ax, [borgirx3]
    sub ax, [youx]

    cmp ax, 10
    jl catchburger3 
	jmp get_direction
    
borgirx3isless:

    mov ax, [youx]
    sub ax, [borgirx3]

    cmp ax, 10
    jl catchburger3
		jmp get_direction
		
	realstart:

call newborgir

call newborgir2
mov cx,10
mov [color],0
mov ax,[borgirx2]
mov [x],ax
mov ax,[borgiry2]
mov [y],ax
paintblacka:
  call aPixel
    add [x], 1
    loop paintblacka
mov [borgiry2],120

call newborgir3
mov cx,10
mov [color],0
mov ax,[borgirx3]
mov [x],ax
mov ax,[borgiry3]
mov [y],ax
paintblackb:
  call aPixel
    add [x], 1
    loop paintblackb
mov [borgiry3],60



loolp2:

;------------------------------------
get_direction:

call paintyou
call dropborgir

	cmp [borgiry],180
	je done
	cmp [borgiry2],180
	je done
	cmp [borgiry3],180
	je done


	cmp [borgiry],179
	je xcheck

	cmp [borgiry2],179
	je xcheck2
	
	
cmp [borgiry3],179
	je xcheck3

	mov ah, 1h
	int 16h
	jz moves

	mov ah, 00h
	int 16h
	

	cmp al,'d'
	jne lc
	
	mov [lastd],'d'
	lc:
	cmp al,'a'
	jne moves
	mov [lastd],'a'

moves:
call delay

left:
cmp [youx],0
je get_direction

	cmp [lastd], 'a'
    jne right
	add [youx],10
	mov bx,[ycolor]
	mov [ycolor],0
	call aPixelb
	sub [youx],1
		call aPixelb
	sub [youx],9
	add [youy],1
		add [youx],10
	call aPixelb
		sub [youx],1
			call aPixelb
	sub [youx],9
		sub [youy],1
	mov [ycolor],bx
  sub [youx], 2
call paintyou


right:
cmp [youx],300
je get_direction
	cmp [lastd], 'd'
    jne get_direction
	mov bx,[ycolor]
	mov [ycolor],0
	call aPixelb
	add [youx],1
	call aPixelb
	sub [youx],1
	add [youy],1
	call aPixelb
	add [youx],1
	call aPixelb
	sub [youy],1
	mov [ycolor],bx
	add [youx], 1
	call paintyou
	jmp loolp2
    
done:
;------------------------------------
;prints message to the black screen
	call sof 



; return to text mode
mov ah, 0
mov al, 2
int 10h
	

exit:
	
	mov ax, 4c00h
	int 21h
END start
