from gensim.models.doc2vec import Doc2Vec
import matplotlib.pyplot as plt
import networkx as nx
import glob


all_files = glob.glob('path/to/lemmas/*lmms')
model = Doc2Vec.load('name_of_model.model')


def get_similarity(n_files):
    for file in all_files:
        most_similar = (model.docvecs.most_similar([file], topn = n_files))
        yield  [file, most_similar]


similarity = [w for w in get_similarity(len(all_files))]

# Rewrites format for the plot
def rewrite():
    for file1, file2 in similarity:
        for f, k in file2:
            x = (file1, f, k)
            yield x


G = nx.Graph(Wiki="Textar")

for a,b,c in rewrite():
    G.add_edge(a,b, weight=c)

large = [(a, b) for (a, b, c) in G.edges(data=True) if c['weight'] >= 0.45]
medium = [(a, b) for (a, b, c) in G.edges(data=True) if 0.45 >= c['weight'] >= 0.33]
small = [(a, b) for (a, b, c) in G.edges(data=True) if 0.32 >= c['weight'] >= 0.0]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=100, node_color='#C71585')

nx.draw_networkx_edges(G, pos, edgelist=large, edge_color='#DC143C',
                       width=2)

nx.draw_networkx_edges(G, pos, edgelist=medium,
                       width=1.25, edge_color='#00008B')


nx.draw_networkx_edges(G, pos, edgelist=small,
                       width=0.75, alpha=0.5, edge_color='#87CEFA')

nx.draw_networkx_labels(G, pos, font_size=12, font_family='Monospace')
plt.show()
