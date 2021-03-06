
from utils import sc
from utils import get_ejex_ejey
from utils import graph_js
from utils import write_html
from utils import graph_js_apilda, write_js_tarea

class Segundo_archivo:


    data_normal = sc.textFile("sales.csv", 14, True).map(lambda line: line.split(",")).collect()[1:]
    data = sc.parallelize(data_normal)

    def first_query(self):

        get_rows = self.data.map(lambda row: (row[0], float(row[13])))
        total = get_rows.reduceByKey(lambda x, y: x + y)
        print("primera consulta archivo 2")
        #print(get_rows.collect())
        print(total.collect())

        xxx = get_ejex_ejey(total)
        print(str(xxx[0]))
        print(str(xxx[1]))

        graph_js("archivo2_reporte1", str(xxx[0]), str(xxx[1]), 'pie','labels','values')
        write_html("archivo2_reporte1", "Ingresos de todas las regiones")


    def second_query(self):
        #use la orden
        get_rows = self.data.map(lambda row: (row[1], row[5].split("/")[2], int(row[8]))) \
            .filter(lambda row: row[0].lower() == 'guatemala')

        total = get_rows.map(lambda row: (row[1]+"x", row[2])).reduceByKey(lambda x, y: x+y)

        orden = total.sortBy(lambda row: row[1], ascending = False)

        #ventas_anio = get_rows.filter(lambda row: row[1]=="2019")
        #GUATEMLA
        print("segunda consulta archivo 2")
        #print(get_rows.collect())
        #print(total.collect())
        print(orden.collect())

        xxx = get_ejex_ejey(orden)
        print(str(xxx[0]))
        print(str(xxx[1]))

        graph_js("archivo2_reporte2", str(xxx[0]), str(xxx[1]), 'bar')
        write_html("archivo2_reporte2", "Año con mas unidades venididas")


    def third_query(self):

        get_rows = self.data.map(lambda row: (row[5].split("/")[2], row[0], float(row[13]), row[3]))
        year2010 = get_rows.filter(lambda row: row[0]=="2010" and row[3].lower() == "online")

        total = year2010.map(lambda row: (row[1], row[2])).reduceByKey(lambda x, y: x + y)
        total_ordenado = total.sortBy(lambda row: row[1], ascending=False)

        print("tercera consulta archivo 2")
        #print(get_rows.collect())
        #print(year2010.collect())
        #print(total.collect())
        print(total_ordenado.collect())

        xxx = get_ejex_ejey(total_ordenado)
        print(str(xxx[0]))
        print(str(xxx[1]))

        graph_js("archivo2_reporte3", str(xxx[0]), str(xxx[1]), 'bar')
        write_html("archivo2_reporte3", "Año 2010 ventas online x region")



    def homewort_query(self):
        get_rows = self.data.map(lambda row: (row[2], float(row[11]), float(row[12]), float(row[13])))

        filter = get_rows.filter(lambda x: (x[0].lower()=='baby food') or \
                                           (x[0].lower() == 'cereal') or \
                                           (x[0].lower() == 'fruits') or \
                                           (x[0].lower() == 'meat') or \
                                           (x[0].lower() == 'vegetables') or \
                                           (x[0].lower() == 'beverages') or \
                                           (x[0].lower() == 'snacks') )

        renueve = filter.map(lambda x: (x[0], x[1])).reduceByKey(lambda x, y: x + y)
        costo = filter.map(lambda x: (x[0], x[2])).reduceByKey(lambda x, y: x + y)
        profit = filter.map(lambda x: (x[0], x[3])).reduceByKey(lambda x, y: x + y)

        xxx = get_ejex_ejey(renueve)
        print(str(xxx[0]))
        print(str(xxx[1]))

        strring = graph_js_apilda('renueve',str(xxx[0]), str(xxx[1]),'bar','x','y','1')

        xxx = get_ejex_ejey(costo)
        print(str(xxx[0]))
        print(str(xxx[1]))

        strring += graph_js_apilda('costo',str(xxx[0]), str(xxx[1]),'bar','x','y','2')

        xxx = get_ejex_ejey(profit)
        print(str(xxx[0]))
        print(str(xxx[1]))

        strring += graph_js_apilda('profit',str(xxx[0]), str(xxx[1]),'bar','x','y','3')

        write_js_tarea('tarea_reporte', strring)
        write_html("tarea_reporte", "Tarea")





