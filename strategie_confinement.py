
import pandas as pd


def strat(df: pd.DataFrame, jour: int) -> pd.DataFrame:
    """
    Applique une stratégie de confinement sur un réseau de villes pour limiter la propagation d'une épidémie.

    Args:
        df (pd.DataFrame): DataFrame contenant les informations sur les villes. Colonnes requises :
            - 'ville' : nom de la ville
            - 'population' : population totale
            - 'infectes_jour' : nombre actuel d'infectés
            - 'voisins' : liste des villes connectées (voies de propagation possibles)
        jour (int): Numéro du jour de la simulation (commence à 0). Utilisé pour appliquer les règles temporelles.

    Returns:
        pd.DataFrame: DataFrame modifié où certaines villes peuvent être isolées :
            - Les villes isolées ont leur colonne 'voisins' modifiée pour simuler le confinement.
            - Les autres villes conservent leurs voisins initiaux.
            - Les autres colonnes ne bougent pas

    Notes:
        - Max 2 villes peuvent être isolées par jour.
        - Les connexions essentielles ('Ville_0', 'Ville_1', 'Ville_4') ne peuvent jamais être coupées.

    """
    return df