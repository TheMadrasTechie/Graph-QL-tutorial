from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler


class Calculator(graphene.ObjectType):
    concat = graphene.String(a=graphene.String(), b=graphene.String())
    add = graphene.String(a=graphene.Int(), b=graphene.Int())

    def resolve_concat(self, info, a, b):
        return a +" "+b

    def resolve_add(self, info, a, b):
        return a+b


app = FastAPI()

schema = graphene.Schema(query=Calculator)

# Enable GraphiQL
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Mount GraphQL at /graphql
app.add_route("/graphql", graphql_app)
