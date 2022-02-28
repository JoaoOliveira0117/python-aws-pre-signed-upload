from flask_restx import Api
from app.config import blueprint

from .src.controller.helloworld_controller import api as helloworld_ctlr

api = Api(
    blueprint,
    title="PRE-SIGNED URL FILE UPLOAD API",
    version="1.0",
    description="a application created for studying purposes"
)

api.add_namespace(helloworld_ctlr, path="/")