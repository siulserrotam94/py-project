import matplotlib.pyplot as plt
#as plt es un alias

#creando una funcion o metodo
def generate_pie_chart():
    labels=['A','B','C']
    values =[200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #plit.show()#para detener el programa
    plt.savefig('pie.png')#grabar la imagen en un archivo con determinado nombre
    plt.close()#cerrar