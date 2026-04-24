serial.redirect(SerialPin.P1, SerialPin.P0, 115200)

def on_data_received():
    msg = serial.read_until(serial.delimiters(Delimiters.NEW_LINE)).trim()
    
    if len(msg) == 0:
        return

    if msg.includes("PX:"):
        x = int(msg.char_at(3))
        y = int(msg.char_at(5))
        v = int(msg.char_at(7))
        if v == 1:
            led.plot(x, y)
        else:
            led.unplot(x, y)
            
    elif msg == "CLR":
        basic.clear_screen()
        
    elif msg.includes("DISP:"):
        basic.show_string(msg.replace("DISP:", ""))
        
    elif msg.includes("MSG:"):
        basic.show_string(msg.replace("MSG:", ""))
        
    elif msg == "INC":
        basic.show_icon(IconNames.YES)

serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

last_a = False
last_b = False

def on_forever():
    global last_a, last_b
    curr_a = input.button_is_pressed(Button.A)
    if curr_a != last_a:
        serial.write_line("BTN_A_DN" if curr_a else "BTN_A_UP")
        last_a = curr_a
    
    curr_b = input.button_is_pressed(Button.B)
    if curr_b != last_b:
        serial.write_line("BTN_B_DN" if curr_b else "BTN_B_UP")
        last_b = curr_b
    
    basic.pause(50)

basic.forever(on_forever)