from schema import cricketplayer, footballplayer, invalid
import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query  # Your GraphQL root query from mapping.py

# Define GraphQL schema with additional types
schema = graphene.Schema(query=query, types=[footballplayer, cricketplayer, invalid])

# Create FastAPI app
app = FastAPI()

# Mount the GraphQL route with GraphiQL UI
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())
app.add_route("/graphql", graphql_app)

# Optional: print schema for debugging
print(schema)
