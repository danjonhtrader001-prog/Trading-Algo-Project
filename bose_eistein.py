import numpy as np
import matplotlib.pyplot as plt

# Paramètres
num_entreprises = 10
capital_total = 10000

# Attractivité (fitness) arbitraire croissante
attractivites = np.linspace(1, 2, num_entreprises)  # ex: de 1 à 2

# Energie = -log(attractivité), plus attractif = énergie plus basse
energies = -np.log(attractivites)

# Température arbitraire (contrôle de la condensation)
T = 0.1

# Potentiel chimique mu approche énergie minimale (pour condensation BE)
mu = np.min(energies) - 1e-5

# Distribution de Bose-Einstein pour chaque entreprise
def bose_einstein(energies, mu, T):
    return 1.0 / (np.exp((energies - mu) / T) - 1)

populations = bose_einstein(energies, mu, T)

# Normalisation pour totaliser capital_total
parts_capital = populations / np.sum(populations) * capital_total

# Pour l'affichage, arrondi à l'entier
parts_capital = np.round(parts_capital).astype(int)

noms_entreprises = [f"Entreprise {i+1}" for i in range(num_entreprises)]

# Tracé du diagramme en barres
plt.figure(figsize=(10,6))
plt.bar(noms_entreprises, parts_capital, color='skyblue')
plt.xlabel("Entreprise")
plt.ylabel("Capital attribué")
plt.title("Condensation de Bose-Einstein : Répartition du capital entre entreprises")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('allocation_bose_einstein.png', bbox_inches='tight')
print("Le graphique a été sauvegardé dans le dossier !")
plt.savefig('bose_einstein.png')
