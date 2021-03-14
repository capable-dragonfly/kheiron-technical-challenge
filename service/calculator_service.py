import logging
from flask import Flask, request, Response
from calculation.calculation import resolve_calculation

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculate():
    notation = request.args.get('notation', 'prefix')
    calculation = request.args.get('calculation')
    if calculation is None:
        return 'No calculation specified', 400
    try:
        return str(resolve_calculation(calculation, notation=notation))
    except Exception as e:
        logger.warning(
            f'Calculation request for {calculation} failed with "{e}"'
        )
        return 'Calculation Error', 400
