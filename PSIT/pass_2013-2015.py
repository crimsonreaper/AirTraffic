"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
def all_data():
    """Return list from fetch data csv"""

    import csv
    import pygal as pg
    main_data = csv.reader(open('airtrafficstats.csv', newline=''))
    main_data = [row for row in main_data]

    pass_ = []
    for i in main_data:
        if i[1] == "Passenger":
            pass_.append(i)

    arrive_2013 = 0
    depar_2013 = 0
    arrive_2014 = 0
    depar_2014 = 0
    arrive_2015 = 0
    depar_2015 = 0
    for i in pass_:
        if i[3] == "2013":
            arrive_2013 += int(i[5])
            depar_2013 += int(i[6])
        elif i[3] == "2014":
            arrive_2014 += int(i[5])
            depar_2014 += int(i[6])
        elif i[3] == "2015":
            arrive_2015 += int(i[5])
            depar_2015 += int(i[6])

    graph = pg.Bar()
    graph.title = 'Passenger 2013 - 2015'
    graph.x_labels = ['2013', '2014', '2015']
    graph.add('Arrive | From', [arrive_2013, arrive_2014, arrive_2015])
    graph.add('Deperture | To', [depar_2013, depar_2014, depar_2015])
    graph.render_to_file('pass_2013-2015.svg')

    print([arrive_2013, arrive_2014, arrive_2015])
    print([depar_2013, depar_2014, depar_2015])
all_data()
