def draw_health(canvas, health):
    round_health = round(int(health)/10)*10
    if round_health == 0:
        pass
    elif round_health >= 10:
        line = canvas.create_rectangle(0, 0, 21, 50, outline = "#FF0000", fill = "#FF0000")
        if round_health >= 20:
            line = canvas.create_rectangle(21, 0, 42, 50, outline = "#FF3300", fill = "#FF3300")
            if round_health >= 30:
                line = canvas.create_rectangle(42, 0, 63, 50, outline = "#ff6600", fill = "#ff6600")
                if round_health >= 40:
                    line = canvas.create_rectangle(63, 0, 84, 50, outline = "#ff9900", fill = "#ff9900")
                    if round_health >= 50:
                        line = canvas.create_rectangle(84, 0, 105, 50, outline = "#FFCC00", fill = "#FFCC00")
                        if round_health >= 60:
                            line = canvas.create_rectangle(105, 0, 126, 50, outline = "#FFFF00", fill = "#FFFF00")
                            if round_health >= 70:
                                line = canvas.create_rectangle(126, 0, 147, 50, outline = "#ccff00", fill = "#ccff00")
                                if round_health >= 80:
                                    line = canvas.create_rectangle(147, 0, 168, 50, outline = "#99ff00", fill = "#99ff00")
                                    if round_health >= 90:        
                                        line = canvas.create_rectangle(168, 0, 189, 50, outline = "#66ff00", fill = "#66ff00")
                                        if round_health >= 100:
                                            line = canvas.create_rectangle(189, 0, 210, 50, outline = "#33ff00", fill = "#33ff00")

    canvas.pack()