# Data Analysis Case Study

Oct 26, 2026

## The case: Kaiser Permanente's Advance Alert Monitor

Kaiser Permanente Northern California used predictive analysis of patient records to warn nurses up to 12 hours before a hospitalized patient deteriorates, and a peer-reviewed study linked the program to roughly 520 fewer deaths over 3.5 years.

The program, called the Advance Alert Monitor (AAM), runs in all 21 Kaiser Permanente hospitals in Northern California. A [March 2026 Kaiser Permanente brief on AI](https://www.kpihp.org/wp-content/uploads/2026/03/4359655541_IHP-Brief-on-AI_031026_ADA-1.pdf) still presents it as a current program. Its main evidence comes from a study of 2016 to 2019 data, so the results are not new, but the system is in use today.

## Data and methods

The model scans each patient's electronic health record and produces a deterioration risk score, using illness-severity scores built from data on over 1.5 million Kaiser Permanente patients. Two of those inputs are the Comorbidity Point Score v2 and the Laboratory-Based Acute Physiology Score v2, which measure chronic and acute severity of illness ([PSNet](https://psnet.ahrq.gov/innovation/advance-alert-monitor-program-automated-early-warning-system-adults-risk-hospital)).

The analysis was then tied to a workflow:

1. Virtual quality nurses check the scores hourly, around the clock.
2. When a score passes the alert threshold, a nurse reviews the chart.
3. If the signs of deterioration are confirmed, the nurse alerts the bedside Rapid Response Team nurse, who must respond within three hours and agree a care and escalation plan with the clinical team.

To test the program, Kaiser rolled it out in stages, starting with two pilot hospitals. Researchers compared outcomes there against hospitals not yet using it. The study covered 326,816 patients and 548,838 non-ICU hospitalizations across 19 hospitals from August 2016 to February 2019, and 43,949 hospitalizations reached the alert threshold.

## Outcomes and decisions

Patients who triggered an alert in the pilot hospitals had lower 30-day mortality, with an adjusted relative risk of 0.84 (95% confidence interval 0.78 to 0.90, p<0.001). That is 3.8 percentage points lower in absolute terms, or about 3.0 deaths avoided per 1,000 eligible patients per year, and an estimated 520 deaths (95% CI 209 to 831) avoided over the 3.5-year study ([PSNet](https://psnet.ahrq.gov/innovation/advance-alert-monitor-program-automated-early-warning-system-adults-risk-hospital)).

The program also reduced ICU stays and hospital length of stay. On the strength of these results Kaiser Permanente expanded AAM from the two pilot hospitals to 19 more, for 21 in total.

One caution for your write-up: Kaiser's [program flyer](https://www.kpihp.org/wp-content/uploads/2024/02/0654_IHP_alert-monitor-_flyer_013124.pdf) says 520 deaths prevented "per year", while the study summary says 520 over the 3.5-year period, and a 2026 brief says about 500 lives a year. I used the study figure, which is the most conservative and the best documented.

## What would have been different without data analysis

This section is my reasoning from the sources, not a finding from them. Without the risk score, nurses would have had no way to single out the few patients heading for trouble among hundreds of thousands of hospital stays, and would have relied on bedside observation and standard emergency alerts. The score gives up to 12 hours of extra warning, and the hospitals that used it had a lower death rate than comparison hospitals. The staged rollout also meant Kaiser could measure the effect before committing every hospital.

The study design has limits. Comparing pilot hospitals with others is observational, not a randomized trial, so hospital differences could explain part of the gap. The alert only helps because nurses act on it, so the analysis and the workflow cannot be separated.

## Significance and conclusion

Data analysis did two jobs in this case: it turned routine health records into an early warning, and it provided the evidence that justified expanding the program. The case shows that analysis creates value when it is built into a decision process, here a nurse review and a response deadline, and when its effect is measured against a comparison group.

For a project, the case also shows a habit worth copying: report the confidence interval, name the study design, and flag where sources disagree.

## Sources

- [Advance Alert Monitor Program, AHRQ Patient Safety Network](https://psnet.ahrq.gov/innovation/advance-alert-monitor-program-automated-early-warning-system-adults-risk-hospital) (listed 2023-06-14)
- [Kaiser Permanente Institute for Health Policy, brief on AI](https://www.kpihp.org/wp-content/uploads/2026/03/4359655541_IHP-Brief-on-AI_031026_ADA-1.pdf) (March 2026)
- [Kaiser Permanente Institute for Health Policy, Advance Alert Monitor flyer](https://www.kpihp.org/wp-content/uploads/2024/02/0654_IHP_alert-monitor-_flyer_013124.pdf) (January 2024)

The underlying study is the New England Journal of Medicine paper cited by these pages. I did not open it directly, so check its figures before you submit.
