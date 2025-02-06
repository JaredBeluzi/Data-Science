# Fachliche Relevanz
Falls die Spalte aus fachlicher Sicht relevant ist, ist sie das wahrscheinlich auch in der Realität

# Datenqualität
- Datenmüll finden und entfernen
- Fehlwerte entfernen / ersetzen
- Ausreißer entfernen / ersetzen
- Konsistenz der Daten mit anderen Einflussfaktoren prüfen
- Verteilung der Werte prüfen

# Einfluss auf Zielvariable
- Korrelation mit Zielvariable (gut, falls hoch)
  - Pearson Korrelation für numerische Werte
  - Chi-Quadrat-Test für kategoriale Variablen
- Informationsgewinn
  - Mutual Information
  - ANOVA-Test

# Kollinearität mit anderen Einflussfaktoren
- falls starke Korrelation mit anderen Einflussfaktoren --> Redundanz und Overfitting
  - VIF (Variance Inflation Factor)
 
# Modellleistung
- Modell mit neuer Spalte trainieren und schauen ob Evaluation besser ist als zuvor
- Feature Importance direkt in einigen Modellen prüfbar (z.B. Entscheidungsbäume oder lineare Regression)
 
