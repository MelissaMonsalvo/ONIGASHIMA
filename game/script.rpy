


label start:
    if persistent.loop3:
        jump prologue_loop3
    if persistent.loop2:
        jump prologue_loop2
    if persistent.loop1:
        jump prologue_loop1
    else:
        jump prologue
