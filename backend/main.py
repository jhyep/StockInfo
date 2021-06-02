from flask import *
import elasticsearch
import stockcrawler
import datetime

app = Flask(__name__.split('.')[0])
es=elasticsearch.Elasticsearch()

@app.route('/getStockInfo')
def getStockInfo():
    stockId=int(request.args.get('id',-1))
    if stockId==-1:
        abort(404)


    try:
        stockInfo = es.get('stock-info',stockId)['_source']
        if stockInfo['date']<datetime.date.today().isoformat():
            stockInfo = stockcrawler.getstockInfo(stockId)
            es.index('stock-info',stockInfo,id=stockId)
        print('here')
    except elasticsearch.exceptions.NotFoundError:
        stockInfo = stockcrawler.getStockInfo(stockId)
        stockInfo['date'] = datetime.date.today().isoformat()
        es.index('stock-info',stockInfo,id=stockId)
        print('here2')
        
    return stockInfo


app.run("127.0.0.1",5000)
