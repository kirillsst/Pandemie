import pandas as pd

INDISPENSABLES = ["Ville_0", "Ville_1", "Ville_4"]

def strat(df: pd.DataFrame, jour: int) -> pd.DataFrame:
    """
    Stratégie d'isolement simple :
    - À chaque jour, on isole jusqu'à 2 villes (maximum) ayant le plus grand nombre
      d'infectés actuellement, en évitant les villes indispensables.
    - Isoler = remplacer la liste 'voisins' par une liste vide (la ville ne peut plus infecter ses voisins).
    - Retourne une copie du DataFrame modifié.

    Entrées :
    - df : DataFrame contenant au moins les colonnes ['ville','population','infectes_jour','voisins']
    - jour : numéro du jour (int), fourni par la simulation (non utilisé pour l'instant mais utile pour extensions)

    Contraintes respectées :
    - Ne pas isoler les villes de INDISPENSABLES
    - Maximum 2 villes isolées par appel
    """

    df_out = df.copy()

    # Filtrer candidats : villes avec au moins 1 voisin et non-indispensables
    candidats_mask = df_out['voisins'].apply(lambda v: len(v) > 0) & (~df_out['ville'].isin(INDISPENSABLES))
    candidats = df_out[candidats_mask].copy()

    # Si aucun candidat -> rien à faire
    if candidats.empty:
        return df_out

    # Trier par infectés_jour décroissant, on prend les top 2
    candidats_sorted = candidats.sort_values(by='infectes_jour', ascending=False)

    # Nombre max à isoler par jour
    MAX_ISOLEES_PAR_JOUR = 2

    # Sélectionner jusqu'à MAX_ISOLEES_PAR_JOUR villes
    villes_a_isoler = list(candidats_sorted['ville'].iloc[:MAX_ISOLEES_PAR_JOUR])

    # Appliquer l'isolation : vider la liste des voisins pour ces villes
    for ville in villes_a_isoler:
        idx = df_out.index[df_out['ville'] == ville]
        if len(idx) > 0:
            df_out.at[idx[0], 'voisins'] = []

    return df_out 
