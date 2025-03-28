import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Sample data
data = [
    {"name": "Roni", "city": "Cologne", "country": "India","number":982882},
    {"name": "John", "city": "London", "country": "UK"},
    {"name": "Maria", "city": "Sydney", "country": "Australia"}
]



# GraphQL Type for Student
class Student(graphene.ObjectType):
    name = graphene.String()
    city = graphene.String()
    country = graphene.String()
    number = graphene.Int()
    name = graphene.String()
# Root Query
class Query(graphene.ObjectType):
    students = graphene.List(Student)
    
    def resolve_students(self, info):
        return data

# Create FastAPI app
app = FastAPI()

# Create schema and GraphQL app with GraphiQL UI enabled
schema = graphene.Schema(query=Query)
app.add_route("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))

print(schema)