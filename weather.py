import requests 
from tkinter import *
from datetime import datetime

def atualizar():
    cidade = city_get.get()
    now = datetime.now()

    link = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=0abf54ab224c4770e156b145c58b9bea".format(cidade)

    
    page = requests.get(link)
    informacao = dict(page.json())
    print(informacao)

    try:
        atual = informacao['main']['temp'] - 273.15
        maximo = informacao['main']['temp_max'] - 273.15
        minimo = informacao['main']['temp_min'] - 273.15
        clima = informacao['weather'][0]['main']
        atual = str("%.2f" %atual)
        maximo = str("%.0f" %maximo)
        minimo = str("%.0f" %minimo)   
        horas = now.hour     
        print(atual, maximo, minimo, clima, horas)
        resultado["text"] = str("º" + atual)
        resultado["font"] = "Montserrat 20"
        maxmin["text"] = ("º"+minimo+"/º"+maximo)
        resultado1["text"] = cidade
        resultado1["font"] = "Montserrat 10"
        
        if clima == "Clear":
            if horas > 6 and horas < 18:            
                foto["image"] = sol
            else:
                foto["image"] = lua 
        elif clima == "Clouds":
            foto["image"] = nuvem
        elif (clima == "Rain" or "Misc" or "Drizzle" or "Thunderstorm"):
            foto["image"] = chuva
        elif clima == "Snow":
            foto["image"] = neve
        else:
            foto["image"] = erro

    except Exception:
        resultado1["text"] = "Cidade não localizada.\nTente sem acentos."
        resultado1["font"] = "Montserrat 8"
        foto["image"] = erro
    
janela = Tk()

nuvem = PhotoImage(file=r"pict\nuvem.png")
sol = PhotoImage(file=r"pict\sol.png")
lua = PhotoImage(file=r"pict\lua.png")
chuva = PhotoImage(file=r"pict\chuva.png")
neve = PhotoImage(file=r"pict\neve.png")
erro = PhotoImage(file=r"pict\erro.png")

foto = Label(image=erro,bg="white")
foto.grid(row=0,column=0)

resultado = Label(janela, text = "Atualize", font="Montserrat 10",bg="white")
resultado.grid(row=0,column=1)

maxmin = Label(janela, text = "", font="Montserrat 8",bg="white")
maxmin.grid(row=1,column=1)

resultado1 = Label(janela, text = "Digite sua cidade:", font="Montserrat 10", bg="white")
resultado1.grid(row=3, column=0)

city_get = Entry(janela)
city_get.grid(row=4, column=0)

botao = Button(janela, width = 12, text = "Atualizar",font="Montserrat 10", command = atualizar)
botao.grid(row=5, column=0)

janela.title("Clima")
janela.iconbitmap(r"pict\icon.ico")
janela.configure(bg="white")
janela.geometry("220x200")
janela.mainloop()


