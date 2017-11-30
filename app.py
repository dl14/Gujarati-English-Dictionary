from flask import Flask, render_template, request

import glexi

app = Flask(__name__)
print("IN APP.PY")
@app.route('/mainpage', methods=['POST', 'GET'])
def hello_world():
    searchword = request.form.get('searchword')
    print("calling glexi")
    def_l_arr = glexi.scrape_lexicon(searchword)
    def_s_arr = glexi.scrape_shabdakosh(searchword)
    print("called glexi")
    return render_template('main.html', searchword=searchword, def_arr=def_l_arr, def_s_arr=def_s_arr)

if __name__ == "__main__":
    app.run()
