import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query

app = FastAPI()

schema = graphene.Schema(query=query)

# Enable GraphiQL UI for GET requests
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

app.add_route("/graphql", graphql_app)

print(schema)
