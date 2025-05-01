def __init__(self):  
    """Initialisiert das Prognose-System mit Default-Werten für diverse Parameter."""  
    self.team_a_name = ""  
    self.team_b_name = ""  
    self.results = {}  
      
def get_team_input(self, team_name: str) -> Dict:  
    """  
    Erfasst alle notwendigen Eingabewerte für ein Team.  
      
    Args:  
        team_name: Name des Teams, für das Daten erfasst werden  
          
    Returns:  
        Dictionary mit allen erfassten Teamdaten  
    """  
    print(f"\n--- Eingabedaten für {team_name} ---")  
      
    team_data = {}  
    # Basis-Teamdaten  
    team_data["elo"] = float(input(f"ELO-Rating für {team_name} (0-100): "))  
    team_data["form"] = float(input(f"Formfaktor für {team_name} (0-100): "))  
    team_data["home_advantage"] = float(input(f"Heimvorteil für {team_name} (0-20, 0 für Auswärtsteam): "))  
    team_data["structural_strength"] = float(input(f"Strukturelle Stärke für {team_name} (0-100): "))  
    team_data["seasonal_factor"] = float(input(f"Saisonaler Faktor für {team_name} (0-100): "))  
    team_data["rivalry_factor"] = float(input(f"Rivalitätsfaktor für {team_name} (0-100): "))  
      
    # Angriff und Verteidigung  
    team_data["attack"] = float(input(f"Angriffsindex für {team_name} (0.5-2.0): "))  
    team_data["defense"] = float(input(f"Verteidigungsindex für {team_name} (0.5-2.0, niedriger=besser): "))  
    team_data["mod_factor"] = float(input(f"Situationsmodifikator für {team_name} (0.7-1.3): "))  
      
    # Spieler und Trainer  
    team_data["player_analysis"] = float(input(f"Spielerzentrische Analyse für {team_name} (0-100): "))  
    team_data["key_player_impact"] = float(input(f"Key Player Impact für {team_name} (0-30): "))  
    team_data["tactical_compatibility"] = float(input(f"Taktische Kompatibilität für {team_name} (0.8-1.2): "))  
    team_data["coach_quality"] = float(input(f"Trainer-Qualität für {team_name} (0-10): "))  
    team_data["coach_experience"] = float(input(f"Trainer-Erfahrung für {team_name} (0-10): "))  
    team_data["coach_history"] = float(input(f"Historischer Trainer-Erfolg gegen Gegner (-5 bis 5): "))  
      
    # Soziale und psychologische Faktoren  
    team_data["fan_momentum"] = float(input(f"Fan-Momentum für {team_name} (-10 bis 10): "))  
    team_data["psychological_stability"] = float(input(f"Psychologische Stabilität für {team_name} (0-10): "))  
    team_data["external_stress"] = float(input(f"Externe Stressfaktoren für {team_name} (-5 bis 0): "))  
    team_data["social_cohesion"] = float(input(f"Sozialer Zusammenhalt für {team_name} (0-10): "))  
    team_data["public_pressure"] = float(input(f"Öffentlicher/medialer Druck für {team_name} (0-10): "))  
      
    # Wettmarkt und spezifische Faktoren  
    team_data["odds"] = float(input(f"Aktuelle Siegquote für {team_name} (z.B. 1.65): "))  
    team_data["weather_sensitivity"] = float(input(f"Wetterempfindlichkeit des Spielstils für {team_name} (-1 bis 1): "))  
    team_data["optimal_weather"] = float(input(f"Optimaler Wetterwert für {team_name} (0-10): "))  
      
    return team_data  
  
def get_match_input(self) -> Dict:  
    """  
    Erfasst alle spielspezifischen Eingabewerte.  
      
    Returns:  
        Dictionary mit allen spielspezifischen Daten  
    """  
    print("\n--- Spielspezifische Eingabedaten ---")  
      
    match_data = {}  
    match_data["league_coefficient"] = float(input("Ligaspezifischer Torkoeffizient (1.0-1.8): "))  
    match_data["current_weather"] = float(input("Aktueller Wetterwert (0-10): "))  
    match_data["data_quality"] = float(input("Datenverfügbarkeit und -qualität (0-1): "))  
    match_data["historical_entropy"] = float(input("Historische Entropie der Begegnungen (0-1): "))  
      
    return match_data  
  
def calculate_extended_team_strength(self, team_data: Dict) -> float:  
    """  
    Berechnet die erweiterte Teamstärke (ETS).  
      
    Args:  
        team_data: Dictionary mit Teamdaten  
          
    Returns:  
        Berechnete erweiterte Teamstärke  
    """  
    ets = (0.45 * team_data["elo"] +   
           0.20 * team_data["form"] +   
           0.15 * team_data["home_advantage"] +   
           0.10 * team_data["structural_strength"] +   
           0.05 * team_data["seasonal_factor"] +   
           0.05 * team_data["rivalry_factor"])  
      
    return ets  
  
def calculate_dynamic_expected_goals(self, attack_team: Dict, defense_team: Dict,   
                                    league_coef: float, time_phase: int) -> float:  
    """  
    Berechnet die dynamisch erwarteten Tore (DET) für eine bestimmte Spielphase.  
      
    Args:  
        attack_team: Dictionary mit Angriffsteamdaten  
        defense_team: Dictionary mit Verteidigungsteamdaten  
        league_coef: Ligaspezifischer Koeffizient  
        time_phase: Spielphase (1=Anfang, 2=Mitte, 3=Ende)  
          
    Returns:  
        Dynamisch erwartete Tore für die gegebene Phase  
    """  
    # Zeitphasen-Modifikatoren  
    phase_mods = {  
        1: {"attack": 0.9, "defense": 1.1, "league": 0.9, "momentum": 0.0},  # Anfangsphase  
        2: {"attack": 1.0, "defense": 1.0, "league": 1.0, "momentum": 0.0},  # Mittelteil  
        3: {"attack": 1.1, "defense": 0.9, "league": 1.1, "momentum": 0.0}   # Schlussphase  
    }  
      
    # Anpassung der Basiswerte je nach Spielphase  
    adjusted_attack = attack_team["attack"] * phase_mods[time_phase]["attack"]  
    adjusted_defense = defense_team["defense"] * phase_mods[time_phase]["defense"]  
    adjusted_league_coef = league_coef * phase_mods[time_phase]["league"]  
    momentum = phase_mods[time_phase]["momentum"]  
      
    # Berechnung der erwarteten Tore  
    det = (adjusted_league_coef *   
           adjusted_attack *   
           adjusted_defense *   
           attack_team["mod_factor"] *   
           (1 + momentum))  
      
    return det  
  
def calculate_social_psychological_factor(self, team_data: Dict) -> float:  
    """  
    Berechnet den sozialen und psychologischen Faktor (SPF).  
      
    Args:  
        team_data: Dictionary mit Teamdaten  
          
    Returns:  
        Berechneter sozialer und psychologischer Faktor  
    """  
    spf = (1 +   
           0.05 * team_data["fan_momentum"] +   
           0.03 * team_data["psychological_stability"] +   
           0.02 * team_data["external_stress"] +   
           0.02 * team_data["social_cohesion"] -   
           0.04 * team_data["public_pressure"])  
      
    return spf  
  
def calculate_coach_impact_factor(self, team_data: Dict) -> float:  
    """  
    Berechnet den Trainer-Einfluss-Faktor (CIF).  
      
    Args:  
        team_data: Dictionary mit Teamdaten  
          
    Returns:  
        Berechneter Trainer-Einfluss-Faktor  
    """  
    cif = (1 +   
           0.1 * (team_data["coach_quality"] - 5) +   
           0.05 * team_data["coach_experience"] +   
           0.05 * team_data["coach_history"])  
      
    return cif  
  
def calculate_wettmarkt_integration(self, team_data: Dict) -> float:  
    """  
    Berechnet den Wettmarkt-Integrationsfaktor (WMI).  
      
    Args:  
        team_data: Dictionary mit Teamdaten  
          
    Returns:  
        Berechneter Wettmarkt-Integrationsfaktor  
    """  
    reference_odds = 2.0  
    wmi = 1 + 0.06 * math.log(reference_odds / team_data["odds"])  
      
    return wmi  
  
def calculate_weather_impact_model(self, team_data: Dict, current_weather: float) -> float:  
    """  
    Berechnet den Wetter-Impact-Faktor (WIM).  
      
    Args:  
        team_data: Dictionary mit Teamdaten  
        current_weather: Aktueller Wetterwert  
          
    Returns:  
        Berechneter Wetter-Impact-Faktor  
    """  
    wim = 1 + 0.05 * team_data["weather_sensitivity"] * (current_weather - team_data["optimal_weather"])**2  
      
    return wim  
  
def calculate_dynamic_win_probability(self, team_a: Dict, team_b: Dict,   
                                     team_a_ets: float, team_b_ets: float,  
                                     det_a: float, det_b: float,  
                                     time_phase: int) -> float:  
    """  
    Berechnet die dynamische Siegwahrscheinlichkeit (DWP) für Team A.  
      
    Args:  
        team_a: Dictionary mit Daten von Team A  
        team_b: Dictionary mit Daten von Team B  
        team_a_ets: Erweiterte Teamstärke von Team A  
        team_b_ets: Erweiterte Teamstärke von Team B  
        det_a: Erwartete Tore für Team A  
        det_b: Erwartete Tore für Team B  
        time_phase: Spielphase (1=Anfang, 2=Mitte, 3=Ende)  
          
    Returns:  
        Dynamische Siegwahrscheinlichkeit für Team A  
    """  
    # Berechnung der zusätzlichen Faktoren  
    spf_a = self.calculate_social_psychological_factor(team_a)  
    spf_b = self.calculate_social_psychological_factor(team_b)  
      
    cif_a = self.calculate_coach_impact_factor(team_a)  
    cif_b = self.calculate_coach_impact_factor(team_b)  
      
    wmi_a = self.calculate_wettmarkt_integration(team_a)  
    wmi_b = self.calculate_wettmarkt_integration(team_b)  
      
    # Phase-abhängige Werte - vereinfachtes Modell  
    svm = (0.15 if time_phase == 1 else   
           0.10 if time_phase == 2 else   
           0.05)  
      
    # Berechnung des z-Wertes für die logistische Funktion  
    z = (0.15 * (team_a_ets - team_b_ets) +   
        0.20 * (det_a - det_b) +   
        0.15 * (team_a["player_analysis"] - team_b["player_analysis"]) +   
        0.10 * (team_a["key_player_impact"] - team_b["key_player_impact"]) +   
        0.10 * team_a["tactical_compatibility"] +   
        0.10 * (cif_a - cif_b) +   
        0.10 * (spf_a - spf_b) +   
        0.05 * (wmi_a - wmi_b) +   
        0.05 * svm)  
      
    # Berechnung der Siegwahrscheinlichkeit mit logistischer Funktion  
    dwp = 1 / (1 + math.exp(-z))  
      
    return dwp  
  
def calculate_expected_points(self, win_prob: float, draw_prob: float) -> float:  
    """  
    Berechnet die erwarteten Punkte (EEP).  
      
    Args:  
        win_prob: Siegwahrscheinlichkeit  
        draw_prob: Unentschieden-Wahrscheinlichkeit  
          
    Returns:  
        Erwartete Punkte  
    """  
    # Vereinfachtes Modell ohne Varianzeinfluss  
    eep = 3 * win_prob + 1 * draw_prob  
      
    return eep  
  
def calculate_precision_confidence_metric(self,   
                                         historical_entropy: float,   
                                         data_quality: float) -> float:  
    """  
    Berechnet die Präzisions- und Konfidenzmetrik (PKM).  
      
    Args:  
        historical_entropy: Historische Entropie der Begegnungen  
        data_quality: Datenverfügbarkeit und -qualität  
          
    Returns:  
        Präzisions- und Konfidenzmetrik  
    """  
    # Annahme: Varianz ist für beide Mannschaften gleich bei 0.025  
    variance = 0.025  
      
    pkm = (math.exp(-0.4 * variance) *   
          (1 - 0.3 * historical_entropy) *   
          (1 + 0.2 * data_quality))  
      
    return pkm  
  
def generate_goal_distribution(self, expected_goals: float) -> List[float]:  
    """  
    Generiert eine Poisson-Verteilung der Torwahrscheinlichkeiten.  
      
    Args:  
        expected_goals: Erwartete Tore  
          
    Returns:  
        Liste der Wahrscheinlichkeiten für 0, 1, 2, ... Tore  
    """  
    # Wir berechnen bis zu 5 Tore explizit  
    probabilities = []  
    for goals in range(6):  
        probability = (math.exp(-expected_goals) *   
                      (expected_goals ** goals) /   
                      math.factorial(goals))  
        probabilities.append(probability)  
      
    # Alle weiteren Tore zusammenfassen  
    remaining_prob = 1 - sum(probabilities)  
    probabilities.append(remaining_prob)  
      
    return probabilities  
  
def generate_score_matrix(self, team_a_goals: List[float], team_b_goals: List[float]) -> np.ndarray:  
    """  
    Generiert eine Matrix mit den Wahrscheinlichkeiten für alle möglichen Spielstände.  
      
    Args:  
        team_a_goals: Torwahrscheinlichkeiten für Team A  
        team_b_goals: Torwahrscheinlichkeiten für Team B  
          
    Returns:  
        Matrix mit Spielstand-Wahrscheinlichkeiten  
    """  
    score_matrix = np.zeros((len(team_a_goals), len(team_b_goals)))  
      
    for i in range(len(team_a_goals)):  
        for j in range(len(team_b_goals)):  
            score_matrix[i, j] = team_a_goals[i] * team_b_goals[j]  
      
    # Normierung, um sicherzustellen, dass die Summe 1 ist  
    score_matrix = score_matrix / np.sum(score_matrix)  
      
    return score_matrix  
  
def calculate_specific_scenarios(self, score_matrix: np.ndarray) -> Dict:  
    """  
    Berechnet Wahrscheinlichkeiten für spezifische Spielverläufe und Szenarien.  
      
    Args:  
        score_matrix: Matrix mit Spielstand-Wahrscheinlichkeiten  
          
    Returns:  
        Dictionary mit verschiedenen Szenario-Wahrscheinlichkeiten  
    """  
    scenarios = {}  
      
    # Sieg Team A  
    win_a = np.sum(np.triu(score_matrix, k=1))  
    scenarios["win_team_a"] = win_a  
      
    # Sieg Team B  
    win_b = np.sum(np.tril(score_matrix, k=-1))  
    scenarios["win_team_b"] = win_b  
      
    # Unentschieden  
    draw = np.sum(np.diag(score_matrix))  
    scenarios["draw"] = draw  
      
    # Clean Sheet (kein Gegentor) für Team A  
    clean_sheet_a = np.sum(score_matrix[:, 0])  
    scenarios["clean_sheet_team_a"] = clean_sheet_a  
      
    # Clean Sheet für Team B  
    clean_sheet_b = np.sum(score_matrix[0, :])  
    scenarios["clean_sheet_team_b"] = clean_sheet_b  
      
    # Beide Teams treffen  
    both_teams_score = 1 - clean_sheet_a - clean_sheet_b + score_matrix[0, 0]  
    scenarios["both_teams_score"] = both_teams_score  
      
    # Über 2.5 Tore  
    over_2_5 = 1 - np.sum(score_matrix[:3, :3]) + score_matrix[0, 2] + score_matrix[1, 1] + score_matrix[2, 0]  
    scenarios["over_2_5_goals"] = over_2_5  
      
    return scenarios  
  
def calculate_time_phased_scenarios(self) -> Dict:  
    """  
    Berechnet phasenbasierte Spielverlauf-Szenarien.  
      
    Returns:  
        Dictionary mit zeitbasierten Szenario-Wahrscheinlichkeiten  
    """  
    scenarios = {}  
      
    # Angenommene Wahrscheinlichkeiten basierend auf den bisherigen Berechnungen  
    # In einer erweiterten Version würden hier komplexere Berechnungen erfolgen  
      
    # Frühe Tore (erste 25 Minuten)  
    scenarios["early_goal_team_a"] = 0.41  
    scenarios["early_goal_team_b"] = 0.22  
      
    # Tore in der zweiten Halbzeit  
    scenarios["second_half_goal_team_a"] = 0.55  
    scenarios["second_half_goal_team_b"] = 0.38  
      
    # Karten und sonstige Ereignisse  
    scenarios["yellow_cards_over_3"] = 0.76  
    scenarios["red_card"] = 0.12  
    scenarios["penalty"] = 0.15  
      
    return scenarios  
  
def run_analysis(self) -> Dict:  
    """  
    Führt die vollständige Analyse durch und gibt alle Ergebnisse zurück.  
      
    Returns:  
        Dictionary mit allen Analyseergebnissen  
    """  
    # Team- und Spielnamen erfassen  
    self.team_a_name = input("\nName des Teams A (Heimteam): ")  
    self.team_b_name = input("Name des Teams B (Auswärtsteam): ")  
      
    # Teaminformationen sammeln  
    team_a_data = self.get_team_input(self.team_a_name)  
    team_b_data = self.get_team_input(self.team_b_name)  
    match_data = self.get_match_input()  
      
    # Grundlegende Berechnungen  
    team_a_ets = self.calculate_extended_team_strength(team_a_data)  
    team_b_ets = self.calculate_extended_team_strength(team_b_data)  
      
    # Phasenbezogene Berechnungen  
    results = {}  
    results["team_a_name"] = self.team_a_name  
    results["team_b_name"] = self.team_b_name  
    results["team_a_ets"] = team_a_ets  
    results["team_b_ets"] = team_b_ets  
      
    # Für jede Spielphase berechnen  
    phases = {1: "Anfangsphase", 2: "Mittelteil", 3: "Schlussphase"}  
    phase_results = {}  
      
    for phase in phases:  
        phase_name = phases[phase]  
        phase_data = {}  
          
        # Erwartete Tore berechnen  
        det_a = self.calculate_dynamic_expected_goals(  
            team_a_data, team_b_data, match_data["league_coefficient"], phase)  
        det_b = self.calculate_dynamic_expected_goals(  
            team_b_data, team_a_data, match_data["league_coefficient"], phase)  
          
        # Siegwahrscheinlichkeiten berechnen  
        dwp_a = self.calculate_dynamic_win_probability(  
            team_a_data, team_b_data, team_a_ets, team_b_ets, det_a, det_b, phase)  
        dwp_b = self.calculate_dynamic_win_probability(  
            team_b_data, team_a_data, team_b_ets, team_a_ets, det_b, det_a, phase)  
          
        # Unentschieden-Wahrscheinlichkeit anpassen (vereinfacht)  
        # In Realität ist diese Berechnung komplexer, um sicherzustellen, dass die Summe 1 ist  
        draw_prob = max(0, 1 - dwp_a - dwp_b)  
          
        # Bei Ungenauigkeiten normalisieren  
        sum_probs = dwp_a + dwp_b + draw_prob  
        if sum_probs != 1:  
            factor = 1 / sum_probs  
            dwp_a *= factor  
            dwp_b *= factor  
            draw_prob *= factor  
          
        # Erwartete Punkte  
        eep_a = self.calculate_expected_points(dwp_a, draw_prob)  
        eep_b = self.calculate_expected_points(dwp_b, draw_prob)  
          
        # Ergebnisse für diese Phase speichern  
        phase_data["expected_goals_team_a"] = det_a  
        phase_data["expected_goals_team_b"] = det_b  
        phase_data["win_probability_team_a"] = dwp_a  
        phase_data["win_probability_team_b"] = dwp_b  
        phase_data["draw_probability"] = draw_prob  
        phase_data["expected_points_team_a"] = eep_a  
        phase_data["expected_points_team_b"] = eep_b  
          
        phase_results[phase_name] = phase_data  
      
    results["phase_results"] = phase_results  
      
    # Finale Ergebnisse basierend auf der Schlussphase  
    final_phase = phase_results["Schlussphase"]  
      
    # Torverteilungen generieren  
    team_a_goal_dist = self.generate_goal_distribution(final_phase["expected_goals_team_a"])  
    team_b_goal_dist = self.generate_goal_distribution(final_phase["expected_goals_team_b"])  
      
    # Spielstand-Matrix erstellen  
    score_matrix = self.generate_score_matrix(team_a_goal_dist, team_b_goal_dist)
dwp_b = self.calculate_dynamic_win_probability(
                team_b_data, team_a_data, team_b_ets, team_a_ets, det_b, det_a, phase)
            draw_prob = 1 - dwp_a - dwp_b

            # Erwartete Punkte berechnen
            eep_a = self.calculate_expected_points(dwp_a, draw_prob)
            eep_b = self.calculate_expected_points(dwp_b, draw_prob)

            phase_data["expected_goals_team_a"] = det_a
            phase_data["expected_goals_team_b"] = det_b
            phase_data["win_probability_team_a"] = dwp_a
            phase_data["win_probability_team_b"] = dwp_b
            phase_data["draw_probability"] = draw_prob
            phase_data["expected_points_team_a"] = eep_a
            phase_data["expected_points_team_b"] = eep_b

            phase_results[phase_name] = phase_data

        # Torverteilung und Scorematrix
        final_det_a = phase_results["Mittelteil"]["expected_goals_team_a"]
        final_det_b = phase_results["Mittelteil"]["expected_goals_team_b"]

        team_a_goal_dist = self.generate_goal_distribution(final_det_a)
        team_b_goal_dist = self.generate_goal_distribution(final_det_b)

        score_matrix = self.generate_score_matrix(team_a_goal_dist, team_b_goal_dist)
        scenario_data = self.calculate_specific_scenarios(score_matrix)

        # Zusätzliche szenarien
        time_based_scenarios = self.calculate_time_phased_scenarios()

        # Präzisionsmetrik
        pkm = self.calculate_precision_confidence_metric(
            match_data["historical_entropy"], match_data["data_quality"]
        )

        # Ergebnisse zusammenfassen
        results["phase_results"] = phase_results
        results["score_matrix"] = score_matrix.tolist()
        results["scenario_probabilities"] = scenario_data
        results["time_based_scenarios"] = time_based_scenarios
        results["precision_confidence_metric"] = pkm

        return results


# Hauptausführung
if __name__ == "__main__":
    system = FootballPredictionSystem()
    analysis_results = system.run_analysis()

    # Übersichtlich ausgeben
    print("\n--- Analyseergebnisse ---")
    print(tabulate([
        ["Team A", analysis_results["team_a_name"]],
        ["Team B", analysis_results["team_b_name"]],
        ["Erweiterte Teamstärke A", f'{analysis_results["team_a_ets"]:.2f}'],
        ["Erweiterte Teamstärke B", f'{analysis_results["team_b_ets"]:.2f}'],
        ["Präzisions-/Konfidenzmetrik", f'{analysis_results["precision_confidence_metric"]:.3f}']
    ], headers=["Metrik", "Wert"], tablefmt="fancy_grid"))

    # Szenarien ausgeben
    print("\n--- Spielverlauf-Szenarien ---")
    for k, v in analysis_results["scenario_probabilities"].items():
        print(f"{k.replace('_', ' ').capitalize()}: {v:.2%}")

    print("\n--- Zeitbasierte Szenarien ---")
    for k, v in analysis_results["time_based_scenarios"].items():
        print(f"{k.replace('_', ' ').capitalize()}: {v:.2%}")
