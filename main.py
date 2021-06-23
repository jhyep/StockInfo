from flask import *
import elasticsearch
import infocrawl
import datetime

app = Flask(__name__.split('.')[0])
es=elasticsearch.Elasticsearch()

@app.route('/getStockInfo')
def getStockInfo():
    stockId=request.args.get('id',-1)
    if stockId==-1:
        abort(404)

    try:
        stockInfo = es.get('stock-info',stockId)['_source']
        if stockInfo['date']<datetime.date.today().isoformat():
            stockInfo = infocrawl.getstockInfo(stockId)
            es.index('stock-info',stockInfo,id=stockId)
    except elasticsearch.exceptions.NotFoundError:
        stockInfo = infocrawl.getStockInfo(stockId)
        stockInfo['date'] = datetime.date.today().isoformat()
        es.index('stock-info',stockInfo,id=stockId)
        
    return str(stockInfo)


app.run("127.0.0.1",5000)
