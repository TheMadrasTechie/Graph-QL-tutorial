import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Define the Interface
class Player(graphene.Interface):
    name = graphene.String()
    country = graphene.String()

# Implement the Interface in FootballPlayer
class FootballPlayer(graphene.ObjectType):
    class Meta:
        interfaces = (Player,)

    position = graphene.String()

# Implement the Interface in CricketPlayer
class CricketPlayer(graphene.ObjectType):
    class Meta:
        interfaces = (Player,)

    battingorder = graphene.Int()

# Define the Query class
class Query(graphene.ObjectType):
    class Meta:
        name = "interfacequery"
        description = "implements field type from interface"

    fplayer = graphene.Field(FootballPlayer, description="coming from football player interface")
    cplayer = graphene.Field(CricketPlayer, description="coming from cricket player interface")

    def resolve_fplayer(self, info):
        return {"name": "player1", "country": "Spain", "position": "Central Back"}

    def resolve_cplayer(self, info):
        return {"name": "player2", "country": "India", "battingorder": 1}

# FastAPI app setup
app = FastAPI()

# Create GraphQL schema
schema = graphene.Schema(query=Query)

# GraphQL app with GraphiQL enabled
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Route
app.add_route("/graphql", graphql_app)

# Optional: print schema
print(schema)
