# Pourquoi le taux de chômage augmente-t-il « sans cesse » au Maroc ?

*Question 3 du sujet. Données : HCP (voir `data/SOURCES.md`). Script : `src/analyse_chomage.py`. Graphique : `figures/chomage_maroc.png`.*

## 1. Corriger la prémisse : une hausse par paliers, pas « sans cesse »

Les données de l'Enquête nationale sur l'emploi (ENE) montrent une hausse de niveau, mais avec des reculs :

| Année | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Taux national (%) | 9,2 | 11,9 | 12,3 | 11,8 | 13,0 | 13,3 | 13,0 |
| Variation (pt) | – | +2,7 | +0,4 | -0,5 | +1,2 | +0,3 | -0,3 |
| Chômeurs (milliers) | 1 107 | 1 429 | 1 508 | 1 442 | 1 580 | 1 638 | 1 621 |

- Entre 2019 et 2025, le taux gagne **3,8 points** et le nombre de chômeurs progresse de **46 %** (+514 000).
- Le taux baisse en 2022 et en 2025 : la formule « augmente sans cesse » est inexacte. Il vaut mieux parler d'un **décrochage à un niveau élevé (12-13 %)** après les chocs de 2020 et 2023, dont le pays ne sort pas.

![Graphique](figures/chomage_maroc.png)

## 2. Les causes, chiffres à l'appui

**a) Chocs successifs Covid + sécheresse.** En 2020, l'économie perd 432 000 emplois, dont 273 000 dans l'agriculture, et le chômage bondit de 322 000 personnes (9,2 % → 11,9 %). L'agriculture représente ainsi environ 63 % des emplois perdus cette année-là (273 000 sur 432 000).

**b) Dépendance de l'emploi à la pluie.** L'agriculture, la forêt et la pêche emploient encore 29,3 % des actifs occupés en 2022. Le secteur perd 215 000 postes en 2022, puis 137 000 en 2024 ; en 2023, l'économie détruit 157 000 emplois au total. Quand la campagne agricole est mauvaise, le chômage rural monte (5,2 % → 6,3 % en 2023) et l'exode alimente le chômage urbain.

**c) Une création d'emplois qui ne suit pas la population active.** En 2024, 82 000 emplois sont créés (+162 000 en ville, -80 000 à la campagne), alors que le nombre de chômeurs augmente de 58 000. La création nette masque aussi une recomposition : en 2024, l'emploi rémunéré progresse de 177 000 tandis que l'emploi non rémunéré recule de 95 000.

**d) Inadéquation entre formation et emplois disponibles.** En 2025, le chômage atteint **19,1 % chez les diplômés** contre **4,7 % chez les non-diplômés**. En 2024, les taux les plus hauts touchent les diplômés de qualification professionnelle (23,9 %) et du secondaire qualifiant (24,6 %). Le marché crée des emplois peu qualifiés (services, agriculture) alors que l'offre de diplômés grandit.

**e) Un chômage de jeunes, de femmes et de longue durée.**
- Jeunes 15-24 ans : **37,2 %** en 2025 (+0,5 pt), seule tranche d'âge en hausse ; 25-34 ans : 20,9 %.
- Femmes : **20,5 %** (+1,1 pt) contre 10,8 % pour les hommes.
- **52,9 %** des chômeurs n'ont jamais travaillé ; **64,8 %** le sont depuis un an ou plus ; durée moyenne **33 mois** (31 en 2024).
- Ce sont des profils d'entrée bloquée sur le marché, plus difficiles à résorber qu'un chômage conjoncturel.

**f) Un taux qui sous-estime le problème.** Le taux d'activité est faible et baisse : 44,3 % (2022) → 43,6 % (2023) → 43,5 % (2024). Des personnes sortent de la population active (découragement), ce qui limite artificiellement le taux de chômage. Le sous-emploi lié au temps de travail passe de 10,1 % à 10,9 % en 2025 (617 000 personnes). Autre signe : les femmes ont un taux d'emploi de seulement 15,4 % contre 61,1 % pour les hommes (T2 2026).

**g) Fortes disparités territoriales.** Le chômage urbain (16,4 % en 2025) est **2,5 fois** le chômage rural (6,6 %). En 2024, Casablanca-Settat (15 %) et Fès-Meknès (14,4 %) dépassent la moyenne nationale (13,3 %), tandis que Marrakech-Safi est à 8,9 %.

## 3. Attention : la rupture statistique de 2026

En 2026, le HCP remplace l'ENE par l'Enquête sur la main-d'œuvre (EMO), alignée sur les normes internationales. Le **chômage strict** tombe à 10,8 % (T1) puis **9,5 % (T2 2026)**, avec 1,121 million de chômeurs, et la sous-utilisation composite de la main-d'œuvre est de 22,5 % puis 18,9 %. Le HCP indique lui-même qu'une comparaison directe avec l'ENE est inappropriée : la définition du chômage est plus restrictive (les personnes qui ne cherchent pas activement en sont exclues). Cette baisse ne prouve donc pas, à elle seule, une amélioration du marché du travail. Le HCP a publié une rétropolation provisoire 2017-2025 (version définitive annoncée début 2027) pour rétablir la continuité des séries. Les jeunes restent à 27,2 % de chômage strict au T2 2026 et les diplômés avancés à 16,7 %.

## 4. Conclusion

Le chômage ne monte pas « sans cesse » : il a fait un saut en 2020 puis s'est installé autour de 12-13 %. Les causes principales sont, par ordre d'importance apparente dans les données :
1. la vulnérabilité de l'emploi rural aux sécheresses (-273 000, -215 000, -137 000 postes agricoles selon les années) ;
2. une croissance qui crée trop peu d'emplois qualifiés pour des diplômés de plus en plus nombreux (19,1 %) ;
3. l'exclusion structurelle des jeunes (37,2 %) et des femmes (20,5 %), avec des durées de chômage de près de 3 ans ;
4. une population active qui se rétrécit (taux d'activité de 43,5 %), qui masque une part du problème.

## 5. Limites

- Les chiffres ont été relevés sur des pages HCP et des articles de presse reprenant les notes du HCP, non téléchargés depuis les bases brutes (pas de réseau dans l'environnement de travail). À vérifier sur https://www.hcp.ma avant rendu.
- Les séries ENE (2019-2025) et EMO (2026) ne sont pas comparables.
- Le lien entre sécheresse et chômage est établi par la concordance des chiffres, pas par une estimation économétrique.
