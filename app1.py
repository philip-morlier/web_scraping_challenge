from scraper_factory import ScraperFactory
from mongo_controller import MongoController
from flask import Flask, render_template


url0='https://space-facts.com/mars/'

mars_facts=ScraperFactory().pandas_scraper(url0)

item=MongoController().make_dictionary('mars_facts',str(mars_facts))

# service=MongoController().set_collection()

# service.insert_one(item)

app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    mars_data = item
    return render_template("index.html", dict=mars_data)


if __name__ == "__main__":
    app.run(debug=True)
