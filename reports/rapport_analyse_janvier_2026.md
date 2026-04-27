# 📊 Rapport d'Analyse Commerciale — Janvier 2026

**Périmètre** : Ventes du mois de janvier 2026
**Source** : Pipeline ETL PostgreSQL → Python
**Date de génération** : Automatisée à chaque exécution du pipeline

---

## 🎯 Synthèse Exécutive

L'analyse des ventes de janvier 2026 couvre **2 501 transactions** réparties sur **6 produits**, **5 régions** et **7 jours de la semaine**. Le pipeline révèle des disparités significatives de rentabilité tant au niveau produit que géographique, avec des opportunités d'optimisation identifiées et actionnables immédiatement.

---

## 📦 Analyse par Produit

### 🔺 Produit Phare — Laptop

Le Laptop s'impose comme le **moteur de rentabilité** du catalogue avec :

- **Profit** : 131 298 €
- **Marge** : 34%
- **Volume** : 501 unités vendues

Malgré un volume de ventes comparable aux autres références, le Laptop génère le profit le plus élevé du portefeuille. Sa marge de 34% témoigne d'un positionnement tarifaire optimal et d'une structure de coût maîtrisée. Ce produit doit être **prioritaire dans les actions commerciales** — toute augmentation de volume aura un impact direct et significatif sur la rentabilité globale.

---

### 🔻 Produit Déficitaire — Clavier

Le Clavier représente le **signal d'alarme** de ce mois avec :

- **Profit** : -26 752 €
- **Marge** : -12%
- **Volume** : 299 unités vendues

C'est le seul produit déficitaire du catalogue. Son coût unitaire **dépasse son prix de vente**, ce qui signifie que chaque unité vendue génère une perte nette. Ce n'est pas un problème de volume — c'est une **anomalie tarifaire structurelle** qui nécessite une action corrective immédiate : révision du prix de vente, renégociation des coûts d'achat, ou retrait temporaire du catalogue.

> ⚠️ **Action recommandée** : Suspendre les promotions sur le Clavier et engager une révision tarifaire en urgence.

---

### 📊 Vue d'ensemble des produits

| Produit | Marge | Profit | Statut |
|---|---|---|---|
| Laptop | 34% | 131 298 € | ✅ Excellent |
| Casque | 29% | 100 915 € | ✅ Bon |
| Smartphone | 26% | 72 665 € | ✅ Bon |
| Souris | 11% | 39 903 € | ⚠️ Faible |
| Tablette | 12% | 38 534 € | ⚠️ Faible |
| Clavier | -12% | -26 752 € | 🔴 Déficitaire |

---

## 🗺️ Analyse par Région

### 🔺 Régions Performantes — Dakar & Kaolack

**Dakar** et **Kaolack** dominent la rentabilité régionale :

- **Dakar** : Marge 34%, Profit 137 600 € — meilleure marge du réseau
- **Kaolack** : Marge 27%, Profit 117 368 €

Ces deux régions concentrent **71% du profit total** malgré un volume de ventes comparable aux autres régions. Leur efficacité commerciale suggère des pratiques de vente ou un mix produit plus favorable qu'ailleurs.

---

### 📍 Région Sous-performante — Thiès

Thiès représente le **point de vigilance géographique** avec :

- **Profit** : 5 761 €
- **Marge** : 2%
- **Volume** : 441 ventes

Thiès affiche la marge la plus faible du réseau malgré un volume de ventes honorable (441 transactions). L'écart entre le volume et la rentabilité suggère soit une **sur-représentation de produits à faible marge** dans les ventes locales, soit des **remises commerciales excessives** accordées sur ce marché.

> ⚠️ **Action recommandée** : Analyser le mix produit vendu à Thiès et auditer la politique de remises locale.

---

### 📊 Vue d'ensemble des régions

| Région | Marge | Profit | Ventes |
|---|---|---|---|
| Dakar | 34% | 137 600 € | 545 |
| Kaolack | 27% | 117 368 € | 499 |
| Saint-Louis | 19% | 60 208 € | 418 |
| Ziguinchor | 8% | 35 626 € | 598 |
| Thiès | 2% | 5 761 € | 441 |

---

## 📅 Analyse par Jour de la Semaine

### 🔺 Jour le Plus Rentable — Mercredi

Le Mercredi s'impose comme le **meilleur jour commercial** :

- **Profit** : 123 248 €
- **Marge** : 34%
- **Quantité** : 431 unités

Le Mercredi concentre à lui seul une part disproportionnée de la rentabilité hebdomadaire. Ce pic suggère une dynamique d'achat particulière en milieu de semaine — potentiellement liée à des habitudes d'achat B2B ou à des actions promotionnelles ciblées.

---

### 📅 Jour Peu Rentable — Dimanche

Le Dimanche représente le **creux de rentabilité** avec :

- **Profit** : 2 680 €
- **Marge** : 1%
- **Quantité** : 375 unités

Malgré 375 ventes — un volume non négligeable — le Dimanche génère une rentabilité quasi nulle. Ce paradoxe volume/marge pointe vers des **remises importantes accordées en fin de semaine** pour écouler les stocks, ou une concentration des ventes sur les produits à faible marge comme le Clavier.

> ⚠️ **Action recommandée** : Revoir la politique tarifaire du dimanche et analyser le mix produit vendu ce jour.

---

### 📊 Vue d'ensemble des jours

| Jour | Marge | Profit | Quantité |
|---|---|---|---|
| Mercredi | 34% | 123 248 € | 431 |
| Samedi | 27% | 71 448 € | 299 |
| Vendredi | 17% | 41 507 € | 307 |
| Jeudi | 13% | 42 618 € | 478 |
| Mardi | 14% | 45 139 € | 435 |
| Lundi | 19% | 29 923 € | 176 |
| Dimanche | 1% | 2 680 € | 375 |

---

## 🎯 Recommandations Prioritaires

### Action immédiate
- **Clavier** → Révision tarifaire urgente ou retrait temporaire du catalogue
- **Thiès** → Audit de la politique de remises et du mix produit local
- **Dimanche** → Revoir la politique tarifaire de fin de semaine

### Action à moyen terme
- **Laptop** → Renforcer la visibilité et les actions commerciales sur ce produit
- **Dakar/Kaolack** → Identifier et répliquer les bonnes pratiques dans les autres régions
- **Mercredi** → Capitaliser sur ce pic en renforçant les stocks et la disponibilité

---

## ⚠️ Limites de l'Analyse

- Données limitées à **janvier 2026** — les tendances saisonnières ne peuvent pas être confirmées sur un seul mois
- L'analyse ne tient pas compte des **coûts fixes** (logistique, salaires) — la rentabilité réelle peut différer
- Les volumes restent **relativement faibles** — les conclusions doivent être confirmées sur plusieurs mois

---

*Rapport généré automatiquement par le pipeline ETL — Ventes Janvier 2026*
*Auteur : Mahmoud At-Tidiane | Data Analyst & Engineer*
