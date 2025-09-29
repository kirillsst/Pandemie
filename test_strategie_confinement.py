import pandas as pd
import pytest
from strategie_confinement import strat

# Lecture du dataset
df = pd.read_csv("df_epidemic.csv")

# Villes indispensables
INDISPENSABLES = ['Ville_0', 'Ville_1', 'Ville_4']

# Paramètres de test
JOURS_MAX = 15
MAX_ISOLEES_PAR_JOUR = 2

@pytest.fixture
def initial_df():
    """Fournit une copie du DataFrame pour chaque test."""
    df_sim = df.copy()
    return df_sim

@pytest.fixture
def simulation(initial_df):
    """Simule l'application de la stratégie sur tous les jours."""
    df_sim = initial_df.copy()
    historique = []

    for jour in range(JOURS_MAX):
        df_sim = strat(df_sim, jour)
        villes_coupées = []
        for idx, row in df_sim.iterrows():
            original_voisins = initial_df.loc[idx, 'voisins']
            current_voisins = row['voisins']
            if not set(current_voisins).issuperset(set(original_voisins)):
                villes_coupées.append(row['ville'])
        historique.append((df_sim.copy(), villes_coupées.copy()))
    return historique

def test_max_isolees_par_jour(simulation):
    """Test que pas plus de 2 villes sont isolées par jour."""
    for jour, (_, villes_coupées) in enumerate(simulation):
        assert len(villes_coupées) <= MAX_ISOLEES_PAR_JOUR, \
            f"Jour {jour}: Plus de 2 villes isolées: {villes_coupées}"

def test_connexions_indispensables(simulation):
    """Test que les connexions indispensables ne sont pas coupées."""
    initial_df = df.copy()
    for jour, (df_jour, _) in enumerate(simulation):
        for ville in INDISPENSABLES:
            original_voisins = set(initial_df.loc[initial_df['ville']==ville, 'voisins'].values[0])
            current_voisins = set(df_jour.loc[df_jour['ville']==ville, 'voisins'].values[0])
            assert original_voisins.issubset(current_voisins), \
                f"{ville} a perdu une connexion indispensable au jour {jour}"
