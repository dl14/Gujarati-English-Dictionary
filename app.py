from flask import Flask, render_template, request

import glexi

app = Flask(__name__)
print("IN APP.PY")
@app.route('/mainpage', methods=['POST', 'GET'])
def hello_world():
    searchword = request.form.get('searchword')
    print("calling glexi")
    def_arr = glexi.scrape_definition(searchword)
    print("called glexi")
    return render_template('main.html', searchword=searchword, def_arr=def_arr)

if __name__ == "__main__":
    app.run()
