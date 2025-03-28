import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query  # Import your query class from mapping.py

app = FastAPI()

schema = graphene.Schema(query=query)

# Enable GraphiQL interface at GET /graphql
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

app.add_route("/graphql", graphql_app)

print(schema)
 