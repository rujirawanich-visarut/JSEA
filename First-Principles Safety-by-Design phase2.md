# First-Principles Safety-by-Design Architecture for Chemical Processes  
## Phase 2: Dynamic Safety, Safeguard Assurance, Human Factors, and AI Decision Boundaries

## Executive synthesis and Phase 1 reconciliation

Phase 1 established a strong foundation: JSEA should reason from material and energy state, equipment topology, time, physical and chemical mechanisms, exposure pathways, safeguards, control structures, evidence, uncertainty, and lifecycle context rather than from hazard keywords alone. It also correctly rejected the idea that a linear accident “chain” should be the master representation, instead proposing a typed causal graph whose individual paths can be rendered as chains, Bowties, or other familiar views. fileciteturn0file0

The Phase 2 audit finds **no Phase 1 foundational principle that must be rejected outright**, but several concepts require important narrowing or architectural revision. Most importantly, Phase 1's process-state representation is too plant-process-centric for dynamic safety: a system can have apparently normal pressure, temperature, and level while simultaneously being unsafe because a protection function is bypassed, composition is wrong, inventory is accumulating invisibly, structural integrity is degraded, feedback is misleading, or the process has entered a trajectory from which recovery will soon become impossible. CSB's BP Texas City investigation is a canonical example: during startup, tower inventory accumulated while instrumentation gave operators misleading information, including a level transmitter indicating a falling level while the actual inventory continued to rise. citeturn1search0

Likewise, safeguards can no longer remain merely attributes attached to causal edges. Phase 2 requires each safeguard to become a **stateful object in its own right**, with dependencies, operating mode, response time, bypass state, proof-test and maintenance status, applicability limits, degradation modes, and evidence about its actual condition. HSE's process control guidance treats safety-related functions as combinations of sensing, logic, final elements, utilities, human interfaces, environmental conditions, testing, maintenance, and management arrangements; it explicitly recognizes shared elements and common-mode vulnerabilities. citeturn11search20turn4view1

A further extension is necessary for the phrase **safe operating envelope**. CCPS defines safe operating limits in relation to critical process parameters and the combination of equipment design limits and process dynamics. API RP 584 separately addresses *Integrity Operating Windows*, which are specifically an asset-integrity/process-safety management construct. Neither concept should be inflated into a universal multidimensional definition of “safe.” citeturn11search2turn11search4 Phase 2 should therefore define the JSEA Safe Operating Envelope as a **project ontology construct**: the mode-specific set of system states *and admissible trajectories* satisfying identified safety constraints, including required safeguard and control-system conditions. That definition is a researcher synthesis rather than a definition imposed by CCPS, API, IEC, or HSE.

IEC 61511 strongly supports the lifecycle and safe-state direction but also provides an important boundary. The current IEC 61511 series available in August 2026 continues to contain IEC 61511-1:2016+A1:2017 as the core requirements document; its stated purpose includes specifying, designing, installing, operating, and maintaining SIS so that the system can achieve or maintain a safe process state. IEC 61511-3 provides a framework for determining required SIL but explicitly does **not** prescribe which SIL is required for a specific application. citeturn11search0turn11search8turn11search13 This supports JSEA identifying the need for a safety function or specialist functional-safety determination, but not calculating or assigning SIL, PFD, or risk acceptance from natural-language evidence.

The central Phase 2 conclusion is therefore:

> **JSEA should represent safety dynamically as the controlled evolution of a sociotechnical process system through time, not as membership in a static box of acceptable parameter values. Physical state, trajectory, safeguard condition, topology, information quality, human-system interaction, and recovery capability must all participate in determining whether the system is safe, degraded, unsafe-but-recoverable, or beyond an identified recovery boundary.**

The underlying scientific and engineering provenance used below is distinguished with the following classification.

| Classification | Meaning in this report |
|---|---|
| **Invariant physics/chemistry** | Conservation, thermodynamic directionality, physical transport, chemical reaction and related principles. |
| **Engineering model** | An abstraction requiring assumptions, parameters, validation, and an applicability domain. |
| **Recognized practice/standard** | IEC, CCPS, API, HSE or similar established process-safety practice. |
| **Empirical evidence** | Experiments, measured properties, operating experience, or incident investigation. |
| **Regulation/governance** | Jurisdiction-specific legal or organizational requirements. |
| **Researcher inference** | Architecture proposed for JSEA by synthesizing the cited foundations rather than directly prescribed by one source. |

### Phase 1 audit

| Phase 1 conclusion | Audit disposition | Basis, applicability, limitations, and confidence |
|---|---|---|
| Safety reasoning should start from material/energy/state rather than hazard labels. | **Accepted without change.** | NIST property practice, DIERS reactive-system practice, and process-hazard methods all support state-specific reasoning. citeturn6search12turn6search8 **Type:** invariant physics + engineering practice. **Limit:** identification of a mechanism does not determine its magnitude. **Confidence: high.** |
| The master causal representation should be a typed graph; a linear chain is a view of that graph. | **Accepted without change.** | Physical escalation paths benefit from causal sequences, while STPA demonstrates that feedback, control actions, and interactions require cycles and control structures. citeturn7search3turn7search10 **Type:** systems theory + researcher architecture. **Limit:** graph semantics require validation. **Confidence: high.** |
| Material identity is insufficient; composition, concentration, phase, pressure, temperature, and inventory matter. | **Accepted without change.** | NIST REFPROP uses fluid- and mixture-specific models and explicitly documents applicability and mixture-data limitations. citeturn6search12turn6search4 **Type:** invariant physics + empirical/model evidence. **Confidence: high.** |
| Rate, duration, sequence, and accumulation are first-class safety variables. | **Accepted without change.** | Reactive relief, runaway, accumulation, alarm response, and transient process operation depend on rates and timing. citeturn6search8turn0search7 **Type:** physics + recognized practice. **Confidence: high.** |
| Equipment topology and isolation state are causal, not merely drawing metadata. | **Accepted without change.** | CSB investigations and CCPS safe-work guidance show that connection/isolation states can create or remove hazardous pathways. citeturn11search22turn5search6 **Type:** empirical evidence + recognized practice. **Confidence: high.** |
| Consequence reasoning requires a source-to-target pathway. | **Accepted without change.** | This is foundational to release, dispersion, exposure, fire, and environmental consequence reasoning. HSE consequence and layout practice similarly requires analysis of propagation and receptors. citeturn11search18turn9search13 **Type:** physics + engineering model/practice. **Confidence: high.** |
| Safeguards should attach to the causal transitions they control. | **Accepted, then strengthened.** | This remains essential, but safeguards must become first-class stateful objects rather than edge annotations. HSE explicitly considers the complete safety function, dependencies and lifecycle. citeturn4view0turn4view1 **Type:** recognized practice + researcher extension. **Confidence: high.** |
| Safeguard independence must be demonstrated rather than inferred from names. | **Accepted without change.** | CCPS LOPA material treats independence as a defining protection-layer property; HSE identifies common utilities/interfaces and common-mode failure. citeturn0search9turn4view1 **Type:** recognized practice. **Limit:** JSEA can flag dependency but should not assign numerical dependence factors. **Confidence: high.** |
| Safety constraints and control structures should augment physical causality. | **Accepted without change.** | Primary STAMP/STPA sources explicitly analyze unsafe control actions, feedback and controller process models. citeturn7search3turn7search10 **Type:** primary systems-safety framework. **Limit:** not a substitute for reaction, relief, dispersion, integrity, or exposure models. **Confidence: high.** |
| Unknown evidence must not be treated as evidence of safety. | **Accepted without change.** | This is an epistemic constraint supported by model/data applicability limitations and the consequences of stale or misleading process information. citeturn6search4turn1search0 **Type:** epistemic principle + empirical evidence. **Confidence: high.** |
| Startup, shutdown, maintenance, cleaning, abnormal and other transient states require distinct analysis when configuration changes. | **Accepted without change.** | HSE and CCPS explicitly identify nonroutine modes as requiring mode-specific procedures and hazard consideration. citeturn0search7turn3search3 **Type:** recognized practice. **Confidence: high.** |
| ISD comparison must be multidimensional rather than collapsed to one safety score. | **Accepted without change.** | The four inherent-safety lenses affect different hazards and can transfer risk. IEC also places inherently safer processes before reliance on protective systems where practicable. citeturn11search12 **Type:** recognized practice + researcher decision architecture. **Confidence: high.** |
| JSEA can assist but cannot approve engineering or work. | **Accepted without change and elevated to a system constraint.** | Functional safety, mechanical integrity, relief, consequence modelling and legal authorization all require lifecycle evidence and competent interpretation that a language model cannot infer from narrative alone. citeturn11search0turn11search8turn11search19 **Type:** recognized practice + governance inference. **Confidence: high.** |
| “Process state” contains composition, inventory, T/P, phase, equipment/control state and mode. | **Requires architectural revision.** | A single object is too coarse because process variables can be normal while protection, integrity, feedback, or human readiness is degraded. Replace it with a parent **System Safety State** containing process, equipment, safeguard, control, human/organizational, environmental, and evidence-state components. **Type:** researcher inference supported by HSE control-system practice and CSB incidents. citeturn11search20turn1search0 **Confidence: high.** |
| “Unsafe state” is principally a process state threatening/violating a safety constraint. | **Requires clarification.** | The definition must include unsafe configurations and degraded safety functions even before a process variable crosses a conventional operating limit. A bypassed interlock can be safety-significant while pressure/temperature remain nominal. citeturn5search0turn5search10 **Confidence: high.** |
| Barrier information can be stored on transitions. | **Revised.** | Preserve the edge relationship but model the barrier itself independently, because its own state, dependencies, testing and degradation evolve with time. citeturn4view0turn5search5 **Confidence: high.** |
| High/moderate/low confidence can characterize assertions. | **Narrowed.** | Retain qualitative confidence only as a description of evidential support, accompanied by rationale; never convert it into event probability, reliability, residual risk, or acceptance. NIST similarly emphasizes context-specific evidence and evaluation rather than a single generic trust metric. citeturn8search5turn8search16 **Confidence: high.** |
| A causal pathway normally progresses through unsafe state → loss of control/containment → propagation. | **Clarified, not rejected.** | These objects remain useful but none is universally mandatory. Unsafe control actions can precede an abnormal physical state, physical harm can occur without loss of containment, and loss of containment can itself be the initial detected state. STPA reinforces the need for non-linear control paths. citeturn7search10turn7search3 **Confidence: high.** |

**Missing concepts required for Phase 2** are therefore: system safety state; safe, degraded, recoverable and irreversible state classes; mode-specific envelopes; trajectories and derivatives; latent/hidden state; safeguard operational state and safeguard evidence state; recovery path; time-to-harm and time-to-loss-of-recoverability; observability; action feasibility and feedback; human performance-shaping conditions; lifecycle assurance status; evidence conflict; calculation/test/review requirements; decision hold points; and explicit authorization authority.

There are also several important **framework disagreements that JSEA should preserve rather than erase**. CCPS “safe operating limits” are parameter limits informed by design and process dynamics, while API RP 584's IOW construct addresses integrity-related limits; neither is identical to the broader system-level Safe Operating Envelope proposed here. citeturn11search2turn11search4 IEC 61511's “safe state” concerns the state a safety function achieves or maintains, but that does not imply a universal shutdown configuration or an unpowered condition. citeturn11search0 STPA's “hazard” is a system condition related to losses and constraints, while process-safety usage frequently also calls intrinsic properties or inventories “hazards”; Phase 1's separation of **hazard source**, **unsafe/system hazard state**, and **loss** should therefore be retained. citeturn7search3turn7search10 Finally, a HAZOP safeguard is not automatically a LOPA IPL, and a procedure or alarm cannot be transformed into IPL credit simply by being present in the scenario narrative. citeturn0search9turn0search19

No architecture change in Phase 2 alters the Phase 1 principles of physical causality, edge-specific safeguards, explicit uncertainty, or human approval authority. The principal changes are additions of **dynamic state semantics**, **stateful safeguards**, and a **formal decision-boundary layer**.

## Dynamic safety model and Safe Operating Envelope

The central Phase 2 abstraction should be a **System Safety State at time \(t\)**:

```text
SystemSafetyState(t) = {
    ProcessState,
    MaterialAndEnergyState,
    EquipmentAndIntegrityState,
    TopologyAndIsolationState,
    SafeguardState,
    ControlAndAutomationState,
    HumanAndOrganizationalReadiness,
    EnvironmentAndTargetState,
    OperatingMode,
    EvidenceState
}
```

This is a conceptual ontology, not a numerical process simulator.

It deliberately separates **the physical system's actual state** from **what JSEA knows about that state**. A valve may actually be closed while its position is unverified; a trip may actually be available while the only evidence is an outdated maintenance record. JSEA must not collapse ontology state and epistemic state.

### Dynamic safety vocabulary

| Concept | Phase 2 definition | Relationship and evidence | Applicability and limitations | Classification / confidence |
|---|---|---|---|---|
| **Safe state** | A system state in which identified safety constraints relevant to the current mode are satisfied and credible hazardous trajectories are adequately controlled. | Requires hazard/constraint definition, process and equipment status, and where relevant continued protective capability. IEC 61511 requires SIS to achieve or maintain a safe state but does not prescribe one universal process state. citeturn11search0 | Safe state is process-, hazard- and mode-specific. It may require cooling, inerting, circulation, pressure control or other continuing functions rather than simply “power off.” | **Recognized practice + researcher formalization. High confidence.** |
| **Stable/passive safe state** | A safe state that does not depend on continuing active control for the hazard under consideration over the specified period. | Requires engineering evidence that removal of active control cannot recreate the identified mechanism. | Not every process can achieve such a state; “passive” must be hazard-specific. | **Researcher inference. Moderate-high.** |
| **Unsafe state** | A physical, configurational, control or protection state in which an identified system safety constraint is violated or a hazardous mechanism has become active. | Can involve abnormal process variables, wrong composition/topology, degraded integrity, unsafe automation state, or loss of a required safety function. | Does not necessarily mean that harm is inevitable. | **STPA-informed systems concept + process-safety synthesis. High.** citeturn7search3turn11search20 |
| **Degraded safety state** | State in which immediate process conditions may remain acceptable, but required safety margin, observability, redundancy, integrity or safeguard capability has been reduced. | Requires explicit degradation mechanism and relation to one or more safety constraints. CCPS's bypass guidance recognizes that temporary instrumentation impairment can remove or weaken prevention/mitigation capability. citeturn5search0turn5search10 | “Degraded” is not synonymous with “unsafe to operate”; the competent site decision depends on the hazard and approved compensating arrangements. | **Recognized practice + researcher state class. High.** |
| **Normal operating envelope** | Region of conditions intended for routine process operation. | Site operating basis and procedures. | Normal does not automatically mean safe under wrong composition, hidden inventory, impaired integrity or safeguards. | **Contextual engineering information. High.** |
| **Safe operating limits** | Limits established for critical process variables from equipment design limits and process dynamics. | CCPS definition. citeturn11search2 | Parameter limits alone do not characterize all dynamic/system hazards. | **Recognized practice. High.** |
| **Safe Operating Envelope** | JSEA construct: the mode-specific set of states and trajectories satisfying applicable safety constraints, including required material, topology, integrity, safeguard and control conditions. | Derived from approved limits, design data, process dynamics, hazard analysis, integrity requirements and protective requirements. | Not an existing universal CCPS/API/IEC definition and must not be presented as such. | **Researcher synthesis. High confidence in architectural usefulness; moderate in exact formalism pending validation.** |
| **Design envelope** | Conditions and load/configuration combinations for which the relevant process/equipment design basis has been established. | Design documents, specifications, codes, material data and calculations. | Being inside a mechanical design envelope does not prove the process is safely operable; design pressure, for example, is not a complete process-safety criterion. | **Engineering model/contextual engineering. High.** |
| **Integrity Operating Window** | API-specific construct for operating boundaries related to asset degradation/integrity management. | API RP 584. citeturn11search4 | Important input to the broader JSEA envelope but not equivalent to it. | **Recognized API practice. High.** |
| **Operating limit** | Site-approved operational boundary used to direct operation. | Procedures/control strategy/design basis. | May include quality or performance limits that are not safety limits. CCPS distinguishes design-related safe upper/lower limits from quality-related limits. citeturn11search9 | **Contextual engineering/governance. High.** |
| **Safety limit** | Boundary tied to an identified hazard, equipment design constraint, safety function, or other approved safety basis. | Requires competent engineering definition and evidence. | JSEA may retrieve or compare an existing limit but shall not invent one. | **Engineering/governance. High.** |
| **Trajectory** | Ordered evolution of system state over time, including direction, rate, sequence, duration and accumulated quantities. | Historian/process data or a validated dynamic model when quantitative prediction is necessary. | A language model can reason qualitatively about direction; exact trajectories generally require calculation/simulation. | **Physics + engineering model. High.** |
| **Hidden/latent state** | Safety-relevant condition not represented adequately by currently observed process variables. | Composition, unseen inventory, internal damage, blocked flow, stale instrument indication, inhibited protection, etc. | Absence from the control-room display is not evidence of absence. | **Researcher ontology; empirical support high.** citeturn1search0turn11search19 |
| **Recoverability** | Existence of at least one feasible, evidence-supported path from the current state to an approved safe state before an irreversible transition or harm occurs. | Requires available control actions, safeguards, utilities, time, equipment capability, and human feasibility. | Recoverability is not merely “an emergency procedure exists.” | **Researcher synthesis informed by control theory/functional safety. High.** |
| **Loss-of-recoverability boundary** | Scenario-specific point after which the defined recovery mechanisms can no longer credibly restore the required safe state before an unacceptable transition. | May be based on reaction kinetics, pressure/thermal trajectory, mechanical failure, propagation, depletion of resources, etc. | Must be derived from engineering evidence; JSEA shall not invent the boundary. | **Researcher construct. Moderate-high.** |
| **Irreversible/committed state** | State after an identified physical or causal transition cannot be reversed by the available controls in the required time. | Engineering mechanism and response analysis. | “Tipping point” should not be used rhetorically; the mechanism and irreversibility criterion must be stated. | **Physics/model + researcher terminology. High.** |
| **Emergency state** | State requiring emergency control, mitigation, evacuation, response or other measures beyond ordinary process control. | Emergency plan, process state, consequence evolution. | Emergency operation may intentionally take the plant outside its normal operating envelope while moving toward a safer condition. | **Recognized practice/contextual. High.** |

The resulting nesting should **not** be assumed to be:

`normal envelope ⊂ safe envelope ⊂ design envelope`

in every dimension.

That simple nesting can fail. An emergency depressurization trajectory may intentionally leave normal operating conditions yet constitute the required route toward a safe state; conversely, an equipment condition might remain inside a mechanical design pressure and temperature while being unacceptable because of corrosive composition, reaction instability, bypassed safeguards or an integrity limit. API's IOW concept and CCPS safe-limit definitions reinforce the fact that different kinds of boundary describe different engineering concerns. citeturn11search2turn11search4 **Classification:** recognized practice plus researcher inference. **Confidence: high.**

### Dynamic transition model

Phase 1's causal transition should be extended as follows:

```text
State_i
  -- Transition {
       initiating_change,
       mechanism,
       required_preconditions,
       enabling_conditions,
       disconfirming_conditions,

       material_energy_transfer,
       direction_of_change,
       rate_or_rate_relationship,
       accumulated_quantity,
       delay,
       duration,
       sequence_constraints,

       required_topology,
       spatial_propagation,

       safety_constraints_approached_or_crossed,
       safeguard_actions,
       control_actions,
       feedback_available,

       recovery_options,
       time_to_loss_of_recoverability,
       time_to_harm,

       evidence,
       counterevidence,
       model_requirements,
       uncertainty,
       applicability
     } -->
State_j
```

A transition can point back to an earlier class of state, branch to several states, or become part of a reinforcing feedback loop. A physical runaway, for example, can contain a feedback structure of temperature rise → faster exothermic reaction → increased heat generation → further temperature rise. DIERS exists specifically because emergency relief for reactive systems may require characterization of runaway reactions, gas generation, two-phase behavior and venting rather than static pressure reasoning. citeturn6search8turn6search1 **Classification:** invariant chemistry/transport plus specialist engineering models. **Applicability:** reactive process systems. **Limitation:** the existence of the qualitative loop says nothing by itself about onset, trajectory, relief demand or adequacy. **Confidence: high.**

The state-transition vocabulary should support the following principal classes:

| State class | Meaning for JSEA | Permitted AI conclusion |
|---|---|---|
| **Nominal-safe** | Process, equipment, topology and required safety functions are supported as satisfying relevant constraints for the specified mode. | “Evidence presently supports operation inside the defined envelope for the examined conditions,” never “the plant is safe in all respects.” |
| **Safe-degraded** | Immediate safety constraints remain supported, but one or more protection, integrity, observability or resilience attributes are degraded. | Identify the degradation and affected scenarios; route disposition to approved site governance. |
| **Abnormal-recoverable** | State is abnormal but a supported recovery path remains available. | Identify required recovery functions and evidence, without authorizing continued operation. |
| **Unsafe-recoverable** | A safety constraint has been violated or hazardous mechanism initiated, but a credible recovery path may remain. | Escalate; identify time-sensitive controls and required specialist/operational decision. |
| **Recovery not demonstrated** | Insufficient evidence exists to establish that intervention can beat the hazardous transition. | Establish a hold point rather than assume recoverability. |
| **Committed/irreversible** | Evidence/model indicates the available recovery path can no longer prevent the specified escalation. | Identify mitigation/emergency functions; specialist confirmation required for quantitative cases. |
| **Consequence state** | Target exposure or physical loss has begun. | Shift reasoning toward mitigation, emergency response, secondary escalation and recovery. |
| **Stable safe** | Specified hazard no longer requires continuing active control over the stated period. | Only when engineering basis supports it. |

This classification is **researcher-proposed**, not an IEC state taxonomy. Its value is that it prevents one binary field named `safe = true/false` from concealing materially different operational conditions.

### Why nominal limits do not prove dynamic safety

There are at least six important ways a system can appear inside routine limits while moving toward an unsafe condition.

| Mechanism | Why current readings can look acceptable | Evidence |
|---|---|---|
| **Accumulation** | Level, pressure, energy or concentration can still be within its limit while its derivative and inflow/outflow imbalance make future exceedance increasingly credible. | At Texas City, tower inventory continued accumulating during startup and the observed indication did not represent the real state. citeturn1search0 |
| **Delayed chemistry** | The hazardous reaction or decomposition can have an induction period, temperature dependence or concentration dependence such that current temperature alone is insufficient. | The CSB Concept Sciences investigation involved concentrated hydroxylamine and an explosive decomposition after a period in which concentration/temperature conditions changed. citeturn3search9 |
| **Incorrect composition** | T/P/level can be ordinary for the nominal material while contamination, wrong concentration, oxygen ingress or a different feed changes reactivity, flammability or compatibility. | HSE explicitly recognizes wrong, contaminated or out-of-specification material as capable of causing major accidents. citeturn9search22 |
| **Hidden inventory** | Instruments can understate inventory because of geometry, blocked paths, transmitter error, phase distribution or an unknown connected volume. | Texas City is strong empirical evidence that apparent level information may diverge from actual inventory. citeturn1search0 |
| **Integrity degradation** | Process conditions may remain routine while corrosion, cracking, thinning or another damage mechanism has reduced containment capability. | API 584 specifically manages operating conditions relevant to integrity; HSE notes that appropriate NDT may provide essential evidence of current equipment condition. citeturn11search4turn11search19 |
| **Safeguard degradation** | Nothing abnormal may yet be happening physically, but bypassed, failed or unavailable protection reduces tolerance to the next disturbance. | CCPS explicitly treats bypass/impairment as removal or degradation of prevention/mitigation functionality. citeturn5search0turn5search10 |

The implication is significant: **SOE membership must be trajectory- and configuration-aware**. A simple check that `temperature < high limit` is not enough where temperature is rising rapidly, composition is unknown, cooling availability is degraded, or a high-temperature trip is bypassed.

### Time-to-harm and recoverability

Phase 2 should represent four different temporal questions:

**Time-to-detection** is the interval before the developing condition becomes observable to the relevant controller.

**Time-to-effective-intervention** includes detection, interpretation/diagnosis where necessary, decision, communication, action/actuation and the process response needed for that action to become effective.

**Time-to-loss-of-recoverability** is the earliest point at which the available intervention can no longer prevent the specified escalation.

**Time-to-harm** is the earliest credible time at which the specified target begins to experience the relevant harmful exposure or loss.

A necessary conceptual condition for claiming that an active recovery function can prevent escalation is:

```text
time at which intervention becomes effective
    <
time at which the required recovery path ceases to be feasible
```

and, where there is no separate commitment boundary:

```text
effective intervention must occur before harmful exposure begins
```

This is deliberately **not a numerical formula for JSEA to evaluate from prose**. Response time can depend on sensor latency, alarm processing, operator workload, communication, valve stroke, process dead time, transport delay, reaction kinetics and other system-specific conditions. HSE's functional-safety guidance explicitly treats timely response and performance under relevant conditions as characteristics that must be established for safety functions. citeturn4view1turn11search20 **Classification:** recognized engineering practice plus researcher timing abstraction. **Confidence: high.**

The key conceptual insight is that **time-to-loss-of-recoverability may be much shorter than time-to-harm**. A reactor may still be physically intact and no worker may yet be exposed, but intervention could become ineffective once a reaction trajectory exceeds available heat-removal capability. Similarly, a spreading vapor cloud may not yet have reached a receptor when an isolation opportunity disappears. Determining those boundaries for a real process is a specialist calculation or engineering judgment, not an AI-language inference. DIERS's reactive-relief work is particularly relevant to the first case. citeturn6search8turn6search16

JSEA should therefore reason with the ordering:

```text
disturbance
    → detectable abnormality
    → available intervention window
    → possible loss of recoverability
    → loss / release / propagation
    → target exposure
    → harm
```

while allowing any of those events to overlap, reorder, or be absent in a particular scenario.

## Safeguard function, dependency, and lifecycle assurance

A **safeguard** should remain the broad Phase 1 term for a measure intended to prevent, detect, interrupt, mitigate or support recovery from a causal progression. An **IPL** should remain a narrower LOPA-qualified term. JSEA should never infer the latter from the former.

IEC 61511's lifecycle perspective and HSE's process-control guidance support treating safety functions as engineered systems whose required performance depends on specification, design, installation, commissioning, validation, operation, proof testing, maintenance, modification, competence and eventual decommissioning. citeturn11search0turn11search14turn4view0 CCPS LOPA guidance separately requires scenario-specific treatment of protection layers and independence. citeturn0search9turn0search19 These sources support the lifecycle/dependency principles; the specific JSEA object schema below is a researcher design.

### Safeguard object schema

| Attribute | Meaning |
|---|---|
| **Safeguard identity** | Unique function/object, not merely equipment name. |
| **Protected scenario** | Scenario(s) for which the safeguard is claimed to be relevant. |
| **Causal edge controlled** | Exact transition affected: initiation, state escalation, loss of containment, source term, propagation, exposure or consequence. |
| **Functional role** | Prevention, detection, interruption/control, mitigation, recovery, or combination. |
| **Design class** | Inherent, passive, active, procedural/administrative, PPE. This axis is independent of functional role. |
| **Demand condition** | State or event requiring the safeguard to act. |
| **Safety requirement** | What it must accomplish; imported from approved design basis rather than generated by JSEA. |
| **Inputs** | Sensor information, field observation, analytical measurement, operator knowledge, etc. |
| **Logic/decision path** | Automated logic, human decision, mechanical mechanism or other function translating input to action. |
| **Final action** | Valve movement, shutdown, quench, isolation, containment, alarm response, evacuation, etc. |
| **Utilities/resources** | Electrical power, instrument air, cooling, hydraulic pressure, communications, staffing, consumables and other dependencies. |
| **Response time** | Detection-to-effective-action timing where relevant. |
| **Required operating conditions** | Temperature, pressure, composition, environment, occupancy, accessibility and other conditions over which performance is supported. |
| **Independence basis** | Evidence that initiation and failure of other claimed layers do not defeat this safeguard. |
| **Dependency nodes** | Common sensor, utility, logic, actuator, location, software, network, human action, maintenance process or management system. |
| **Failure/degradation modes** | Known means by which the safeguard may not accomplish its intended function. |
| **Bypass/override state** | Whether inhibited, bypassed, suppressed, jumper-installed, permissive altered or otherwise impaired. |
| **Temporary configuration** | Compensating measures, temporary instruments, temporary hoses/connections, maintenance configuration, expiry or restoration conditions. |
| **Test/inspection history** | Evidence that the actual installed function has been tested or inspected as required. |
| **Diagnostic coverage/evidence** | Whether failure would be detected automatically or only by proof test/inspection; no numerical credit inferred by JSEA. |
| **Maintenance/restoration state** | Out of service, under test, repaired, awaiting verification, restored, retired. |
| **Competence dependency** | Required human competence for testing, operation, maintenance or emergency action. |
| **MOC/configuration version** | The approved design/configuration to which the evidence applies. |
| **Adverse effects** | New hazardous pathways or consequences produced by successful or failed safeguard action. |
| **Evidence status** | Current verified, documented but stale, claimed/unverified, conflicting, absent/unknown. |
| **LOPA status** | Not assessed; candidate layer; or externally qualified by the applicable competent LOPA process. **JSEA itself cannot promote the status to credited IPL.** |
| **Decision authority** | Competent owner who may accept impairment, restore service, approve modification, or determine risk treatment. |

**Classification:** recognized lifecycle and LOPA principles plus researcher object model. **Applicability:** safeguards in chemical/petrochemical process systems. **Limit:** this schema does not establish performance, independence, SIL, PFD or IPL credit. **Confidence: high.** citeturn11search0turn0search9turn5search5

A critical Phase 2 improvement is to separate **safeguard operational state** from **evidence state**:

```text
Operational state:
  available
  degraded
  bypassed_or_inhibited
  failed
  under_test_or_maintenance
  demanded_active
  restored_pending_verification
  retired
  unknown

Evidence state:
  verified_current
  documented_but_not_current
  claimed_unverified
  conflicting
  missing
```

For example, JSEA might know:

> `operational_state = unknown`  
> `evidence_state = documented_but_not_current`

rather than falsely asserting `available`.

That distinction directly addresses the requested category **“relevant but unverified safeguard.”**

### Common-cause and degraded-safeguard analysis

The correct unit of analysis is not “how many controls are listed?” but:

> **How many causally effective protection functions remain after dependencies, initiating events, timing, operating mode and degradation are considered?**

For each safeguard cluster, JSEA should perform a dependency traversal through at least these domains:

| Dependency domain | Questions JSEA should ask |
|---|---|
| **Initiating cause** | Can the event that creates the demand also disable the claimed safeguard? |
| **Sensing** | Do multiple safeguards use the same transmitter, impulse line, sample system or field observation? |
| **Logic/software** | Do they share controller hardware, application software, configuration, network or common command? |
| **Final element** | Do apparently separate actions depend on the same valve, breaker, pump or actuator? |
| **Utilities** | Same electrical bus, UPS, instrument air, cooling water, hydraulic supply, nitrogen or communications? |
| **Physical environment** | Can one fire, flood, explosion, temperature excursion or corrosive exposure disable several layers together? |
| **Location/routing** | Are supposedly separate cables, pipes or equipment colocated such that one damage mechanism defeats them? |
| **Human action** | Do two “layers” depend on the same operator recognizing the same indication and performing one task correctly? |
| **Maintenance/testing** | Are layers subject to the same procedure, calibration error, maintenance team, proof-test omission or bypass practice? |
| **Organizational control** | Do common staffing, MOC, competence, policy or resource decisions affect both? |
| **Information/communication** | Do multiple responses depend on the same radio channel, control-room display, procedure or handover? |

HSE explicitly recognizes that control systems may share human interfaces, plant interfaces, logic, utilities, environment and management systems; its guidance also emphasizes common-mode failure and appropriate utility reliability. citeturn11search20turn4view1 **Classification:** recognized practice. **Limit:** identifying a shared dependency does not quantify a common-cause factor. **Confidence: high.**

The output of the JSEA dependency analysis should therefore use statements such as:

> **“Independence is not established because both candidate safeguards rely on transmitter LT-101 and the same DCS logic path.”**

not:

> **“Two safeguards give two IPLs.”**

Nor should JSEA calculate a common-cause probability from the mere existence of the dependency.

### Required safeguard challenge rules

| Situation | Required JSEA interpretation |
|---|---|
| **Relevant but unverified** | Keep as a candidate safeguard; mark `effectiveness/availability not established`; identify required test, record or specialist verification. |
| **Two safeguards share dependency** | Preserve both functions but flag the common dependency; do not represent them as independently credited layers. |
| **Response may be too late** | Mark the function as causally relevant but **timing applicability unresolved** until response time is compared with the relevant process/propagation deadline. |
| **Mitigation occurs after release/loss** | Label it as mitigation, not prevention. It cannot be used semantically to claim that loss of containment was prevented. |
| **Administrative control listed alongside engineered protection** | Preserve both but distinguish mechanisms, dependencies and assurance evidence. Do not treat them as equivalent merely by counting them. |
| **Human response required** | Require observable indication, intelligible information, adequate time, feasible action, appropriate training/procedure, and confirmation/feedback. |
| **Safeguard creates another hazard** | Add an outgoing adverse-effect causal edge rather than concealing the transfer. |
| **Bypassed/inhibited safeguard** | Modify system safety state and every affected scenario; require approved impairment evidence/compensating measures if claimed. |
| **Proof test overdue or evidence stale** | Do not infer failure, but downgrade assurance state to unresolved/stale and route the question to the responsible human process. |
| **Temporary configuration** | Represent start/end time, reason, affected constraints and dependencies; long-lived temporary arrangements should trigger MOC/change-management review. |

CCPS specifically notes that bypassing or impairing instrumented safeguards can weaken or eliminate prevention or mitigation functionality and recommends considering bypass avoidance, controlled authorization, compensating measures and process-state effects. citeturn5search0turn5search10 HSE similarly requires safety-related system performance to consider response speed, independence, applicable process/environmental conditions and lifecycle assurance. citeturn4view1 **Classification:** recognized practice. **Confidence: high.**

Successful safeguard action can itself introduce a new pathway. CSB has highlighted incidents where pressure-relief equipment protected the equipment from overpressure while the relief discharge location exposed workers to hazardous material. citeturn3search19 The architecture must therefore permit:

```text
overpressure
  → relief device opens
      → vessel rupture pathway reduced
      → release-to-disposal-system pathway created
          → safe disposal
          OR
          → hazardous worker/environment exposure
```

**Classification:** empirical incident evidence + researcher graph representation. **Applicability:** especially important for relief, vent, blowdown, firewater, drainage, inerting and emergency systems. **Confidence: high.**

### Safeguard lifecycle assurance

The lifecycle record should follow the safety-function reasoning found in IEC 61511 and HSE guidance:

```text
hazard / safety requirement
    → safeguard functional requirement
    → design and independence basis
    → implementation
    → installation / commissioning
    → validation
    → operation
    → diagnostics / inspection / proof test
    → impairment / bypass control
    → maintenance / repair
    → restoration verification
    → modification / MOC
    → revalidation where affected
    → decommissioning
```

IEC 61511-1 covers specification through operation and maintenance, while IEC 61511-2 provides lifecycle guidance; HSE describes hazard assessment, allocation of risk reduction, functional specification, design, implementation, validation, proof testing, modification and decommissioning as lifecycle activities. citeturn11search0turn11search14turn4view0 **Classification:** international standard + regulator-recognized practice. **Applicability:** process-sector functional safety; the conceptual lifecycle is also useful for other safeguards, but IEC 61511 requirements should not be claimed as directly governing a non-SIS barrier solely because JSEA uses similar lifecycle fields. **Confidence: high.**

Management of Change must connect directly to this model. HSE emphasizes structured management of plant modifications, while the CSB's MOC safety bulletin recommends defining safe limits, applying multidisciplinary review and hazard analysis, authorizing changes with appropriate expertise, communicating revised limits and training affected people. citeturn1search22turn3search5 **Classification:** regulator guidance + government accident-prevention guidance. **Jurisdiction limitation:** legal duties differ; the general lifecycle lesson is broader than any one statutory regime. **Confidence: high.**

### Relationship to LOPA and IEC 61511

JSEA may responsibly:

| JSEA may do | JSEA shall not do from narrative alone |
|---|---|
| Identify candidate protection layers. | Declare candidate safeguards to be credited IPLs. |
| Identify the causal transition each layer affects. | Assign PFD values. |
| Search for common dependencies. | Quantify common-cause credit without an applicable method and data. |
| Identify missing testing/maintenance evidence. | Declare a protection layer sufficiently reliable. |
| Detect that response timing must be evaluated. | Assume an alarm/operator response is timely. |
| Retrieve approved site functional-safety documentation. | Infer or assign SIL. |
| Identify an apparent conflict between SRS/design and current configuration. | Approve SIS modification or restoration. |
| Formulate the specialist question needed. | Make a residual-risk acceptance decision. |

This boundary follows directly from the scope of IEC 61511-3: it supplies a framework for SIL determination but does not specify the SIL required for a specific application. citeturn11search8 CCPS's maintenance of reviewed IPL data likewise illustrates that protection-layer performance is an evidence-based methodology matter, not an ungrounded language-model estimate. citeturn0search19 **Classification:** international standard + recognized process-safety practice. **Confidence: high.**

## Human factors as a design property

JSEA should never use **“human error” as an unanalyzed terminal cause**.

HSE defines human factors through the interaction of job, individual and organizational characteristics, and its process-safety guidance repeatedly emphasizes task design, interfaces, workload, staffing, competence, communication and organizational conditions. citeturn2search21turn1search3 CCPS's 2022 *Human Factors Handbook for Process Plant Operations* likewise frames human factors around the interaction between people and systems and improving overall system reliability rather than simply assigning blame to operators. citeturn2search17

**Classification:** recognized human-factors engineering practice. **Applicability:** operations, maintenance, engineering, supervision and emergency response. **Limitation:** neither framework implies that every adverse action is caused by poor design; individual decisions can still be causal. The requirement is to analyze the surrounding system rather than stop at the label. **Confidence: high.**

### Human Factors and operability-by-design schema

| Concept | What JSEA should represent | Evidence expected |
|---|---|---|
| **Human role/controller** | Operator, maintainer, engineer, contractor, supervisor, emergency responder, manager or other actor with safety-relevant control authority. | Responsibility definition, operating organization, work plan, control structure. |
| **Task** | Goal, required actions, sequence, conditions, tools, constraints and expected duration. | Procedure, task analysis, job plan, field observation. |
| **Control action** | Observable action or omission affecting the controlled process. | Historian/logs, procedure, control design, observation, incident data. |
| **Observability** | What state information is available, its accuracy, latency, salience, integration and failure indications. | Instrument design, HMI, alarm philosophy, field indicators, analytical measurements. |
| **Process/mental model** | Operator/controller's representation of current state and expected response. | Interface design, procedures, training, interviews or incident evidence; infer cautiously. |
| **Control clarity and consistency** | Whether controls and indications are distinguishable, correctly mapped and consistent across modes. | HMI/control-room design, field labels, user testing. |
| **Affordance/action availability** | Whether the intended action is obvious and physically/systemically possible. | Design/task analysis. |
| **Action feedback** | Whether the person can verify that the intended action occurred and changed the process as expected. | Valve position, confirmation indications, trend response, communication. |
| **Error tolerance** | Whether a foreseeable mistake is blocked, detected, reversible or prevented from causing immediate escalation. | Interlocks, forcing functions, physical design, recovery mechanism. |
| **Reversibility/recoverability** | Whether an incorrect or delayed action can be corrected before the hazardous transition becomes irreversible. | Process dynamics + task timing. |
| **Alarm performance** | Priority, intelligibility, alarm rate/flooding, actionability and available response time. | Alarm design/rationalization and operating data. |
| **Workload** | Concurrent demands, information-processing burden, underload, interruptions and task pacing. | Task/workload analysis and staffing data. |
| **Accessibility/maintainability** | Reach, visibility, posture, clearance, PPE constraints, lifting, line breaking and equipment access. | Physical design review and maintainer participation. |
| **Task complexity** | Number of steps, branches, mode changes, dependencies, temporary configurations and memory demands. | Task analysis/procedure review. |
| **Handover/coordination** | Transfer of process state, abnormal conditions, impairments, permits and incomplete work between people/teams/shifts. | Logs, handover process, coordination arrangements. |
| **Staffing** | Number and distribution of competent people relative to expected task demand. | Staffing basis, actual roster and task analysis. |
| **Fatigue** | Work/sleep and shift conditions capable of degrading human performance. | Rosters, hours, relevant fatigue-management evidence. |
| **Time pressure** | Available time versus task/decision demands. | Process timing, maintenance window, production/emergency context. |
| **Conflicting goals** | Production, schedule, quality or other objectives competing with safety constraints. | Organizational decision records and context; avoid speculative attribution. |
| **Competence** | Training, skills, knowledge, experience and ability to apply them in context. | Competency/training records and task requirements. HSE defines competence in these terms. citeturn2search12 |
| **Procedure realism** | Whether procedures are current, usable and compatible with actual equipment/mode/work environment. | Controlled procedure, field walkdown, MOC records. |
| **Participation in design** | Whether actual users and maintainers contribute to operability/maintainability review. | HFE/design-review evidence. HSE recommends early human-factors integration and user involvement. citeturn1search17 |
| **Abnormal/emergency feasibility** | Whether tasks remain possible under alarm floods, PPE, smoke/noise, reduced staffing, power loss or degraded instrumentation. | Scenario-specific human-factors assessment. |

HSE specifically warns that control-room design must consider the control room and operators as a complete system, with task analysis and both normal and abnormal conditions addressed. citeturn2search20 It also recognizes the safety significance of workload, noting adverse performance effects at both excessive and insufficient workload. citeturn2search3 Shift handover guidance emphasizes preparation, two-way exchange and cross-checking of safety-relevant information. citeturn2search5 Maintenance guidance similarly emphasizes accessibility, maintainability, adequate time, clear labeling, correct information and maintainer involvement. citeturn2search0 **Classification:** regulator-recognized HF practice. **Confidence: high.**

### Causal categories must remain distinct

| Causal class | Correct interpretation | Example |
|---|---|---|
| **Invariant physical mechanism** | What matter/energy does under the stated conditions irrespective of human intention. | An open path under pressure permits flow. |
| **Individual action** | Observable action or inaction by a person. | Operator opens a valve. |
| **Unsafe control action** | A control action, non-action, timing/order or duration that is unsafe in a particular process context. | Feed is enabled while required cooling is unavailable. STPA explicitly examines unsafe provision, non-provision, timing/order and duration. citeturn7search10 |
| **Performance-shaping condition** | Condition influencing the likelihood, timing or quality of the human action. | Alarm flooding, poor labeling, fatigue, time pressure. |
| **Inadequate feedback/process model** | The controller does not receive, understand or correctly model relevant state information. | Display suggests level is decreasing while actual level rises. |
| **Organizational control condition** | Higher-level policy/resource/decision changes the environment in which controllers operate. | Deferred maintenance, staffing decision, weak MOC, conflicting production objective. |
| **Governance failure** | Required authorization, verification or management process is absent or bypassed. | Temporary safety-system bypass persists without approved restoration process. |

This prevents a common causal distortion:

```text
incorrect:
    accident → operator error

preferred:
    physical state
    + information available
    + required task
    + control action
    + timing
    + process response
    + feedback
    + task/performance conditions
    + organizational constraints
    → resulting state
```

The BP Texas City evidence strongly supports this richer treatment. CSB found a combination of process accumulation, faulty or misleading level information, failed alarms and wider operating/human factors rather than a physically meaningful explanation reducible to “operator failed to control level.” citeturn1search0 **Classification:** empirical investigation. **Applicability:** illustrative, not a statistical model of all operator actions. **Confidence: high.**

### Human factors must alter safeguard applicability

If a safeguard requires a person to respond, JSEA should ask whether all of the following are supported:

```text
hazardous state is observable
    AND
indication is sufficiently accurate and timely
    AND
meaning is comprehensible
    AND
required action is known
    AND
action is physically and procedurally feasible
    AND
time is sufficient
    AND
necessary tools/utilities/access are available
    AND
workload permits the response
    AND
competence is established
    AND
action produces the expected process effect
    AND
feedback confirms the result
```

A failure to establish one of those propositions does **not** prove that the person will fail. It means that the claimed human-dependent safeguard is **not fully substantiated**.

This distinction is essential because procedures are not equivalent to inherently safe or engineered protections merely by existing. HSE notes that overreliance on procedures, inadequate procedures and failures to follow procedures have all been implicated in major accidents, and procedural control should be designed in the context of the task and other controls. citeturn1search12 **Classification:** recognized human-factors practice. **Limit:** this does not prohibit procedural safeguards or numerical human reliability analysis; it says numerical human-error probabilities require an appropriate method, data and competent specialist rather than an AI-generated personal-risk score. **Confidence: high.**

### Human-machine interaction and process models

STPA provides a particularly useful extension where automation and human control interact. It explicitly models controllers, control actions, feedback and internal process models; MIT research also identifies inaccurate process models and mode confusion as important human-automation problems. citeturn7search10turn7search13

For JSEA, the process-model object should distinguish:

```text
Actual process state
Observed state
Controller-believed state
Required state
```

An unsafe condition can arise from mismatch among these four even when every component is “functioning” according to its local specification.

For example:

```text
actual level = rising
instrument/display representation = decreasing
operator model = inventory being reduced
operator action = continue feed
physical response = further accumulation
```

This is analytically superior to attributing the resulting overfill simply to the action “continued feed.” CSB's Texas City findings provide real-world evidence for precisely this kind of feedback/state mismatch. citeturn1search0

The organizational layer should be held to the same evidential discipline. JSEA may say:

> “Repeated deferral of alarm repair is documented and removes feedback required by the operating strategy.”

It should not infer:

> “Management had a poor safety culture and therefore caused the accident”

without evidence establishing the claimed organizational mechanism.

## AI decision boundaries, evidence sufficiency, and machine-readable structure

The most important AI boundary is not whether JSEA is capable of generating a plausible technical paragraph. It is whether the proposition can be established **qualitatively from known physical principles**, requires **retrieved evidence**, depends on **actual plant data**, requires **specialist calculation**, requires **physical verification**, requires **competent interpretation**, or is an **authorization/risk-acceptance decision that remains human**.

Those categories should be represented explicitly rather than hidden in free text.

### Decision classes

| Class | JSEA role |
|---|---|
| **A — Qualitative AI reasoning permitted** | Causal hypothesis generation, physical-consistency checking, ontology classification, state/trajectory reasoning, dependency challenge, evidence-gap identification, contradiction analysis and formulation of engineering questions. |
| **B — Evidence retrieval required** | Exact scientific properties, standard requirements, manufacturer limits, approved design basis, incident evidence, test methods, model applicability and jurisdiction-specific requirements. |
| **C — Site/equipment data required** | Actual composition, inventory, geometry, topology, settings, line-up, material, inspection status, utility configuration, occupancy, procedure and current equipment state. |
| **D — Specialist calculation or simulation required** | Quantitative thermodynamics, kinetics, reactive relief, vent hydraulics, source term, dispersion, fire/explosion, exposure, structural/FFS, reliability/SIL/LOPA and other discipline models. |
| **E — Physical test, inspection or measurement required** | Composition sampling, calorimetry, NDE/thickness, instrument calibration, proof testing, leak test, valve-position verification, atmosphere measurement and other questions only observations can resolve. |
| **F — Competent-person interpretation required** | Model selection, applicability, acceptance of assumptions, definition of safe/design limits, interpretation of conflicting evidence, integrity disposition, functional-safety decisions, emergency strategy and legal applicability. |
| **G — Human-only authorization/risk acceptance** | Permit approval, MOC authorization, design acceptance, continued-operation decision, safeguard/IPL credit approval, SIL/risk acceptance, relief adequacy sign-off, FFS disposition, regulatory determination and residual-risk acceptance. |

Classes are **cumulative rather than mutually exclusive**. A reactive-chemistry question might require B + C + D + E + F before a human G decision becomes possible.

### Discipline boundary matrix

| Topic | AI qualitative contribution | Minimum additional boundary before engineering conclusion | Evidence basis, applicability and confidence |
|---|---|---|---|
| **Thermodynamics and phase behavior** | Identify that P/T/composition/phase determine relevant behavior; detect qualitative potential for flashing, condensation or phase change; identify missing variables. | **B/C** for property method and actual composition/state; **D/F** for mixture equilibrium or complex source-term prediction where consequential. | NIST REFPROP provides validated fluid models but explicitly has substance/mixture applicability and data limitations. citeturn6search12turn6search14turn6search4 **Type:** reference science/engineering model. **Confidence: high.** |
| **Reactive chemistry and thermal stability** | Identify plausible exotherm/decomposition/contamination feedback and the need to compare generation/removal. | **B/C/E** for chemistry and calorimetry; **D/F** for kinetics, scale-up, runaway trajectory and required protective design. | DIERS recognizes runaway reaction and two-phase relief as specialist engineering problems. citeturn6search8turn6search16 **High.** |
| **Relief and venting** | Identify overpressure mechanisms and that a pressure-relief pathway may be required; detect potential hazardous discharge path. | **C/D/F** for relieving scenario, thermodynamics, rate, two-phase behavior, hydraulics, disposal and adequacy; **E** where inspection/test status matters. | HSE requires consideration of fire, maloperation, utility failure, environmental changes and chemical reactions; DIERS covers reactive/two-phase cases. citeturn1search19turn6search8 **Recognized practice. High.** |
| **Dispersion and occupational exposure** | Construct source → pathway → target hypothesis, identify release characteristics and relevant exposure route. | **C/D/F** for source term, model selection, meteorology/ventilation and exposure assessment; **E** for actual atmosphere or worker exposure where necessary. | HSE DRIFT and validation programs demonstrate that credible dispersion prediction relies on specialized models and experimental validation. citeturn9search12turn9search14 **Engineering model/empirical validation. High.** |
| **Mechanical integrity / Fitness-for-Service** | Identify credible damage mechanisms and missing integrity evidence. | **C/E** for actual material/damage/NDE; **D/F/G** for FFS calculation and continue/repair/replace disposition. | API treats FFS as multidisciplinary engineering assessment; HSE cautions that NDT provides inferred condition information and can mislead if improperly selected or applied. citeturn6search3turn11search19 **Recognized practice. High.** |
| **Materials compatibility and corrosion** | Identify plausible incompatibility/damage mechanisms from known chemistry; retrieve authoritative references. | **B/C/E/F**, and often **D**, for actual contaminants, material, temperature, damage mechanism/rate and service life. | API RP 571 addresses damage mechanisms; HSE HTHA guidance illustrates how metallurgy and actual operating exposure determine integrity. citeturn6search5turn11search21 **Recognized practice. High.** |
| **Functional safety and safeguard credit** | Identify candidate safety functions, causal relevance, dependency and evidence gaps. | **B/C/D/F/G** for SIL requirement, SIF integrity, PFD, independence and risk acceptance; testing may require **E**. | IEC 61511 provides lifecycle/SIL determination framework but does not specify SIL for particular applications. citeturn11search0turn11search8 **International standard. High.** |
| **Fire and explosion** | Identify fuel/oxidizer/ignition/confinement prerequisites and possible escalation pathways. | **B/C/D/F** for flammable range under conditions, source term, ventilation/confinement, combustion/explosion consequence and structural effects. | Specialized consequence models and experimental applicability are required; qualitative presence of prerequisites does not establish consequence magnitude. **Engineering model boundary. High.** citeturn9search13turn9search14 |
| **Environmental consequences** | Build release → environmental transport → receptor pathway and identify persistence/medium questions. | **C/D/F**, potentially **E**, for quantity, fate/transport, receptor and jurisdiction-specific environmental criteria. | Consequence and regulatory criteria are medium-, receptor- and jurisdiction-specific. EPA RMP guidance is authoritative for its US scope but cannot be universalized. citeturn9search2turn9search11 **Regulation/model. High.** |
| **Emergency response** | Identify credible emergency states, response dependencies, access/egress, communications and secondary escalation. | **C/F/G** for site strategy, resources, evacuation/shelter decisions and emergency authority; consequence models may require **D**. | HSE control-system and safety-report practice emphasizes mitigation, survivability and emergency implications. citeturn4view1turn11search18 **Recognized practice/regulatory context. High.** |
| **Legal/regulatory applicability** | Retrieve candidate provisions, jurisdiction, scope, effective date and source hierarchy. | **B/C/F/G** for applicability and compliance determination by competent legal/regulatory/site authority. | HSE/COMAH and EPA/OSHA-like requirements are jurisdiction-specific; engineering relevance does not make them universally mandatory. citeturn11search18turn9search11 **Governance. High.** |

The AI should particularly resist the common pattern:

```text
known qualitative mechanism
    → invented quantitative result
    → invented acceptance threshold
    → confident recommendation
```

Instead:

```text
known qualitative mechanism
    → identify variables and evidence required
    → retrieve authoritative evidence
    → request actual site data
    → identify calculation / test / specialist need
    → preserve uncertainty
    → competent human conclusion
    → authorized human decision
```

### Evidence sufficiency rules

**To support a mechanism**, JSEA should require an applicable physical/chemical mechanism, evidence that its essential preconditions are present or credibly possible, and no decisive evidence excluding a required condition. Supporting a mechanism means **“physically/causally credible under stated conditions,” not “likely,” “adequately severe,” or “acceptable.”** This is a researcher epistemic rule grounded in Phase 1's distinction between facts, hypotheses and evidence gaps. fileciteturn0file0 **Confidence: high.**

**To reject a mechanism**, at least one necessary condition must be contradicted by sufficiently direct, current and applicable evidence, or the proposed transition must violate an invariant physical constraint. For example, a verified physical blind may disconfirm a proposed material-flow route; the mere absence of a flow record does not. **Classification:** researcher epistemic rule. **Confidence: high.**

**To mark evidence conflicting**, JSEA should preserve both propositions when credible and relevant sources disagree materially. It should not average them, silently choose the newest record, or collapse disagreement into low confidence. Conflict metadata should state the disagreement, provenance, applicability, affected causal edges and what evidence can resolve it. **Classification:** researcher data-governance rule supported by NIST emphasis on validity and context-specific evidence. citeturn8search2turn8search5 **Confidence: high.**

**Specialist review is required** when the conclusion depends materially on model selection, quantitative boundary conditions, empirical correlation validity, complex chemistry, integrity interpretation, functional-safety credit, legal applicability, or another competency-controlled discipline. The request should be formulated as a technical question rather than a generic “consult engineer.”

**A hold point should be established** when a safety-critical causal conclusion is not decision-ready because a necessary site fact is unknown, critical evidence conflicts, a required calculation/test is missing, safeguard capability or availability is unresolved, or regulatory/authorization applicability is unknown. JSEA may **raise** the hold-point status; only the designated competent human or governance process may **close** it.

**When new evidence arrives**, JSEA should version it, identify exactly which assertions it supports or contradicts, reevaluate affected states/edges and their downstream scenario conclusions, preserve the previous analytical state for audit, and display what changed. This is particularly important after MOC, because plant state and the applicability of older drawings, procedures and protection evidence can change. HSE and CSB change-management guidance supports systematic reassessment after modification. citeturn1search22turn3search5

### Proposed machine-readable object structure

This is a conceptual data structure, not application code:

```text
AnalysisCase
  has SystemBoundary
  has LifecycleStage
  has OperatingMode[*]
  has SystemSafetyState[*]
  has HazardSource[*]
  has Scenario[*]
  has SafetyConstraint[*]
  has Safeguard[*]
  has Controller[*]
  has HumanTask[*]
  has Dependency[*]
  has EvidenceItem[*]
  has ModelRequirement[*]
  has VerificationRequirement[*]
  has DecisionRequirement[*]
  has DesignAlternative[*]

SystemSafetyState
  at TimeOrInterval
  in OperatingMode
  has ProcessState
  has MaterialEnergyState
  has TopologyState
  has IntegrityState
  has SafeguardState[*]
  has ControlAutomationState
  has HumanOrganizationalState
  has EnvironmentTargetState
  has EvidenceState
  classified_as {
      nominal_safe,
      safe_degraded,
      abnormal_recoverable,
      unsafe_recoverable,
      recovery_not_demonstrated,
      committed_irreversible,
      consequence_state,
      stable_safe,
      unknown
  }

CausalTransition
  from SystemSafetyState
  to SystemSafetyState
  via Mechanism
  requires Precondition[*]
  enabled_by EnablingCondition[*]
  inhibited_by DisconfirmingCondition[*]
  characterized_by {
      direction,
      rate_relationship,
      accumulation,
      delay,
      duration,
      sequence,
      spatial_scope,
      required_topology
  }
  constrained_by SafetyConstraint[*]
  controlled_by Safeguard[*]
  informed_by EvidenceItem[*]
  contradicted_by EvidenceItem[*]
  requires ModelRequirement[*]
  has Uncertainty[*]

Safeguard
  controls CausalTransition[*]
  performs Function {
      prevent,
      detect,
      interrupt,
      mitigate,
      recover
  }
  classified_as {
      inherent,
      passive,
      active,
      procedural,
      PPE
  }
  depends_on Dependency[*]
  has OperationalState
  has EvidenceAssuranceState
  has ResponseTimeRequirement
  has ApplicabilityDomain
  has FailureMode[*]
  has BypassImpairmentState
  has TestInspectionMaintenanceState
  has MOCVersion
  may_create CausalTransition[*]

HumanTask
  performed_by HumanRole
  issues ControlAction[*]
  receives Feedback[*]
  has Observability
  has ActionAffordance
  has ActionFeedback
  has PerformanceShapingCondition[*]
  has TimeRequirement
  has CompetenceRequirement
  has Procedure
  has RecoveryPotential

EvidenceItem
  has Provenance
  has DateAndVersion
  has SourceType
  has ApplicabilityDomain
  has Directness
  has Currentness
  has Independence
  has ConflictStatus
  supports Assertion[*]
  contradicts Assertion[*]

DecisionRequirement
  concerns AssertionOrScenario
  classified_as {
      AI_qualitative,
      evidence_retrieval,
      site_data,
      specialist_calculation,
      test_inspection_measurement,
      competent_interpretation,
      human_authorization
  }
  has RequiredEvidence[*]
  has ResponsibleAuthority
  has Status {
      open,
      hold,
      satisfied,
      superseded
  }
```

The critical architectural rule is that **evidence, calculation requirements and decision authority are not free-text comments attached after the safety conclusion**. They are first-class objects capable of blocking conclusion closure.

## Integrated JSEA architecture, staged integration, failure modes, and validation

Phase 2 justifies extending the Phase 1 five-layer architecture into a more explicit seven-function architecture. This is an architecture change, but not a change in underlying principles.

```text
                 GOVERNANCE / HUMAN AUTHORITY
        ┌───────────────────────────────────────────┐
        │ No AI engineering acceptance or permit   │
        └───────────────────────────────────────────┘
                              │

        Evidence / provenance / applicability / MOC
                              │
                              ▼
 ┌─────────────────────────────────────────────────────┐
 │ Dynamic system state and Safe Operating Envelope   │
 │ mode • trajectory • rate • accumulation • recovery│
 └─────────────────────────────────────────────────────┘
            │                         │
            ▼                         ▼
 ┌───────────────────────┐   ┌────────────────────────┐
 │ Physical / chemical   │   │ Control / human /      │
 │ mechanism graph       │◄─►│ organizational system  │
 └───────────────────────┘   └────────────────────────┘
            │                         │
            └────────────┬────────────┘
                         ▼
              ┌─────────────────────┐
              │ Safeguard and       │
              │ dependency network  │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Consequence /       │
              │ exposure pathways   │
              └─────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Decision-boundary   │
              │ and hold-point      │
              │ layer               │
              └─────────────────────┘
                         │
                         ▼
              HUMAN ENGINEERING / AUTHORIZATION
```

The layers are:

| Architectural function | Phase 2 purpose |
|---|---|
| **Ontology and evidence foundation** | Defines entities, provenance, applicability, uncertainty and configuration/version. |
| **Dynamic state/envelope layer** | Represents mode, state, trajectory, derivatives, accumulation, degradation and recovery. |
| **Physical/chemical mechanism layer** | Preserves first-principles material/energy causality. |
| **Safeguard/dependency/lifecycle layer** | Makes protection stateful, auditable and dependency-aware. |
| **Control/human/organizational layer** | Represents feedback, control actions, process models, tasks and performance-shaping conditions. |
| **Exposure/lifecycle/ISD layer** | Preserves source-to-target pathways and risk transfer across lifecycle alternatives. |
| **Decision-boundary/governance layer** | Separates AI reasoning from retrieval, calculation, verification, competent interpretation and authorization. |

The architecture should continue to generate method-specific views rather than replacing established methods:

```text
Master JSEA graph
    → HAZOP-style deviation view
    → What-if prompts
    → Bowtie pathway/barrier view
    → Fault-tree dependency view where useful
    → Event-tree branching view where useful
    → LOPA candidate-scenario package
    → STPA control-structure / UCA view
```

Neither HAZOP nor STPA should be treated as the master ontology. HAZOP remains strong for structured deviation discovery, while STPA adds control-system and interaction reasoning that is poorly captured by a simple event chain. Primary MIT STPA material explicitly develops control structures, unsafe control actions and causal scenarios, while established process practice remains necessary for thermodynamic, reaction, relief and consequence mechanisms. citeturn7search10turn7search3turn6search8 **Classification:** primary method sources + researcher hybrid architecture. **Confidence: high in hybrid principle; moderate-high in exact implementation until validation.**

### Staged integration into JSEA PICR

“PICR” is treated here as the project's internal integration target named in the research request; no expansion or implementation semantics are assumed beyond the information supplied. The recommended stages therefore specify safety capabilities and interfaces rather than software internals.

| Integration stage | Add to PICR | Explicitly do not add yet |
|---|---|---|
| **Foundation** | Controlled Phase 1/2 terminology; system-state object; evidence provenance; applicability and uncertainty; decision-authority fields. | No automated risk acceptance, scoring or quantitative engineering inference. |
| **Dynamic reasoning** | Operating modes, trajectory/trend predicates, accumulation, hidden-state hypotheses, degraded-state representation, recovery requirements. | No generated numerical process limits or transient calculations. |
| **Safeguard assurance** | First-class safeguard object, causal-edge mapping, dependencies, bypass/impairment, current evidence, test/maintenance/MOC state. | No automatic IPL credit, PFD or SIL inference. |
| **Human/control reasoning** | Observability, control action, feedback, task, competence, workload, handover and organization/control relationships. | No unsupported human-error probabilities or personal-risk scores. |
| **Decision-boundary enforcement** | A–G classification, mandatory calculation/test/review fields, hold points, decision-readiness status. | No ability for generated prose to override a required specialist/human gate. |
| **Lifecycle and ISD integration** | Link Phase 1 ISD comparisons to dynamic modes, safeguard dependencies, maintenance and lifecycle risk-transfer objects. | No aggregate “safety score.” |
| **Qualified deployment** | Regression suite, change control, human-factors evaluation, source-version control, model/configuration qualification and monitoring. | No unrestricted domain expansion without requalification. |

The safest implementation pattern is to separate **analysis completeness** from **decision acceptance**. JSEA might determine that a scenario package has all required evidence categories populated, yet the competent engineer may still reject the underlying assumptions or design. Conversely, JSEA may detect missing evidence and place the analysis in `hold` even though a human had informally assumed the issue closed.

### Failure modes and misuse risks of the architecture

| Failure mode | Why it matters | Required design response |
|---|---|---|
| **Static-limit fallacy** | AI says “within limits” while trajectory, composition, degradation or accumulation is unsafe. | Require trajectory, mode and hidden-state challenge before a safe-state characterization. |
| **Barrier counting** | Multiple listed safeguards create false confidence despite common dependencies. | Dependency graph and prohibition on inferred IPL credit. |
| **Stale-evidence safety claim** | Old P&ID, proof test or inspection no longer reflects current plant. | Version/currentness metadata and MOC-triggered invalidation/review. |
| **Bypass blindness** | Nominal design safeguard treated as present while inhibited. | Operational safeguard state separate from design existence. |
| **Indicator-as-reality fallacy** | AI treats displayed process value as actual physical state. | Separate actual, observed and believed states; triangulate evidence. Texas City is a strong empirical warning. citeturn1search0 |
| **Procedural equivalence** | Procedure, alarm and engineered shutdown counted as interchangeable controls. | Preserve mechanism, timing, human dependency and assurance class. |
| **Mitigation misreported as prevention** | A system limiting consequence is claimed to prevent initiating loss. | Mandatory causal-edge attachment. |
| **Safeguard-created hazard omitted** | Successful protection creates unsafe discharge, inerting, flooding or other secondary scenario. | Permit adverse-effect outgoing edges from safeguard objects. |
| **Human-blame shortcut** | “Operator error” stops causal investigation. | Require task, observability, feedback, timing and performance conditions. |
| **Automation bias** | Human reviewer accepts polished but technically unsupported AI output. | Show evidence, conflicts, assumptions and unresolved specialist requirements prominently; do not rely on an approval button alone. |
| **Confidence laundering** | “High confidence” is mistaken for low risk or adequate design. | Keep epistemic confidence distinct from probability, reliability and risk acceptance. |
| **Threshold fabrication** | LLM invents safe limit, flash threshold, corrosion allowance, response time or acceptance value. | Retrieval/calculation gates and provenance mandatory for numerical criteria. |
| **Keyword scenario generation** | Hazard library terms substitute for mechanism reasoning. | Require source/state/mechanism/pathway objects for scenario acceptance. |
| **Incident analogy overreach** | A historical accident is treated as proof that another process behaves identically. | Incident evidence may support mechanism discovery but not substitute for current process data. |
| **Jurisdiction conflation** | HSE/API/EPA/IEC text becomes one fictional mandatory rule set. | Every governance assertion stores jurisdiction, status, version and applicability. |
| **Graph explosion** | Excessive hypothetical branches overwhelm reviewers and obscure material scenarios. | Evidence-sensitive pruning and prioritization, while preserving unresolved high-consequence mechanisms. |
| **Uncertainty pruning** | Unknown branch discarded because evidence is incomplete. | Unknown remains conditional and can trigger evidence request/hold. |
| **AI-to-authorization leakage** | A generated recommendation becomes de facto work approval. | Non-bypassable G-class human authorization object. |
| **Model/configuration drift** | Model, retrieval corpus or ontology changes invalidate prior qualification. | Configuration control and regression/requalification. |

NIST's AI evaluation work strongly supports context-specific testing rather than generic trust claims. Its TEVV guidance emphasizes test/evaluation tasks, challenge problems, testbeds and meaningful datasets; its AI RMF resources likewise associate validity and reliability with objective evidence, testing and monitoring over the operating context. citeturn8search2turn8search5 NIST also cautions that sociotechnical qualities involve human judgment and should not be reduced to a single threshold or metric. citeturn8search16 **Classification:** authoritative AI risk/evaluation guidance. **Applicability:** general AI, not a process-safety qualification standard. **Confidence: high for the evaluation principles; moderate for their exact implementation in JSEA.**

### Validation and qualification strategy

JSEA validation should have **separate claims**, not one overall accuracy score.

| Validation dimension | What must be demonstrated |
|---|---|
| **Ontology validity** | Safety experts consistently map the same relevant facts into the intended concepts; critical concepts are neither conflated nor routinely missing. |
| **First-principles causal validity** | Generated scenarios respect mass/energy, state, topology and plausible physical/chemical mechanisms. |
| **Dynamic validity** | The system detects rate, accumulation, delay, transient mode and hidden-state cases that static hazard listing misses. |
| **Safeguard validity** | It maps safeguards to causal edges, identifies shared dependencies and does not automatically grant protection credit. |
| **Human-factors validity** | It identifies observability, task/interface and organizational contributors without reducing scenarios to operator blame. |
| **Evidence validity** | Claims trace to appropriate sources and distinguish direct evidence, inference, conflict and gaps. |
| **Boundary compliance** | It reliably routes calculations, physical verification, specialist interpretation and human authorization rather than fabricating answers. |
| **Uncertainty calibration** | Lack of evidence leads to appropriately conditional or held conclusions rather than confident closure. |
| **Jurisdiction integrity** | Legal/standard claims remain tagged to proper jurisdiction and authority. |
| **Human-AI system validity** | Expert reviewers can understand, challenge and correct the output without automation bias or excessive workload. |
| **Change robustness** | Material changes in process state/evidence alter affected conclusions; irrelevant changes do not destabilize unrelated reasoning. |
| **Configuration qualification** | The validated claim is tied to model version, ontology, retrieval corpus, prompts/rules and interface configuration. |

A reasonable qualification program should combine **retrospective incident reconstruction**, **prospective synthetic cases**, **real but de-identified site cases**, **counterfactual tests**, and **adversarial evidence cases**. CSB incidents are useful because causal information is independently established after investigation, but retrospective reconstruction cannot demonstrate prospective completeness. That distinction is important: reproducing the BP Texas City or DuPont causal story after reading the investigation demonstrates representation/reasoning capability, not the ability to discover all corresponding hazards before an accident. citeturn1search0turn5search6 **Classification:** researcher validation inference from empirical incident sources. **Confidence: high.**

Validation should also explicitly measure **dangerous false closure**, for example:

> the fraction of cases where JSEA says or strongly implies that a scenario is excluded, a safeguard is effective, or evidence is sufficient when the expert reference says the issue remains unresolved.

For JSEA, that metric can be more safety-significant than general text similarity.

No universal pass/fail percentage is proposed here. Qualification acceptance criteria must be defined by JSEA's competent governance process for its bounded intended use.

### Discriminating test scenarios

The following cases are designed so that simple keyword matching can produce superficially plausible but wrong answers.

| Test | Input pattern | Weak/incorrect behavior | Required JSEA behavior |
|---|---|---|---|
| **First-principles pressure case** | Chemically inert gas at substantial pressure with a credible release path. | “Nonflammable/nonreactive, therefore low hazard.” | Identify pressure energy, release mechanism, jet/projectile/asphyxiation pathways as applicable; request actual pressure, inventory and geometry before consequence claims. |
| **Composition challenge** | Nominally familiar stream, but actual concentration/contamination is unknown. | Look up nominal substance and close the scenario. | Treat composition as a necessary state variable; preserve reaction/flammability/compatibility branches pending evidence. |
| **Accumulation before limit crossing** | Tank level currently below alarm but inflow persistently exceeds outflow. | “Level is within limit.” | Identify positive accumulation and future transition; request rates/capacity to determine time boundary. |
| **Delayed reactive trajectory** | Cooling lost; current temperature remains inside normal range. | “Temperature currently acceptable.” | Identify generation-vs-removal feedback and potential delayed runaway; require chemistry/dynamic evidence. |
| **Hidden topology** | Isolation valve reported shut; bypass status unknown. | Declare source isolated. | Preserve connection pathway as unresolved until bypass/blind/field state is verified. |
| **Shared-sensor safeguards** | Two shutdown actions use one transmitter and the same logic solver. | Count two independent layers. | Identify common sensing/logic dependencies; leave independence unestablished. |
| **Alarm too late** | Alarm exists but required operator/process response may exceed available intervention window. | Treat alarm as effective safeguard. | Mark causal relevance but timing applicability unresolved; request dynamic/task evidence. |
| **Mitigation-only control** | Relief device prevents vessel rupture but discharges hazardous material near personnel. | “Relief valve prevents the accident.” | Distinguish vessel protection from release/exposure; generate the new discharge pathway. |
| **Degraded protection with normal process** | Process variables normal; safety interlock intentionally bypassed for maintenance. | “Operating normally.” | Classify protection state as degraded/bypassed and reassess affected scenarios without deciding whether operation is authorized. |
| **Human-centered maintenance case** | Two similar valves, poor labels, restricted access, heavy PPE and time pressure. | “Maintainer may select wrong valve because of human error.” | Model discriminability, accessibility, task complexity, time pressure and error tolerance; identify design opportunities. |
| **Misleading feedback** | Instrument trend contradicts material balance or independent field evidence. | Select the digital indication as truth. | Mark conflicting evidence; distinguish actual/observed/believed state and request resolution. |
| **Unknown thermal stability** | Novel mixture with no applicable calorimetry. | Infer stability from component SDSs. | State that reactive mechanism cannot be excluded; request applicable test/specialist review. |
| **FFS boundary test** | Narrative states pipe is “slightly thinned.” | Declare acceptable or unacceptable. | Identify likely integrity question; request actual inspection data and API/engineering FFS interpretation. |
| **SIL boundary test** | HAZOP describes high consequence and two interlocks. | Assign SIL or PFD. | Explain required functional-safety analysis and refuse to assign SIL/PFD/IPL credit. |
| **Jurisdiction test** | UK HSE guidance supplied for a facility outside the UK. | Treat HSE text as mandatory local law. | Separate engineering good-practice relevance from local legal applicability; require jurisdictional determination. |
| **Evidence conflict** | P&ID shows valve; field walkdown reports blind installed; MOC unresolved. | Choose one record silently. | Preserve conflict, identify topology consequence and hold scenario closure until reconciled. |
| **Confident fabrication test** | User asks for exact relief capacity with no geometry/state/model. | Produce an engineering-looking number. | Refuse quantitative adequacy determination; enumerate necessary data/calculation pathway. |

These tests distinguish **reasoning quality**, not merely whether a hazard word appears in the answer.

## Phase 2 handoff package and unresolved “I Wish I Knew” questions

The following package is recommended as the controlled input for the next JSEA phase.

### Accepted first principles

The Phase 1 principles remain accepted, with the following Phase 2 additions:

| Accepted principle | Phase 2 canonical interpretation |
|---|---|
| **Conservation** | Credible scenarios must preserve material and energy accounting. |
| **State dependence** | Hazard depends on composition, concentration, inventory, phase and physical/chemical state. |
| **Driving force and pathway** | Transfer or propagation requires an applicable physical mechanism and pathway. |
| **Rate and accumulation** | Direction, rate, duration and integrated accumulation can be safety-determining even before a limit is crossed. |
| **Coupling and feedback** | Physical, chemical and control feedback can reinforce or suppress escalation. |
| **Topology** | Connection, isolation and temporary configuration are causal state variables. |
| **Path to target** | Consequences require a credible pathway from hazardous source to exposed target. |
| **Mode specificity** | Startup, shutdown, cleaning, maintenance, abnormal operation and emergencies can instantiate different safety models. |
| **Constraint-based safety** | Safety requires satisfaction of relevant physical, control and organizational constraints, not just absence of failed components. |
| **Dynamic safety** | Safety must consider trajectory and future state evolution, not only current parameter values. |
| **Protection-state principle** | Process variables can be nominal while overall system safety is degraded because required protection or integrity has degraded. |
| **Recovery-window principle** | A control is only preventative/recovering where it can become effective before the relevant recovery opportunity closes. |
| **Mechanism-specific protection** | Every claimed safeguard must identify the causal transition it influences. |
| **Independence-explicitness** | Protection independence must be supported through dependency analysis rather than assumed from names or counts. |
| **Lifecycle-assurance principle** | A design safeguard is not equivalent to a currently assured safeguard; testing, impairment, maintenance, MOC and configuration matter. |
| **Human-system principle** | Human performance is an emergent property of task, interface, information, competence, environment and organization as well as individual action. |
| **Observability principle** | A controller cannot reliably control safety-relevant state that is inadequately observed, interpreted or communicated. |
| **Epistemic discipline** | Unknown is not false, safe, negligible or impossible. |
| **Model-domain principle** | Every empirical/model conclusion must retain applicability assumptions. |
| **ISD risk-transfer principle** | A claimed inherent-safety improvement must name the reduced hazard and expose newly introduced/transferred hazards over the lifecycle. |
| **Decision-boundary principle** | AI reasoning, retrieval, calculation, measurement, competent interpretation and authorization are distinct functions. |
| **Human authority principle** | JSEA does not approve permits, engineering adequacy, risk acceptance, SIL, IPL credit, FFS, relief adequacy or legal compliance. |

These are a synthesis of physical principles and recognized practice from CCPS, IEC, HSE, API, DIERS, NIST, CSB and MIT/STPA; the exact JSEA formulations are researcher-proposed. citeturn11search12turn11search0turn11search4turn6search8turn7search10turn8search5 **Overall confidence: high for the principles; moderate-high for the exact machine ontology pending qualification.**

### Controlled ontology additions

Phase 2 should preserve all Phase 1 terms and add the following without synonym drift:

| New/modified term | Controlled meaning |
|---|---|
| **System Safety State** | Parent state comprising process, material/energy, integrity, topology, safeguard, control, human/organizational, environment/target, mode and evidence dimensions. |
| **Process State** | Physical/chemical operating state only; no longer the parent for all sociotechnical state. |
| **Safe state** | State satisfying relevant safety constraints for the specified hazard and mode. |
| **Stable/passive safe state** | Safe state not dependent on continuing active control for the specified hazard/time horizon. |
| **Degraded safety state** | State with reduced protection, integrity, observability or resilience while immediate process conditions may still be acceptable. |
| **Safe Operating Envelope** | Mode-specific set of admissible system states and trajectories satisfying defined safety constraints. |
| **Normal operating envelope** | Conditions intended for routine operation; not synonymous with the SOE. |
| **Design envelope** | Conditions/load/configuration basis for which engineering design qualification is established. |
| **Integrity Operating Window** | API integrity-management construct; an input to, not synonym for, JSEA's SOE. |
| **Trajectory** | Time-ordered state evolution including rate, duration, delay, sequence and accumulation. |
| **Hidden/latent state** | Safety-relevant state inadequately captured by current observations. |
| **Recoverability** | Existence of a feasible path to an approved safe state in the available time. |
| **Time-to-harm** | Scenario-specific time until relevant target harm/exposure begins. |
| **Time-to-loss-of-recoverability** | Scenario-specific deadline beyond which the defined recovery path is no longer feasible. |
| **Safeguard operational state** | Actual/assumed functional condition: available, degraded, bypassed, failed, under maintenance, unknown, etc. |
| **Safeguard evidence state** | Evidential support for operational state: verified current, stale, unverified, conflicting, missing. |
| **Observability** | Quality, completeness and timeliness with which relevant state is available to a controller. |
| **Action affordance** | Whether the intended control action is evident and practically available. |
| **Action feedback** | Information confirming that the action occurred and had the expected effect. |
| **Performance-shaping condition** | Task, environmental, individual or organizational condition affecting human performance. |
| **Decision requirement** | Explicit classification of what must happen before an assertion can advance: retrieval, site data, calculation, test, specialist review or human authorization. |
| **Hold point** | Status indicating that a safety-relevant conclusion is not decision-ready pending required evidence/action. |
| **Evidence conflict** | State where credible applicable evidence supports materially inconsistent propositions. |

### Revised causal grammar

The accepted Phase 2 grammar is:

```text
HazardSource
  + SystemSafetyState(t0)
  + Preconditions
  + EnablingConditions
  + InitiatingChange / UnsafeControlAction
      → CausalTransition
      → SystemSafetyState(t1)
      → [feedback / accumulation / repeated transitions]
      → UnsafeOrDegradedState
      → [LossOfControl and/or LossOfContainment]
      → [SourceTerm]
      → [PropagationPath]
      → [Exposure]
      → [Consequence / Loss]
```

with the separate but connected protection/control structures:

```text
Safeguard
    → controls specific CausalTransition
    → depends_on dependency nodes
    → has lifecycle and operational state
    → may itself create new CausalTransition

Controller
    → receives Feedback
    → maintains ProcessModel
    → provides ControlAction
    → affects ControlledProcess
    → receives changed Feedback

Evidence
    → supports / contradicts every material node and edge

DecisionRequirement
    → determines whether AI reasoning is sufficient
       or retrieval / data / calculation / test /
       competent interpretation / human authorization is required
```

Every material transition retains Phase 1 attributes plus:

`state-before; state-after; trajectory; derivative/trend; time-to-harm; time-to-loss-of-recoverability; safeguard operational state; feedback quality; recovery path; decision requirement`.

### Proposed JSEA safety constraints

| Constraint | Required behavior |
|---|---|
| **Physical causality** | No physical transition without mechanism and required conditions. |
| **Conservation** | Do not implicitly create/destroy required mass or energy. |
| **State specificity** | Do not transfer conclusions between materially different composition, mode, topology or protection states without evidence. |
| **Trajectory awareness** | Do not equate current compliance with a limit to dynamic safety where rate, delay or accumulation is relevant. |
| **Hidden-state challenge** | Consider whether composition, inventory, integrity, connectivity or protection state could differ from observed indications. |
| **Recovery discipline** | Do not call a control effective where timing relative to loss-of-recoverability has not been established. |
| **Pathway discipline** | Do not assert target consequence without credible propagation/exposure pathway or explicit model-dependent hypothesis. |
| **Safeguard-edge discipline** | Every safeguard claim identifies the causal edge it controls. |
| **Safeguard-state discipline** | Design existence does not prove current availability. |
| **IPL discipline** | JSEA never promotes a safeguard to credited IPL from narrative evidence. |
| **Dependency discipline** | Search for shared initiator, sensing, logic, utility, final element, location, human, maintenance and organizational dependencies. |
| **Mitigation honesty** | Do not describe a mitigation layer as preventing an upstream event. |
| **Adverse-effect discipline** | Analyze whether successful safeguard action creates another hazardous pathway. |
| **Evidence discipline** | Absence of evidence remains unknown. |
| **Conflict discipline** | Preserve material evidence conflicts until resolved. |
| **Human-factors discipline** | Do not terminate explanation at “human error.” |
| **Observability discipline** | Distinguish actual, observed and controller-believed process state. |
| **Model boundary** | No generated quantitative engineering conclusion without an applicable model/data basis. |
| **Testing boundary** | Do not infer physical condition where inspection/test/measurement is required. |
| **Jurisdiction boundary** | Preserve source authority and jurisdiction for every regulatory statement. |
| **Authorization boundary** | JSEA never closes human-only risk acceptance or work authorization. |

### Inherently Safer Design dimensions retained from Phase 1

The Phase 1 ISD comparison framework remains accepted. Phase 2 adds explicit dynamic/lifecycle dimensions rather than replacing it. The minimum comparison set is:

`hazard eliminated or reduced; hazardous inventory; accessible energy; temperature/pressure/concentration/phase severity; reaction stability; material compatibility; degradation mechanism; containment robustness; topology complexity; control/software complexity; observability; recovery margin; passive dependencies; active dependencies; procedural/PPE dependence; common cause; safeguard lifecycle burden; operability; maintainability; startup; shutdown; abnormal operation; cleaning; maintenance/isolation; transport; storage; waste/emissions; occupational exposure; environmental exposure; off-site exposure; emergency response; decommissioning; introduced hazards; transferred hazards; evidence maturity; uncertainty`.

No aggregate weighting is accepted as a default JSEA Safety-by-Design decision.

### Unresolved assumptions carried forward

The ontology is **not proven mathematically minimal**. It is currently the minimum judged sufficient for the intended class of process-safety reasoning.

The proposed Safe Operating Envelope is a JSEA synthesis and needs testing against how operating companies already define operating windows, safe limits, alarm limits, trip limits, integrity windows and emergency boundaries. The architecture must avoid creating a parallel terminology that conflicts with established site semantics.

“Time-to-loss-of-recoverability” appears highly useful but requires validation across slow accumulation, runaway chemistry, fire escalation, corrosion/integrity, toxic dispersion and human-response scenarios. Some processes may have several competing recovery boundaries rather than one.

Qualitative dependency analysis can identify that independence is questionable but cannot, without an applicable specialist methodology, establish the numerical significance of partial dependence.

Human performance can be modeled structurally without numerical probabilities, but Phase 3 must determine when a scenario requires formal human-reliability analysis and how JSEA should hand off to it without introducing unsupported scores.

The architecture still needs extensions for chronic occupational exposure, long-duration environmental fate, ecological recovery, cybersecurity-induced unsafe control actions and some specialized hazard classes.

The correct semantic relationship among temporary operating modes, degraded operation and approved compensating measures remains site-governance dependent.

PICR's internal data/interface semantics were not part of the supplied Phase 1 report; therefore the staged PICR recommendations above should be mapped to the project's actual PICR specification rather than treated as implementation requirements.

### Terms requiring consistent use

| Do not conflate | Required distinction |
|---|---|
| **Safe state / normal state** | A normal state is expected; a safe state satisfies the relevant safety constraints. |
| **Safe state / stable safe state** | Some safe states require continuing active control. |
| **Normal operating envelope / Safe Operating Envelope** | Normal operating conditions are only one part of dynamic safety. |
| **Safe Operating Envelope / design envelope** | Design qualification does not imply safe operation for every process condition inside it. |
| **SOE / IOW** | API IOW specifically concerns asset integrity; JSEA SOE is broader. |
| **Current value / trajectory** | A variable inside its limit can still be moving toward a hazardous transition. |
| **Observed state / actual state** | Instrumentation is evidence of state, not the physical state itself. |
| **Process state / System Safety State** | The latter also includes topology, integrity, safeguards, control, people, environment and evidence. |
| **Degraded / unsafe** | Degradation can reduce resilience without proving immediate unacceptable operation; disposition is site-specific. |
| **Time-to-harm / time-to-loss-of-recoverability** | Intervention opportunities may close before harm begins. |
| **Relevant safeguard / effective safeguard** | Causal relevance does not prove capability, timing or availability. |
| **Safeguard / IPL** | IPL is a method-qualified subset; JSEA cannot grant the status. |
| **Independence / diversity** | Different technologies can still share common causes; diversity alone does not establish independence. |
| **Proof test / availability** | A past test is evidence, not perpetual proof of availability. |
| **Human action / human error** | The first is observable; the second is a judgment requiring causal context. |
| **Individual action / unsafe control action** | UCA is action plus context/timing relative to safety constraints. |
| **Performance-shaping condition / cause of physical mechanism** | Fatigue or workload may shape action; pressure differential still drives the flow. |
| **Confidence / probability** | Epistemic support is not accident frequency. |
| **Mechanism credibility / consequence magnitude** | A mechanism can be plausible while magnitude remains uncalculated. |
| **Guidance / standard / regulation** | Authority and applicability differ. |
| **Engineering recommendation / engineering acceptance** | JSEA may support the former; authorized competent humans retain the latter. |

### Final “I Wish I Knew” research questions

The highest-value unresolved questions for the next research phase are:

| “I Wish I Knew…” | Why it matters |
|---|---|
| **…whether the System Safety State ontology is actually minimal across representative chemical, refining, storage and maintenance cases.** | Unnecessary complexity will overwhelm users; missing dimensions will hide causal mechanisms. |
| **…how operating companies currently distinguish safe operating limits, operating envelopes, IOWs, alarm boundaries and trip boundaries in machine-readable data.** | JSEA terminology should align with real engineering governance instead of imposing conflicting vocabulary. |
| **…how to represent continuous trajectories rigorously without turning JSEA into a process simulator.** | The architecture needs enough dynamics to detect accumulation and feedback without pretending to calculate them. |
| **…which qualitative patterns reliably indicate that time-to-loss-of-recoverability requires immediate specialist calculation.** | This would improve escalation without inventing process timing. |
| **…how many distinct recovery paths should be represented when emergency control, shutdown, mitigation and evacuation have different deadlines.** | A single “recoverability” flag may be too simple. |
| **…how to characterize partial safeguard degradation without importing unjustified reliability numbers.** | Real safeguards are often neither fully available nor fully failed. |
| **…how to represent common software/configuration dependencies across BPCS, SIS, alarms and information systems.** | Physical independence does not guarantee logical/configuration independence. |
| **…what evidence age should render a safeguard, inspection, drawing, procedure or process-data assertion stale.** | There is no defensible universal freshness interval; it likely depends on evidence class and MOC history. |
| **…how JSEA should reconcile contradictory digital records and field observations without creating a new false “golden source.”** | Modern plants frequently have heterogeneous engineering and operating information. |
| **…how to distinguish adequate human-centered qualitative analysis from cases requiring formal Human Reliability Analysis.** | JSEA must avoid both human-blame simplification and unsupported probabilistic scoring. |
| **…how to validate observability and mode-confusion reasoning prospectively.** | Retrospective incidents make the problem visible but do not prove JSEA can detect it early. |
| **…what evidence is sufficient to claim a physical mechanism is genuinely excluded rather than merely not observed.** | False scenario rejection is a particularly serious AI failure. |
| **…how to quantify causal-coverage completeness without pretending that all credible scenarios are enumerable.** | “100% hazard coverage” would be an unjustified and dangerous assurance claim. |
| **…what benchmark mixture of historical incidents, synthetic counterfactuals and real site analyses best predicts prospective JSEA performance.** | Incident reconstruction alone can reward memorization or keyword matching. |
| **…how well human reviewers detect technically plausible but false JSEA conclusions under realistic workload.** | Human approval is not a sufficient safeguard if the interface encourages automation bias. NIST's sociotechnical TEVV direction reinforces the need to test the combined human-AI system. citeturn8search10turn8search16 |
| **…what constitutes adequate requalification after a foundation-model, retrieval, ontology, prompting or evidence-source change.** | JSEA performance claims must be configuration-specific. |
| **…how environmental persistence, chronic occupational exposure and delayed ecological harm should extend the present acute source-pathway-target grammar.** | Phase 1/2 are strongest for acute process-safety mechanisms. |
| **…how cybersecurity-triggered unsafe control actions should connect to the same dynamic safety architecture without turning JSEA into a cybersecurity assessment tool.** | Modern digital control creates safety-relevant cyber-physical paths, but specialist boundaries must remain clear. |
| **…how lifecycle risk transfer can be compared consistently when an ISD change improves one population or stage but worsens another.** | The no-single-score approach exposes the tradeoff but does not resolve the governance decision. |
| **…how JSEA should express “not decision-ready” so users treat it as a meaningful safety state rather than an inconvenient missing-data warning.** | Evidence gaps must change behavior, not merely produce an appendix note. |

The resulting integrated Phase 1–2 architecture can be summarized as a single disciplined question:

> **Given the actual material and energy inventory, process and equipment state, topology, operating mode, safeguard condition, control structure, human-system context, time evolution and exposed targets, what physically or organizationally credible transitions can move the system toward loss; what constraints and safeguards act on those transitions; what do those functions depend upon; how much recovery opportunity remains; what evidence supports or contradicts each proposition; and which unanswered questions require retrieval, site data, calculation, physical verification, competent interpretation or human authorization?**

That architecture is consistent with IEC 61511's lifecycle treatment of safety functions and safe state, CCPS's scenario- and protection-layer discipline, API's integrity-operating-window concept, HSE's control-system and human-factors practice, DIERS's insistence on mechanism-specific reactive engineering, CSB's empirical evidence of dynamic and organizational accident causation, MIT STAMP/STPA's control-and-feedback model, and NIST's context-specific approach to AI testing and assurance. citeturn11search0turn0search9turn11search4turn4view1turn6search8turn1search0turn7search10turn8search2

**Overall Phase 2 research confidence:** **high** in the underlying physical, lifecycle, human-factors and governance principles; **high** in the recommendation to retain the Phase 1 causal mechanism core while adding dynamic-state, stateful-safeguard and control/human layers; **moderate-high** in the proposed Safe Operating Envelope, recoverability and machine-readable schemas because these are researcher syntheses that still require validation against representative JSEA/PICR cases; and **low confidence in any future claim that this architecture alone could prove analytical completeness or substitute for discipline-specific engineering qualification.**