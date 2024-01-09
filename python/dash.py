import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

# Charger le fichier Excel dans un DataFrame
df = pd.read_excel('imports1.xlsx')

# Grouper les données par produit et calculer la somme des valeurs importées
total_imported_value = df.groupby('Product label')['Imported value in 2019'].sum()

# Obtenir les trois principaux produits par importation
top3_products = total_imported_value.nlargest(3)

# Tracer le top 3 des produits par importation
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = top3_products.plot(kind='bar', ax=ax, color='skyblue')

# Ajuster l'orientation des labels sur l'axe x
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=10, ha='right')

ax.set_title('Top 3 Imported Products')
ax.set_xlabel('Product')
ax.set_ylabel('Total Imported Value')

plt.tight_layout()  # Ajuster automatiquement la disposition pour éviter la coupure des labels
plt.show()


# Sauvegarder la figure comme une image
fig.savefig('top_imported_products.png')
# Move the image to the public directory
react_public_path = os.path.join(os.path.dirname(__file__), '..', 'react', 'public')
shutil.move('top_imported_products.png', os.path.join(react_public_path, 'top_imported_products.png'))
