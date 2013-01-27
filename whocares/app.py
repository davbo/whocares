from flask import Flask, jsonify

from whocares.region import Region

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2:///nhs')
app = Flask(__name__)


@app.route("/regions")
def list_regions():
    s = sessionmaker(engine)()
    regions = s.query(Region).all()
    response = {'regions': []}
    for region in regions:
        response['regions'].append({
            'name': region.name,
            'points': region.area.coords(s)[0]})
    return jsonify(response)

if __name__ == "__main__":
    app.run()
