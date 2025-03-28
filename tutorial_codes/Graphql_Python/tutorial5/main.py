from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from mapping import query  # Import your query ObjectType from mapping.py

app = FastAPI()

# Define the schema using the imported query
schema = graphene.Schema(query=query)

# Create GraphQLApp with GraphiQL UI enabled
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Add GraphQL route
app.add_route("/graphql", graphql_app)

# Print schema (optional for debugging)
print(schema)
