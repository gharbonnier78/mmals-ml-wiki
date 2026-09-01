#!/usr/bin/env python3
"""One-time idempotent migration for adaptive-decision notation entries.

The canonical registry remains mathematics/notation/registry.json. This script exists only to
apply a deterministic append/update without replacing pre-existing learning history. It is
safe to rerun: semantic ids are appended only when absent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "mathematics" / "notation" / "registry.json"

SOURCE_POMDP = {
    "type": "peer_reviewed_primary",
    "reference": "Kaelbling, Littman & Cassandra (1998), Planning and Acting in Partially Observable Stochastic Domains",
    "status": "catalogued",
}
SOURCE_PROJECT = {
    "type": "project_pedagogical_synthesis",
    "reference": "Diderot belief/sufficiency/adaptive-planning pathway, 2026-09-01",
    "status": "project_synthesis_not_external_authority",
}

ENTRIES = [
    {
        "id": "belief-state-notation",
        "display": "bₜ(s)",
        "latex": "b_t(s)",
        "aliases": ["belief distribution at time t"],
        "spoken": {"fr_literal": "b indice t de s", "fr_natural": "la probabilité attribuée à l'état s au temps t par le belief courant"},
        "concept": "belief state / distribution postérieure sur l'état caché",
        "category": "probabilités et décision séquentielle",
        "formal": "b_t(s)=P(s_t=s\\mid o_{\\le t},a_{<t}).",
        "plain_language": "Après tout ce qui a été observé et fait jusqu'à t, b_t(s) indique à quel point l'état caché s reste plausible.",
        "why_here": "Le POMDP remplace l'accès direct à l'état caché par une distribution de croyance mise à jour avec l'historique action-observation.",
        "example": {"statement": "b_t(\\mathrm{fault})=0.70", "explanation": "Le modèle attribue 70 % de probabilité au régime fault à l'instant t."},
        "prerequisites": ["probabilité conditionnelle", "état caché", "observation", "POMDP"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Belief-state page and adaptive-decision pathway", "contribution": "Belief externalized as an information state distinct from the hidden state and from durable memory."}],
        "connections": ["policy-notation", "predictive-state-representation", "bayesian-filtering"],
        "domains": ["POMDP", "filtrage bayésien", "contrôle", "machine learning"],
        "misconception": {"wrong": "b_t est l'état vrai du système.", "correction": "b_t est une distribution sur les états cachés compatible avec l'information disponible."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L2",
    },
    {
        "id": "policy-notation",
        "display": "π",
        "latex": "\\pi",
        "aliases": ["policy", "politique de décision"],
        "spoken": {"fr_literal": "pi", "fr_natural": "la politique ou règle de décision"},
        "concept": "politique de décision séquentielle",
        "category": "décision séquentielle",
        "formal": "Une politique déterministe peut être écrite a_t=\\pi(b_t); une politique stochastique renvoie une distribution sur les actions.",
        "plain_language": "π dit comment choisir l'action à partir de l'information courante, puis peut être réappliquée après chaque nouvelle observation.",
        "why_here": "La discussion distingue une action ponctuelle d'une règle capable de continuer à décider après mise à jour du belief.",
        "example": {"statement": "a_t=\\pi(b_t)", "explanation": "Le belief courant entre dans la politique; l'action courante en est une sortie."},
        "prerequisites": ["fonction", "action", "belief state"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Policy concept page", "contribution": "Action séparée de la politique contingente."}],
        "connections": ["belief-state-notation", "finite-horizon-value", "action-value"],
        "domains": ["reinforcement learning", "POMDP", "contrôle", "planification"],
        "misconception": {"wrong": "π est une séquence d'actions figée calculée une fois pour toutes.", "correction": "Une politique est une règle qui peut produire des actions différentes après des observations différentes."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L2",
    },
    {
        "id": "finite-horizon",
        "display": "H",
        "latex": "H",
        "aliases": ["horizon"],
        "spoken": {"fr_literal": "H", "fr_natural": "l'horizon de planification"},
        "concept": "horizon fini de décision",
        "category": "décision séquentielle",
        "formal": "H fixe le nombre d'étapes futures incluses dans la valeur ou le problème de planification considéré.",
        "plain_language": "H indique jusqu'où dans le futur le calcul accepte de regarder.",
        "why_here": "Un état peut être suffisant pour la prochaine action et insuffisant lorsqu'on inclut des conséquences ou observations plus tardives.",
        "example": {"statement": "H=2", "explanation": "La décision actuelle et une étape de continuation sont prises en compte."},
        "prerequisites": ["temps discret", "séquence", "planification"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Value and contingent-sufficiency pages", "contribution": "H rendu explicite comme variable de portée de la suffisance."}],
        "connections": ["finite-horizon-value", "action-value", "decision-regret"],
        "domains": ["POMDP", "reinforcement learning", "contrôle optimal"],
        "misconception": {"wrong": "Augmenter H améliore toujours la décision gratuitement.", "correction": "Un horizon plus long peut mieux représenter les effets retardés mais augmente le coût de calcul et la dépendance au modèle."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L1",
    },
    {
        "id": "discount-factor",
        "display": "γ",
        "latex": "\\gamma",
        "aliases": ["discount factor", "facteur d'actualisation"],
        "spoken": {"fr_literal": "gamma", "fr_natural": "le facteur qui pondère les conséquences futures"},
        "concept": "facteur d'actualisation temporelle",
        "category": "décision séquentielle",
        "formal": "Dans une somme actualisée, le terme à k étapes est pondéré par \\gamma^k, typiquement avec 0\\le\\gamma\\le1.",
        "plain_language": "γ règle combien les conséquences éloignées comptent par rapport aux conséquences immédiates.",
        "why_here": "Le toy de planification permet de faire disparaître ou apparaître la valeur d'une information retardée en modifiant le poids du futur.",
        "example": {"statement": "\\gamma=0.9", "explanation": "Une conséquence située une étape plus tard reçoit 90 % du poids nominal utilisé dans ce toy."},
        "prerequisites": ["puissance", "somme", "récompense ou coût"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Value-function page and belief/adaptive-planning lab", "contribution": "γ relié explicitement aux résultats retardés et à la frontière du mécanisme pédagogique."}],
        "connections": ["finite-horizon-value", "action-value", "finite-horizon"],
        "domains": ["reinforcement learning", "contrôle optimal", "économie dynamique"],
        "misconception": {"wrong": "γ est une probabilité de transition.", "correction": "Ici γ est un poids temporel dans l'objectif, pas le modèle de transition."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L1",
    },
    {
        "id": "finite-horizon-value",
        "display": "Vᴴπ(b)",
        "latex": "V_H^\\pi(b)",
        "aliases": ["state value", "policy value"],
        "spoken": {"fr_literal": "V indice H exposant pi de b", "fr_natural": "la valeur de la politique pi depuis le belief b sur l'horizon H"},
        "concept": "valeur attendue d'une politique sur horizon fini",
        "category": "décision séquentielle",
        "formal": "V_H^\\pi(b_t)=\\mathbb E[\\sum_{k=0}^{H-1}\\gamma^k r_{t+k}\\mid b_t,\\pi].",
        "plain_language": "V résume la qualité attendue de tout le futur induit par une politique, pas seulement le gain de la prochaine action.",
        "why_here": "La valeur multi-étapes permet d'exprimer des résultats retardés et de comparer des plans contingents.",
        "example": {"statement": "V_2^\\pi(b)=7.6", "explanation": "Sur deux étapes, cette politique obtient une valeur attendue totale de 7,6 selon le modèle et l'objectif déclarés."},
        "prerequisites": ["espérance", "politique", "horizon", "facteur d'actualisation"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Value-function and contingent-policy pages", "contribution": "V utilisé pour séparer valeur d'une politique et préférence d'une seule action immédiate."}],
        "connections": ["policy-notation", "action-value", "decision-regret"],
        "domains": ["reinforcement learning", "POMDP", "contrôle optimal"],
        "misconception": {"wrong": "V est le résultat effectivement observé d'une trajectoire unique.", "correction": "V est une espérance selon le modèle, la politique et l'incertitude déclarés."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L2",
    },
    {
        "id": "action-value",
        "display": "Qᴴπ(b,a)",
        "latex": "Q_H^\\pi(b,a)",
        "aliases": ["action value", "Q-value"],
        "spoken": {"fr_literal": "Q indice H exposant pi de b virgule a", "fr_natural": "la valeur de commencer par l'action a depuis b puis de continuer avec la politique pi"},
        "concept": "valeur attendue d'une action suivie d'une politique",
        "category": "décision séquentielle",
        "formal": "Q_H^\\pi(b_t,a_t)=\\mathbb E[r_t+\\gamma V_{H-1}^\\pi(b_{t+1})\\mid b_t,a_t].",
        "plain_language": "Q compare les conséquences d'un premier choix tout en tenant compte de ce qui pourra être fait ensuite.",
        "why_here": "Le projet distingue un vecteur de valeurs à un pas d'une vraie valeur contingente à horizon plus long.",
        "example": {"statement": "Q_2(b,\\mathrm{probe})>Q_2(b,\\mathrm{reuse})", "explanation": "Le probe peut être préféré même s'il coûte maintenant lorsque l'information améliore la continuation."},
        "prerequisites": ["valeur V", "action", "espérance", "transition de belief"],
        "encounters": [{"source_ref": "2026-09-01--kaelbling-littman-cassandra-pomdp", "context": "Value-function page and adaptive-planning lab", "contribution": "Q utilisé pour rendre visible la différence entre payoff immédiat et conséquence adaptative."}],
        "connections": ["finite-horizon-value", "policy-notation", "value-of-information"],
        "domains": ["reinforcement learning", "POMDP", "planification"],
        "misconception": {"wrong": "Q est toujours une valeur à une seule étape.", "correction": "Q peut inclure une continuation multi-étapes; sa définition dépend de l'horizon ou de l'objectif considéré."},
        "authority": {"mathematical_sources": [SOURCE_POMDP], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L2",
    },
    {
        "id": "decision-regret",
        "display": "Rᴴ(z)",
        "latex": "R_H(z)",
        "aliases": ["finite-horizon decision regret"],
        "spoken": {"fr_literal": "R indice H de z", "fr_natural": "le regret décisionnel induit par la représentation z sur l'horizon H"},
        "concept": "perte de valeur décisionnelle relative à une référence",
        "category": "évaluation de représentation",
        "formal": "R_H(z)=V_H^*(b)-V_H^{\\pi_z}(b) dans le cadre local où b est l'état d'information de référence et \\pi_z la politique induite par z.",
        "plain_language": "R mesure combien la compression z fait perdre dans le processus de décision par rapport à la référence déclarée.",
        "why_here": "Le programme veut distinguer fidélité prédictive, reconstruction d'un belief et utilité réelle pour une décision séquentielle déclarée.",
        "example": {"statement": "R_H(z)=0", "explanation": "Pour ce goal, cet horizon, ces actions et ce modèle de référence, aucune valeur n'a été perdue; cela ne prouve pas que z contient tout sur le monde."},
        "prerequisites": ["valeur V", "politique", "référence optimale", "représentation"],
        "encounters": [{"source_ref": "DIDEROT-BELIEF-SUFF-ADAPT-20260901", "context": "Decision-regret and contingent-sufficiency pages", "contribution": "Notation enregistrée comme métrique locale de suffisance décisionnelle, avec portée explicitement query-relative."}],
        "connections": ["finite-horizon-value", "contingent-sufficiency", "sufficient-state"],
        "domains": ["decision theory", "continual learning", "world-model research"],
        "misconception": {"wrong": "R_H(z)=0 implique que z reconstruit exactement l'état caché ou le belief.", "correction": "Zéro regret porte seulement sur le problème décisionnel, l'horizon et la référence déclarés."},
        "authority": {"mathematical_sources": [SOURCE_PROJECT], "pedagogical_sources": ["Diderot learning synthesis 2026-09-01"], "scientific_authority": False},
        "status": "draft",
        "maturity": "L1",
    },
]


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entries = data.setdefault("entries", [])
    existing = {entry.get("id") for entry in entries if isinstance(entry, dict)}
    added = []
    for entry in ENTRIES:
        if entry["id"] not in existing:
            entries.append(entry)
            added.append(entry["id"])
    data["updated"] = "2026-09-01"
    data["source_note"] = (
        "Canonical Diderot notation registry. Initial entries were seeded from the 2026-08-30 function/graph learning session; "
        "adaptive-decision notation was appended on 2026-09-01 under the pinned pedagogical harness with per-entry authority records."
    )
    REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Notation capitalization complete: {len(added)} added; {len(entries)} total.")


if __name__ == "__main__":
    main()
