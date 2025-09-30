import pandas as pd
import ast
from strategie_confinement import strat

# Lecture du dataset
df = pd.read_csv("df_epidemic.csv")
# Conversino des listes
df['voisins'] = df['voisins'].apply(ast.literal_eval)

# Paramètres de simulation
jours_max = 15
infection_rate = 0.3  # proportion de population qui peut être infectée par contact

# Initialisation
df_sim = df.copy()
voisins_init = df["voisins"]
# Stockage de l'historique
historique = []

for jour in range(jours_max):
    # Réinitialiser les voisins chaque jour
    df_sim['voisin'] = voisins_init
    # Appliquer la stratégie de confinement
    df_sim = strat(df_sim, jour)

    # Propagation de l'épidémie
    for idx, row in df_sim.iterrows():
        infectes = row['infectes_jour']
        population = row['population']
        voisins = row['voisins']
        for voisin in voisins:
            # Trouver l'index du df correspondant à ce voisin
            idx_voisin = df_sim.index[df_sim['ville'] == voisin][0]
            
            infectes_voisin = df_sim.at[idx_voisin, 'infectes_jour']
            nouveaux_infectes = int(infection_rate * infectes)
            nouveaux_infectes = min(nouveaux_infectes, df_sim.at[idx_voisin, 'population'] - infectes_voisin)
            df_sim.at[idx_voisin, 'infectes_jour'] += nouveaux_infectes

    # Sauvegarde de l'état de la journée
    historique.append(df_sim[['ville', 'infectes_jour', 'population']].copy())




# Affichage des résultats jour par jour
for jour, df_jour in enumerate(historique):
    total_infectes = df_jour['infectes_jour'].sum()
    total_population = df_jour['population'].sum()
    print(f"Jour {jour}: {total_infectes}/{total_population} infectés")

# Calcul population saine finale
df_final = historique[-1]
df_final['sains'] = df_final['population'] - df_final['infectes_jour']
population_saine_finale = df_final['sains'].sum()
total_population = df_final['population'].sum()
print(f"\nPopulation saine finale : {population_saine_finale}/{total_population} ({population_saine_finale/total_population*100:.1f}%)")

