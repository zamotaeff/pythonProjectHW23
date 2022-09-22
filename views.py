from flask import Blueprint, request, jsonify, Response

from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestParams


main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return Response(response=error.messages, status=400)

    result = None
    for query in params['queries']:
        result = build_query(
                cmd=query['cmd'],
                param=query['value'],
                data=result)

    return jsonify(result)
