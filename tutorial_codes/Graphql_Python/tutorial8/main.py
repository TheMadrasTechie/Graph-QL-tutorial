import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query  # This should be a graphene.ObjectType in mapping.py

app = FastAPI()

# Define the GraphQL schema
schema = graphene.Schema(query=query)

# Create the GraphQL route with GraphiQL UI enabled
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Mount the /graphql route
app.add_route("/graphql", graphql_app)

# Optional: print the schema for debug
print(schema)
