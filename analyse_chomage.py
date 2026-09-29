"""Import du dataset chômage Maroc (HCP) et génération des graphiques.

Usage : python src/analyse_chomage.py
Sortie : figures/chomage_maroc.png + indicateurs affichés en console.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
annuel = pd.read_csv(ROOT / "data" / "chomage_annuel_ENE.csv")
details = pd.read_csv(ROOT / "data" / "chomage_2025_details.csv")
emo = pd.read_csv(ROOT / "data" / "emo2026_nouvelle_serie.csv")

# --- Indicateurs calculés ---
debut, fin = annuel.iloc[0], annuel.iloc[-1]
print(f"Taux national {int(debut.annee)} -> {int(fin.annee)} : "
      f"{debut.taux_national}% -> {fin.taux_national}% "
      f"(+{fin.taux_national - debut.taux_national:.1f} pt)")
print(f"Chômeurs {int(debut.annee)} -> {int(fin.annee)} : "
      f"{debut.chomeurs_milliers:.0f}k -> {fin.chomeurs_milliers:.0f}k "
      f"(+{(fin.chomeurs_milliers / debut.chomeurs_milliers - 1) * 100:.0f}%)")
annuel["var_pt"] = annuel["taux_national"].diff()
print("\nVariations annuelles (points) :")
print(annuel[["annee", "taux_national", "var_pt"]].to_string(index=False))
print("\nÉcart urbain/rural 2025 :",
      round(fin.taux_urbain / fin.taux_rural, 1), "x")
print("\nDétails 2025 :")
print(details[["indicateur", "valeur_2024", "valeur_2025", "unite"]].to_string(index=False))

# --- Graphique ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

ax1.plot(annuel.annee, annuel.taux_national, "o-", lw=2.5, color="#c0392b", label="National")
ax1.plot(annuel.annee, annuel.taux_urbain, "s--", color="#2c3e50", label="Urbain")
ax1.plot(annuel.annee, annuel.taux_rural, "^--", color="#27ae60", label="Rural")
for x, y in zip(annuel.annee, annuel.taux_national):
    ax1.annotate(f"{y}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)
ax1.axvspan(2019.6, 2020.4, color="grey", alpha=0.15)
ax1.text(2020, 1.5, "Covid +\nsécheresse", ha="center", fontsize=8)
ax1.set_title("Taux de chômage au Maroc (%), ENE-HCP")
ax1.set_xlabel("Année")
ax1.set_ylabel("%")
ax1.set_ylim(0, 20)
ax1.legend()
ax1.grid(alpha=0.3)

ax2.bar(annuel.annee, annuel.chomeurs_milliers, color="#e67e22")
for x, y in zip(annuel.annee, annuel.chomeurs_milliers):
    ax2.text(x, y + 20, f"{y:,.0f}".replace(",", " "), ha="center", fontsize=9)
ax2.set_title("Nombre de chômeurs (milliers)")
ax2.set_xlabel("Année")
ax2.set_ylim(0, 1900)
ax2.grid(axis="y", alpha=0.3)

fig.text(0.5, 0.005,
         f"Rupture de série en 2026 (EMO) : chômage strict {emo.taux_chomage_strict.iloc[-1]}% au T2 2026, "
         "non comparable aux données ENE ci-dessus. Source : HCP (voir data/SOURCES.md)",
         ha="center", fontsize=8, style="italic")
plt.tight_layout(rect=(0, 0.03, 1, 1))
out = ROOT / "figures" / "chomage_maroc.png"
out.parent.mkdir(exist_ok=True)
plt.savefig(out, dpi=150)
print(f"\nGraphique enregistré : {out}")
