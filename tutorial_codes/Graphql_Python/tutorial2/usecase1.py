import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Sample data
course_name = "Computer Science"
course_time_year = 1
sundar_city = "Tiruppur"

# Define GraphQL schema
class Course(graphene.ObjectType):
    name = graphene.String()
    duration = graphene.Int()
    city = graphene.String()
    def resolve_name(self, info):
        return course_name

    def resolve_duration(self, info):
        return course_time_year
    
    def resolve_city(self, info):
        return sundar_city

# Create FastAPI app
app = FastAPI()

# Define GraphQL schema and enable GraphiQL UI
schema = graphene.Schema(query=Course)
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())

# Add route
app.add_route("/graphql", graphql_app)

# Optional: print schema (for debugging)
print(schema)
