import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Define GraphQL Query
class MyQuery(graphene.ObjectType):
    class Meta:
        name = "typefrommetaclass1"
        description = "description from metaclass1"

    hello = graphene.String(description="hello string")
    bye = graphene.String(description="bye string")

    def resolve_hello(self, info):
        return "hello world!!!"

    def resolve_bye(self, info):
        return "good bye!!"

# Create FastAPI app
app = FastAPI()

# Define schema
schema = graphene.Schema(query=MyQuery)

# Create GraphQLApp with GraphiQL UI enabled
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Add route
app.add_route("/graphql", graphql_app)

# Optional debug print
print(schema)
