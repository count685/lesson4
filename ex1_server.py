from flask import Flask, abort, request

from ex1 import get_pop_names

from settings import apikey

app = Flask(__name__)

@app.route('/names')
def pop_names_table():
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows%s' % apikey
    pop_names = get_pop_names(url)
#    for row in pop_names:
#        print(row['Cells']['Name'])
    pop_names_len = len(pop_names)
    possible_years = ['2015', '2016', '2017']
    user_year = request.args.get('year') if request.args.get('year') in possible_years else 'all'
    print(user_year)
    print(pop_names_len)
    result = '<table>'
    result += '<tr><th>Name</th><th>Number Of Persons</th><th>Year</th></tr>'
    #for row in pop_names:
    #    result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['Cells']['Name'], row['Cells']['NumberOfPersons'], row['Cells']['Year'])
    if user_year == '2017':
        for row in pop_names:
            if row['Cells']['Year'] == 2015:
                pass
            elif row['Cells']['Year'] == 2016:
                pass
            else:
                result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['Cells']['Name'], row['Cells']['NumberOfPersons'], row['Cells']['Year'])
    elif user_year == '2016':
        for row in pop_names:
            if row['Cells']['Year'] == 2015:
                pass
            elif row['Cells']['Year'] == 2017:
                pass
            else:
                result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['Cells']['Name'], row['Cells']['NumberOfPersons'], row['Cells']['Year'])
    elif user_year == '2015':
        for row in pop_names:
            if row['Cells']['Year'] == 2016:
                pass
            elif row['Cells']['Year'] == 2017:
                pass
            else:
                result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['Cells']['Name'], row['Cells']['NumberOfPersons'], row['Cells']['Year'])
    elif user_year == 'all':
        for row in pop_names:
            result += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['Cells']['Name'], row['Cells']['NumberOfPersons'], row['Cells']['Year'])
    result += '</table>'
    
    return result
if __name__ == "__main__":
    app.run(debug=True)

