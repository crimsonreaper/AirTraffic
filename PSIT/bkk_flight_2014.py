"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
def all_data():
    """Return list from fetch data csv"""

    import csv
    import pygal as pg
    main_data = csv.reader(open('airtrafficstats.csv', newline=''))
    main_data = [row for row in main_data]

    bkk = []
    for i in main_data:
        if i[0] == "BKK":
            bkk.append(i)

    flight_ = []
    for i in bkk:
        if i[1] == "Flight":
            flight_.append(i)

    arrive_2014 = []
    depar_2014 = []
    for i in flight_:
        if i[3] == "2014":
            arrive_2014.append(int(i[5]))
            depar_2014.append(int(i[6]))

    graph = pg.Line(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    graph.title = 'BKK Flight 2014'
    graph.x_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October', 'November', 'December']
    graph.add('Arrive | From', arrive_2014)
    graph.add('Deperture | To', depar_2014)
    graph.range = [37000, 62000]
    graph.render_to_file('bkk_flight_2014.svg')

    print(arrive_2014)
    print(depar_2014)
all_data()
