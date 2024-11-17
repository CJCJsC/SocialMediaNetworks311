import networkx as nx  # For graph representation
import matplotlib.pyplot as plt  # For visualization

# Adding a user dataset
users = [
    {
        "username": "AliceS",
        "real_name": "Alice Smith",
        "age": 30,
        "gender": "female",
        "connections": [
            {"username": "user1", "type": "follow"},
            {"username": "BobDaBuilder", "type": "follow"}
        ],
        "posts_authored": [
            {
                "post_id": "post1a",
                "content": "Check out my latest project!",
                "num_comments": 150,
                "num_views": 1500,
                "views": ["BobDaBuilder", "user1"]
            },
            {
                "post_id": "post1b",
                "content": "Loving this new book I'm reading!",
                "num_comments": 15,
                "num_views": 125,
                "views": ["BobDaBuilder"]
            }
        ],
    },
    {
        "username": "BobDaBuilder",
        "real_name": "Bob Johnson",
        "age": 25,
        "gender": "male",
        "connections": [{"username": "AliceS", "type": "follow"}],
        "posts_authored": [
            {
                "post_id": "post2a",
                "content": "Excited for this new opportunity!",
                "num_comments": 500,
                "num_views": 2500,
                "views": ["user1", "AliceS"]
            }
        ],
    }
]

# Create a Graph from the Dataset
  # Add Users and Posts as Nodes
  # Add Connections Between Users

# Make the Graph

# Define colors for different connection types

# Iterate through nodes and calculate importance for posts and assigns size

# Visualization of Graph
