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
def create_graph(data):
    G = nx.DiGraph()

    # Add Users and Posts as Nodes
    for user in data:
        G.add_node(user["username"], type="user", **user)

        # Add user's posts
        for post in user["posts_authored"]:
            G.add_node(post["post_id"], type="post", num_comments=post["num_comments"], num_views=post["num_views"])
            # Link user to their post
            G.add_edge(user["username"], post["post_id"], connection="authorship")

            # Add views
            for viewer in post["views"]:
                # Link viewer to post
                G.add_edge(viewer, post["post_id"], connection="view")

    # Add Connections Between Users
    for user in data:
        for connection in user["connections"]:
            # Link users
            G.add_edge(user["username"], connection["username"], connection=connection["type"]) 

    return G

# Make the Graph
G = create_graph(users)

# Define colors for different connection types
edge_colors = []
for _, _, attrs in G.edges(data=True):
    if attrs["connection"] == "authorship":
        edge_colors.append("blue")  # Authorship edges in blue
    elif attrs["connection"] == "view":
        edge_colors.append("green")  # View edges in green
    elif attrs["connection"] == "follow":
        edge_colors.append("orange")  # Follow edges in orange

# Iterate through nodes and calculate importance for posts and assigns size
for node, attrs in G.nodes(data=True):
    if attrs.get("type") == "post":  
        attrs["importance_score"] = attrs["num_comments"] * 0.75 + attrs["num_views"] * 0.5
        
# Scale importance for visualization
sizes = [
    G.nodes[node].get("importance_score", 10) * 10  
    for node in G.nodes
]

# Visualization of Graph
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=sizes,
    node_color="lightblue",
    font_weight="bold",
    edge_color=edge_colors,
    width=2  
)

plt.title("Social Media Graph Highlighting Important Posts")
plt.show()
