# First-Principles Safety-by-Design Architecture for Chemical Processes

## Executive synthesis and Safety-by-Design axioms

### Executive summary

A credible AI architecture for chemical-process Safety by Design should begin neither with accident labels nor with generic lists of hazards, but with a **state-and-pathway model of matter, energy, equipment, time, control, and exposed targets**. Chemical identity by itself is insufficient: the same material can present materially different hazards depending on quantity, composition, concentration, pressure, temperature, phase, confinement, geometry, reaction state, connectivity, and surrounding conditions. Authoritative property sources such as NIST therefore organize safety-relevant knowledge around thermochemical and thermophysical properties rather than names alone, while DIERS practice demonstrates that reactive-system behavior and pressure relief can depend on reaction heat, gas generation, phase behavior, and two-phase flow. citeturn18search0turn18search1turn18search2turn18search6

The proposed JSEA mechanism core should therefore remain causal, but it should be implemented conceptually as a **typed causal graph rather than a literal one-way chain**. A useful canonical path is:

> hazardous inventory or energy → preconditions → initiating change → physical/chemical mechanism → unsafe state → loss of control or containment → propagation/exposure pathway → target → consequence

That structure is compatible with established process-safety reasoning: HAZOP identifies departures from intended conditions and possible consequences; Bowtie relates threats, a loss-of-control or “top” event, barriers, and consequences; and LOPA evaluates already-defined scenarios and protection layers. The proposed graph extends those practices by making thermodynamic state, rate, accumulation, topology, time, space, evidence, and counterevidence explicit. HSE explicitly notes that HAZOP identifies potential hazards but does not itself determine likelihood or loss, while CCPS LOPA guidance starts from an identified scenario and evaluates the contribution of initiating events and independent protection layers. citeturn20search0turn8search12turn8search5  
**Evidence assessment:** source types are regulator guidance and CCPS industry guidance; applicability is high for chemical/process industries; neither source prescribes the JSEA graph proposed here. **Confidence: high** for the method characteristics, **moderate-high** for the proposed synthesis. The synthesis is a researcher inference.

A purely linear chain is nevertheless insufficient for modern process systems. Feedback control, automation, human decision-making, common dependencies, organization, delayed information, and changing process models introduce cycles and interactions that are not well represented by a sequence of component failures. MIT's STPA material explicitly treats accidents as control problems and addresses unsafe control actions, feedback, and process-model flaws; STPA also allows hazardous interactions when individual components have not necessarily “failed.” HSE similarly treats the Basic Process Control System, safety instrumented systems, alarms, people, and lifecycle management as interacting parts of process functional safety rather than interchangeable safeguards. citeturn14search5turn14search7turn20search1turn20search11  
**Evidence assessment:** primary MIT STAMP/STPA material plus regulator guidance. STPA's claims about the limitations of event-chain thinking are theoretical/system-safety claims rather than evidence that HAZOP or LOPA should be discarded. **Confidence: high** that a control/feedback layer is necessary; **low confidence** in any claim that STPA should replace established process methods.

The recommended architecture is therefore **hybrid**: retain a first-principles physical/chemical mechanism graph; add a safety-constraint and control-structure layer inspired by STAMP/STPA; maintain a separate barrier/dependency layer compatible with Bowtie/LOPA; and keep evidence, uncertainty, lifecycle, and governance as explicit metadata. This architecture allows JSEA to ask both, “By what physical mechanism could this consequence occur?” and, “What control or organizational condition could permit the system to enter that hazardous state?” It avoids forcing thermodynamics into STPA terminology or forcing software/control failures into an oversimplified material-release chain. citeturn14search5turn20search1turn20search15  
**Evidence assessment:** the need for both mechanism-oriented and control-oriented reasoning is strongly grounded, but the five-layer JSEA implementation is a **researcher design recommendation**. **Confidence: high** in the hybrid direction, **moderate** in the precise decomposition until tested against a representative scenario corpus.

For inherently safer design, JSEA should **not produce a single “safety score.”** The accepted four lenses—minimize, substitute, moderate, and simplify—are intended to eliminate or reduce hazards at their source, but one option may improve one hazard while worsening another. The CCPS inherently safer alternatives checklist explicitly spans material substitution, inventory reduction, temperature and pressure moderation, complexity and connection reduction, human factors, siting, and transportation. CSB investigations provide concrete evidence that material-of-construction decisions can constitute inherently safer opportunities: following the Chevron Richmond fire, CSB identified use of more corrosion-resistant alloy as an inherently safer alternative to continued dependence on inspection of vulnerable carbon steel. citeturn5view3turn21search2turn21search6turn21search20  
**Evidence assessment:** CCPS guidance and government accident investigation. ISD comparisons remain process-specific; neither source supports universal weighting or automatic design acceptance. **Confidence: high.**

Finally, JSEA's role should remain **analysis assistance, not engineering acceptance**. The system can generate causal hypotheses, find missing evidence, detect inconsistent safeguards, compare design alternatives, and expose unresolved assumptions. It should not declare pressure relief adequate, assign SIL, approve a permit, certify ALARP, establish material compatibility, or conclude a design is safe without the engineering calculations, data, competent review, and jurisdiction-specific governance those decisions require. HSE functional-safety guidance, for example, treats hazard analysis, safety requirements, design, validation, operation, proof testing, modification, competence, and formal assessment as a lifecycle; MIT's 2024 study of LLM-assisted STPA also found that superficially plausible LLM results could contain errors difficult for human reviewers to detect. citeturn20search1turn15view1  
**Evidence assessment:** regulator guidance plus a primary MIT workshop study of one particular LLM/STPA approach. The MIT study should not be generalized quantitatively to all future AI systems; its relevance is the demonstrated possibility of plausible-looking analytical errors and reviewer overreliance. **Confidence: high** for maintaining human engineering authority; **moderate** for extrapolating the study to JSEA.

### Proposed first principles

The following thirteen axioms are recommended as the Phase 1 Safety-by-Design foundation.

| Axiom | Safety-by-Design first principle | Basis and interpretation |
|---|---|---|
| **Conservation** | **A scenario that requires unexplained creation or disappearance of mass or energy is physically incomplete.** | Material and energy balances are foundational constraints. JSEA need not solve full balances itself, but its causal graph should expose required sources, sinks, transfers, generation terms, and accumulation. Thermodynamic data and engineering models provide the required properties. citeturn18search0turn18search1 **Source:** physical science/reference data. **Limit:** conservation alone does not determine rates or realizability. **Confidence: high.** |
| **State dependence** | **Hazard depends on material plus state, not material identity alone.** | Composition, concentration, phase, temperature, pressure and inventory can change release, reaction and exposure behavior. NIST's property databases explicitly distinguish properties across fluid states and mixtures. citeturn18search1turn18search12 **Source:** NIST reference science. **Limit:** property databases do not themselves constitute hazard assessments. **Confidence: high.** |
| **Driving force** | **Transfer and loss of containment require a physically credible driving force and pathway.** | Pressure differences, concentration gradients, thermal gradients, gravity, chemical affinity, mechanical energy and related potentials govern whether material or energy can move. Geometry and boundary conditions determine how the potential is expressed. **Researcher synthesis** grounded in standard transport/thermodynamic engineering and process design practice. citeturn18search12turn20search13 **Confidence: high.** |
| **Rate and accumulation** | **“Can occur” and “can become hazardous fast enough” are different questions.** | Inflow, outflow, generation and removal rates determine accumulation; transient states can exceed safe limits even where nominal steady operation is acceptable. Reactive relief practice is a strong example because heat generation, gas generation, heat removal and venting must be evaluated dynamically. citeturn18search2turn18search6 **Limit:** specific rates require specialist models/data. **Confidence: high.** |
| **Coupling and feedback** | **Chemical kinetics, heat transfer, mass transfer and phase change can reinforce or suppress each other.** | Runaway behavior can arise when heat or gas generation outpaces removal; CCPS defines autodecomposition in terms of heat evolution exceeding heat loss, causing rising temperature and reaction rate. citeturn19view1 **Source:** CCPS technical glossary. **Limit:** mechanism and onset are substance/system-specific. **Confidence: high.** |
| **Topology** | **Connectivity and isolation state are causal properties, not drawing metadata.** | An open, leaking, bypassed or misaligned connection can create a pathway between otherwise separate inventories. The DuPont La Porte investigation illustrates the importance of a valve-connected pathway during nonroutine work that prior analyses had not effectively captured. citeturn21search3turn21search7 **Source:** CSB investigation. **Limit:** one incident illustrates the principle but does not define universal failure frequencies. **Confidence: high.** |
| **Path to loss** | **Hazardous inventory is not itself a consequence: a credible route from source to exposed target is required.** | Release source term, propagation, ignition/reaction where applicable, occupancy/receptor and exposure determine consequence. COMAH safety-report guidance likewise distinguishes dangerous-substance inventories, major-accident scenarios, triggers, consequences, neighboring receptors and mitigation. citeturn20search19 **Source:** UK jurisdiction-specific regulator guidance. **Limit:** COMAH requirements are not globally mandatory. **Confidence: high** for the physical principle. |
| **Temporal completeness** | **Startup, shutdown, cleaning, maintenance, abnormal operation and transition states must be modeled independently of normal operation when their state or topology differs.** | HSE explicitly requires operating procedures to cover normal, abnormal, temporary, emergency, commissioning, startup, shutdown and change conditions; CSB investigations repeatedly identify startup/nonroutine configurations as important. citeturn20search9turn21search1turn21search3 **Source:** regulator and accident investigations. **Confidence: high.** |
| **Constraint-based safety** | **Safety means maintaining system conditions inside defined constraints, not merely avoiding named component failures.** | STAMP/STPA frames safety around system hazards, constraints, control actions and feedback; IEC/HSE functional-safety practice similarly derives required safety functions from hazard and risk analysis. citeturn14search5turn20search1turn20search11 **Source:** primary systems-safety framework plus regulator guidance. **Limit:** safety constraints do not replace consequence modelling or PHA. **Confidence: high.** |
| **Mechanism-specific protection** | **A safeguard is relevant only if it acts on a causal transition in the scenario, with adequate capability and timing.** | CCPS IPL concepts require a protection layer to prevent scenario progression and emphasize independence and capability; alarm effectiveness likewise requires actionable and timely operator response. citeturn8search19turn8search4turn20search1 **Source:** CCPS/HSE guidance. **Limit:** qualification as an IPL requires method-specific evidence beyond semantic relevance. **Confidence: high.** |
| **Dependency explicitness** | **Independence must be demonstrated, not assumed.** | Common power, sensors, logic, utilities, communication, maintenance, environmental exposure, human actions or organizational processes can couple nominally separate protections. HSE requires risk-based utility redundancy where loss would prevent safe operation or shutdown. citeturn20search7turn20search1 **Source:** regulator guidance. **Confidence: high.** |
| **Epistemic discipline** | **Unknown is not equivalent to false, safe, impossible, or negligible.** | Missing reaction data, topology, valve state, occupancy, calibration history or model applicability should remain an evidence gap. NIST itself notes limitations and uncertainty in reference-data use, while competent hazard assessment requires an adequate process definition and chemical-reaction characterization. citeturn18search4turn20search0 **Researcher inference:** JSEA should preserve unresolved branches rather than silently close them. **Confidence: high.** |
| **Hazard reduction before dependency addition** | **Prefer eliminating or reducing the relevant hazard where practicable, but never claim improvement without checking transferred hazards over the lifecycle.** | CCPS's ISD checklist applies substitution, minimization, moderation and simplification across process, equipment, siting and transport; CSB's Chevron findings show the practical distinction between eliminating/reducing a damage mechanism through design and continually managing vulnerable equipment through inspection. citeturn5view3turn21search6turn21search20 **Limit:** ISD alternatives can create different hazards and therefore require multidimensional comparison. **Confidence: high.** |

A fourteenth rule should govern the **AI system rather than the plant**:

> **JSEA may propose, challenge and structure safety reasoning; it may not confer engineering acceptance or regulatory approval.**

This is a governance constraint rather than a physical axiom. It is justified by the lifecycle and competence requirements associated with safety functions and by evidence that AI-generated safety analyses can look plausible while containing substantive errors. citeturn20search1turn15view1 **Confidence: high.**

## Minimum safety ontology

### Epistemic categories

The ontology should distinguish what kind of knowledge a proposition represents, because an equation of state, an operator statement, a plant drawing, an empirical corrosion correlation and a legal requirement are not interchangeable evidence.

| Code | Category | Meaning for JSEA |
|---|---|---|
| **P** | Invariant physical or chemical principle | Conservation, thermodynamic relationships, causal direction imposed by physical law. These constrain credible scenarios but usually do not alone calculate them. |
| **M** | Engineering model | Deliberate abstraction such as heat balance, dispersion model, relief model, reaction model, structural model or reliability model. Valid only within assumptions and domain. |
| **E** | Empirical relationship/data | Measured material properties, kinetics, failure data, corrosion data, human-performance data and experimentally fitted correlations. |
| **C** | Contextual engineering information | Actual process composition, equipment geometry, piping topology, operating mode, valve alignment, alarm configuration, occupancy and procedures. |
| **H** | Human or organizational condition | Competence, workload, authority, communications, maintenance practices, decision processes, staffing, supervision, management of change and organizational incentives. |
| **G** | Regulatory/governance requirement | Legal duties, standards adopted by an organization, corporate criteria, approval authority and jurisdiction. These govern what must be demonstrated but are not laws of physics. |

That separation is important because HSE, for example, specifies jurisdictional COMAH duties, while NIST supplies scientific property data and IEC/CCPS supply engineering methods and standards. A JSEA assertion should preserve the category and provenance rather than presenting all three as equivalent “rules.” citeturn20search19turn18search0turn20search1

### Minimum Safety Ontology table

| Concept | Definition | Category | Principal relationships | Evidence required | Applicability limits | Example |
|---|---|---|---|---|---|---|
| **System boundary** | What equipment, activities, environment, utilities, controls, organizations and lifecycle stage are inside the analysis. | C, H | contains equipment, inventories, controllers, targets; interfaces with external systems | scope statement, PFD/P&ID, work scope, site/context information | Wrong boundaries can omit utility, neighboring-unit, transport or organizational causes. STPA likewise begins by defining purpose/system boundary. citeturn14search5 | Reactor job includes reactor, connected feed lines, nitrogen, cooling supply, control system and maintenance activity. |
| **Material identity** | Chemical species or defined material/product identity. | C, E | has composition, properties, compatibility, reaction network | SDS plus authoritative physical/property/reaction sources; assay where necessary | Commercial mixtures, impurities and decomposition products may not be represented by nominal name. NIST data coverage is substance/property specific. citeturn18search0turn18search4 | “Toluene” is insufficient if feed also contains peroxide initiator. |
| **Composition and concentration** | Relative amount of components, including contaminants, diluents, oxidants and reaction products. | C, E | determines phase, kinetics, toxicity, flammability, compatibility | sample/assay, recipe, process data, specification, credible contamination cases | Concentrations can vary spatially and temporally; average values may conceal hazardous local conditions. | Oxygen ingress changes an otherwise inert vapor-space condition. |
| **Inventory / holdup** | Mass, moles, volume or stored amount that can participate in a hazardous event. | C, P | source of mass/chemical energy; changes by flow, generation and removal | vessel dimensions, level, line holdup, batch size, mass balance | Nominal capacity is not necessarily actual or releasable inventory. ISD minimization explicitly targets raw-material, process and finished-product inventory. citeturn5view3 | Smaller intermediate vessel lowers the maximum releasable toxic inventory. |
| **Hazardous properties** | Properties capable of causing harm: toxicity, flammability, reactivity, corrosivity, instability, asphyxiation and relevant physical hazards. | E | combined with state/inventory/pathway produces hazard scenario | authoritative property data, testing, literature, compatibility data | Property values are conditional on temperature, pressure, composition and test method. citeturn18search0turn19view1 | Low flash-point solvent in an open transfer. |
| **Thermodynamic state** | Sufficient state variables to characterize relevant equilibrium/nonequilibrium condition, typically pressure, temperature, composition and phase. | P, M, C | controls vaporization, density, energy, phase change, release behavior | instruments, process data, property model/database | Equation/model validity matters, particularly mixtures, near critical regions and metastable conditions. REFPROP explicitly uses fluid/mixture-specific models. citeturn18search1turn18search20 | Liquefied gas above atmospheric boiling point can flash after depressurization. |
| **Phase and phase transition** | Solid/liquid/vapor/supercritical or multiphase condition and possible transition. | P, M, E | affects flow, expansion, heat transfer and source term | phase data, P-T-composition, validated property method | Non-equilibrium flashing, foaming and two-phase relief may need specialist modelling. DIERS exists specifically because simple single-phase assumptions can be inadequate. citeturn18search6turn18search10 | Reactive vessel vents two-phase froth rather than vapor only. |
| **Energy inventory** | Stored thermal, pressure, mechanical, chemical, electrical or gravitational energy capable of driving a hazardous transition. | P, C | couples to release, reaction, ignition, equipment failure | pressure/temperature/state, chemical reaction data, equipment configuration | “Energy” is not one interchangeable scalar for risk comparison; forms and accessibility differ. | Compressed gas possesses expansion energy even if chemically inert. |
| **Driving force** | Difference in potential capable of causing transfer or change. | P | drives mass/heat/momentum/electrical transfer | measured state, boundaries, geometry | Presence of a gradient does not establish a hazardous rate without resistance/geometry. | Vessel pressure above atmosphere drives discharge through an opening. |
| **Reaction network** | Intended and unintended chemical transformations that may occur. | C, M, E | consumes/reactants, generates products, heat and gas; changes properties | chemistry basis, calorimetry, literature, impurity/compatibility testing | Unknown side reactions are a major epistemic gap; absence from normal recipe does not prove impossibility. | Contamination initiates exothermic decomposition. |
| **Kinetics and thermal stability** | Rates of reaction/decomposition and sensitivity to temperature, composition, catalysts, confinement and time. | M, E | couples with heat generation/removal and accumulation | calorimetry, kinetic data/model, validated scale-up assumptions | Lab data require applicability assessment; reaction rates may be controlled by mixing or mass transfer as well as intrinsic kinetics. CCPS explicitly notes “apparent activation energy” can include physical processes. citeturn19view1 | Cooling loss allows reaction heat generation to accelerate faster than removal. |
| **Heat-transfer capability** | Capacity and rate for heat input/removal across the actual geometry and operating condition. | P, M, E, C | affects temperature, reaction rate, phase change | UA data/model, utilities, fouling state, agitation, temperatures | Nominal exchanger duty may not apply after loss of circulation, fouling, phase change or utility degradation. | Agitator loss reduces effective heat removal during an exothermic batch. |
| **Mass transfer / mixing** | Transfer between phases or locations and degree of compositional mixing. | P, M, E | affects reaction rate, vapor generation, dilution, exposure | mixing design, flow regime, agitation, empirical correlations/test data | Perfect-mixing assumptions can be unsafe where stratification or local concentrations matter. | Dense vapor accumulates in a low area despite acceptable room-average concentration. |
| **Containment** | Physical boundary intended to retain material/energy. | C | has design limits, material, openings, connections, degradation mechanisms | design documents, inspection, thickness, material certificates | Nominal equipment existence does not prove integrity. HSE identifies pressure, temperature, material of construction, corrosion and erosion as core design considerations. citeturn20search13 | Corroded process pipe is the boundary separating hydrocarbon from atmosphere. |
| **Geometry and capacity** | Dimensions, free volume, surface area, elevation, orientation and capacities relevant to accumulation, flow or consequence. | C, M | constrains inventory, rate, heat transfer, pressure rise, drainage and dispersion | drawings, datasheets, field verification | Simplified drawings may omit dead legs, elevations or temporary equipment. | Small vent line limits the rate at which generated gas can leave. |
| **Connectivity / topology** | Which equipment volumes and environments are connected under a specified valve, blind, bypass and hose configuration. | C | defines material/energy pathways and isolation | current P&ID, line list, valve/blind status, field verification, temporary connection records | P&IDs may not represent temporary or incorrect alignments. CSB's DuPont findings demonstrate why nonroutine valve topology matters. citeturn21search3 | Open valve connects toxic-liquid piping to a waste-gas header. |
| **Material of construction and degradation state** | Boundary material and its present resistance to corrosion, erosion, embrittlement, fatigue or other damage. | C, E, M | controls containment integrity and failure mechanisms | MOC records, service chemistry, inspection/NDE, damage-mechanism assessment | Inspection is evidence at points in time, not proof of indefinite integrity. Chevron illustrates a design choice between vulnerable carbon steel and more corrosion-resistant alloy. citeturn21search6turn21search20 | Sulfidation-thinned carbon steel piping. |
| **Operating/design envelope** | Defined range of state and operating variables for which equipment/process/control assumptions are valid. | C, M, G | safety constraints bound process state | design basis, operating limits, alarms/trips, mechanical ratings | Different limits may apply to normal, upset, startup and relief conditions; AI should not invent thresholds. | Maximum allowable vessel condition versus normal operating pressure. |
| **Time, rate and accumulation** | Temporal variables describing sequence, duration, delay, residence time, rates and accumulated quantity/energy. | P, M, C | qualifies every dynamic edge | historian data, procedural timing, kinetics, flow rates, alarm/action time | A snapshot can miss transient peaks; CCPS enabling-condition guidance recognizes “time at risk” and peak-risk periods. citeturn8search23turn8search31 | Drain closed for long enough that feed accumulates and floods a tower. |
| **Operating mode / lifecycle state** | Normal operation, startup, shutdown, batch phase, idle, cleaning, maintenance, commissioning, emergency or decommissioning. | C, H | selects applicable topology, procedures, barriers and process model | work scope, schedule, procedures, plant status | Normal-operation assumptions cannot automatically be transferred across modes. citeturn20search9turn21search1 | Startup has different level control and routing than steady operation. |
| **Precondition** | Existing state required for an initiating change to propagate through a specified mechanism. | C, P, M | enables causal edge | current process/equipment state and mechanism basis | Must not be confused with the initiating event itself. | Vessel already contains reactive charge when cooling becomes unavailable. |
| **Enabling condition** | Condition that must be present concurrently or over a relevant interval for a scenario to propagate, but is not itself the initiating cause. | C, H | enables/modifies an edge | operating mode, occupancy, weather, ignition availability etc. | In LOPA, enabling conditions have method-specific treatment and should not be double counted. CCPS explicitly describes enabling conditions as concurrent scenario requirements. citeturn8search0turn8search23 | Maintenance is performed only 5% of calendar time; the open-equipment pathway exists only during that task. |
| **Initiating change / disturbance** | Change that moves the system from one state toward a hazardous mechanism. | C, H, M | triggers state transition | historian, event records, credible-deviation analysis | “Initiating event” definitions vary by method; it should be distinguished from precondition, enabling condition and root cause. | Cooling flow stops; wrong valve opens; external fire begins. |
| **Mechanism** | Physical, chemical, biological, mechanical or control process by which one state produces another. | P, M, E | causal edge connecting states | scientific basis plus model/data appropriate to conditions | Mechanism identification does not automatically determine magnitude or frequency. | Heat generation exceeds removal → temperature rises → reaction accelerates. |
| **Unsafe/intermediate state** | State that does not yet constitute the final loss but violates or approaches a safety constraint. | C, M | result of mechanisms; precursor to loss | process variables, equipment/control state, defined constraints | Avoid equating all deviations with hazardous states; context matters. | Reactor pressure rising while relief remains closed. |
| **Loss of control / containment** | Boundary transition where intended control over hazardous material or energy is lost. | C, M | corresponds approximately to Bowtie top event; initiates propagation | mechanism analysis, boundary condition, release route | Some accidents involve loss of safe control without physical release; terminology must allow both. citeturn8search5turn14search7 | Pipe rupture releases hydrocarbon; or automation commands an unsafe reaction sequence before any release. |
| **Source term** | Rate, quantity, duration, phase, composition and conditions of material/energy entering a propagation environment. | M, E, C | input to dispersion/fire/explosion/exposure models | opening geometry, state, inventory, validated release model | Requires specialist calculation for many scenarios; JSEA should identify calculation need rather than manufacture a number. | kg/s toxic vapor release for a defined duration. |
| **Propagation pathway** | Spatial/physical route by which released material, heat, pressure, contamination or other hazardous influence reaches a target. | M, C | connects source term to exposure | site geometry, ventilation, drainage, weather, barriers, dispersion/fire models | Strongly condition-dependent; atmospheric models have explicit assumptions. citeturn19view1 | Vapor travels downwind into occupied area. |
| **Exposed target / receptor** | Person, population, asset, environment, ecosystem or critical function capable of being harmed. | C, G | receives exposure; determines consequence type | occupancy, population, asset/site/environment data | Occupancy and receptor vulnerability change with time. COMAH explicitly treats people and environment and requires consideration of surroundings. citeturn20search19 | Contractor in temporary trailer; nearby watercourse. |
| **Exposure** | Contact between hazardous agent/energy and a receptor characterized by magnitude, duration, route and location. | M, E, C | source + pathway + target → dose/load | exposure/consequence model and target data | Toxic dose, thermal radiation, overpressure, ecological effects require different models. | Worker inhales toxic plume for a defined duration. |
| **Consequence / loss** | Physical harm or unacceptable outcome resulting from exposure or loss of system function. | M, E, G | terminus of scenario; linked to STPA unacceptable loss | consequence criteria/models and stakeholder definitions | Criteria vary by jurisdiction and organization; avoid merging them into universal thresholds. | Fatality/injury, environmental damage, equipment destruction, loss of critical operation. |
| **Barrier / safeguard** | Measure intended to prevent, detect, interrupt, control or mitigate a specific causal transition or consequence. | C, M, H | acts on one or more causal edges | design basis, functionality, test/maintenance records, response time | A “safeguard” is not automatically an IPL. CCPS IPL criteria impose stronger capability/independence expectations. citeturn8search19turn8search4 | High-level trip closes feed valve before overflow. |
| **Dependency / common cause** | Shared condition capable of defeating multiple functions or barriers. | C, H, M | links barriers/controllers that otherwise appear separate | common utilities, sensors, hardware, maintenance, environment, software and procedures | Dependency strength often requires specialist reliability analysis. | Two shutdown valves depend on same instrument air header. |
| **Safety constraint** | Condition that must be maintained to prevent an identified system-level hazard. | C, G, M | constrains states/actions; enforced by controllers/barriers | hazard analysis, design basis and engineering approval | Must be specific enough to test; should not invent limits absent design basis. STPA uses safety constraints as a central construct. citeturn14search5 | “Do not permit feed while verified cooling capability is unavailable.” |
| **Controller / control action** | Human, software, automation or organizational entity that issues an action intended to control a process. | H, C, M | observes feedback, holds process model, issues action | control narrative, procedures, logic, responsibilities | “Human error” is too coarse: actions depend on context and information. HSE recommends analyzing performance-influencing factors rather than stopping at operator error. citeturn20search15turn20search17 | Operator starts pump; PLC opens valve; management authorizes continued operation. |
| **Feedback / information** | Information by which a controller estimates controlled-process state. | C, H, M | updates process model and affects actions | sensor architecture, displays, communications, alarms | Feedback may be absent, wrong, delayed or ambiguous. BP Texas City included false readings and failed alarms during tower overfill. citeturn21search5 | Level transmitter reports a falling value while actual level continues to rise. |
| **Process / mental model** | Controller's representation or belief about current system state and how actions will affect it. | H, M | interprets feedback and generates decisions | procedures, interface, training, software state/logic | Not directly observable in all cases; causal claims require evidence. MIT STPA emphasizes process-model flaws as a pathway to unsafe control. citeturn14search13turn14search17 | Operator believes tower level is low because instrument indication is misleading. |
| **Human task and performance conditions** | Required actions and contextual factors influencing whether they can be performed correctly and on time. | H | affects barrier/controller reliability | task analysis, staffing, workload, competence, interface, environment | Do not assign generic human-error probabilities without applicable data. HSE expressly warns against unsupported precise probabilities. citeturn20search15 | Operator must diagnose alarm and isolate flow within available response time. |
| **Organizational condition** | Management, resource, communication, maintenance, change and governance conditions that shape system behavior. | H | influences controllers, barriers, evidence quality and operating envelope | MOC records, maintenance backlog, audit results, roles, decisions | Must be tied to a credible mechanism; avoid vague “safety culture caused it” assertions. | Known alarm problem remains uncorrected through repeated startup. |
| **Evidence item** | Traceable observation/document/data/source supporting or challenging an assertion. | C, E, H, G | supports/contradicts node or edge | provenance, date, version, author, method | Evidence quality and relevance differ; later plant changes can make old information stale. | Current calibrated trend versus five-year-old P&ID. |
| **Uncertainty / evidence gap** | Known incompleteness in state, model, parameter, topology, causality or applicability. | M, C | annotates conclusions and may prevent closure | gap statement plus required resolution evidence | “Low confidence” is not an accident probability. | Unknown valve position prevents concluding that transfer path is isolated. |
| **Applicability domain** | Conditions under which evidence/model/standard is valid. | M, E, G | bounds every imported rule/model | source scope, assumptions, test range, jurisdiction, version | Essential to prevent extrapolating empirical correlations or legal requirements. | API/IEC/HSE provisions applied only where technically and jurisdictionally relevant. |
| **Governance requirement** | External or internal rule defining duties, criteria, competence or approval authority. | G | constrains analysis/decision process | applicable law, standard, company standard, jurisdiction and effective version | Never convert one jurisdiction's obligation into universal physical truth. COMAH, for example, is UK-specific. citeturn20search19 | Site must meet a company safety standard in addition to local legal duties. |
| **Decision authority** | Competent person/body authorized to approve engineering or work decisions. | H, G | consumes JSEA output; cannot be replaced by AI | responsibility matrix, legal/company governance | AI confidence is not engineering approval. | Process engineer approves design basis; authorized issuer controls permit issuance. |

The ontology should permit **multiple epistemic labels on one concept**. For example, “pressure” is a physical state variable, the measured value is empirical/contextual information, the allowable pressure is an engineering/governance constraint, and the predicted pressure during a runaway is a model output. Conflating those propositions is a serious category error.

## Reusable causal grammar and mechanism template

### The chain should be the canonical reading order, not the underlying data structure

The proposed causal pattern is fundamentally sound for many chemical-process scenarios, but the word **chain** should describe a human-readable projection of a richer graph.

T2 Laboratories provides a simple illustration of why the mechanism portion is valuable: loss/inadequacy of cooling was associated with rising reactor temperature and pressure, runaway reaction and vessel failure. BP Texas City shows why state, accumulation, instrumentation and exposure location must also be explicit: during startup a tower flooded, overpressurized and discharged hydrocarbons; failed or misleading indications influenced operator understanding, and workers were located close to the atmospheric vent. citeturn9search0turn21search1turn21search5  
**Source type:** CSB accident investigation. **Applicability:** illustrations of causal completeness, not universal templates or frequency data. **Confidence: high.**

A useful minimum schema is:

```text
SCENARIO :=
    SCOPE
  + HAZARD_SOURCE{1..n}
  + INITIAL_STATE
  + PRECONDITION{0..n}
  + ENABLING_CONDITION{0..n}
  + INITIATING_CHANGE{1..n}
  + MECHANISM_TRANSITION{1..n}
  + UNSAFE_STATE{1..n}
  + LOSS_OF_CONTROL_OR_CONTAINMENT{0..n}
  + PROPAGATION_PATH{0..n}
  + TARGET_EXPOSURE{0..n}
  + CONSEQUENCE{0..n}
  + SAFETY_CONSTRAINT{0..n}
  + BARRIER{0..n}
  + CONTROL_LOOP{0..n}
  + EVIDENCE_LEDGER
  + UNCERTAINTY_LEDGER
```

The `{0..n}` notation is intentional. Not every hazardous scenario requires a physical release: an unsafe control action could damage equipment directly; a worker could be exposed inside equipment; or a reaction could progress toward rupture before loss of containment has occurred. Conversely, a scenario can contain multiple release/propagation episodes.

Each **mechanism transition** should be represented conceptually as:

```text
STATE_i
  --[
      mechanism,
      required preconditions,
      enabling conditions,
      inhibiting/disconfirming conditions,
      material/energy transfer,
      rate or characteristic time,
      accumulation,
      spatial scope,
      topology required,
      applicable model,
      evidence,
      counterevidence,
      uncertainty,
      safeguards acting on this transition
    ]-->
STATE_j
```

This is a conceptual grammar, not application code.

### Essential causal links

The strongest irreducible elements are:

**A source of hazardous potential.** This can be material inventory, chemical reaction potential, pressure, thermal energy, mechanical energy, electrical energy, gravity, oxygen deficiency potential, or some combination. Without a source, a scenario lacks physical basis.

**A state and set of conditions that make the mechanism possible.** Composition, phase, T/P state, geometry, material condition and topology frequently distinguish a credible scenario from an impossible one. NIST and DIERS sources illustrate how property/state assumptions matter to physical behavior. citeturn18search1turn18search2

**A state-changing mechanism.** “Equipment failure causes incident” is too coarse. JSEA should seek the mechanism: corrosion thinning → pressure-boundary rupture; inflow greater than outflow → level accumulation → overflow; reaction heat generation greater than removal → temperature rise → faster reaction; pressure difference plus open route → discharge.

**A causal route to harm.** For consequence claims, the analysis must identify the target and how hazardous material or energy reaches it. UK COMAH guidance explicitly requires consideration of possible major-accident scenarios, triggers, consequences, surrounding environment, neighboring establishments and mitigation. citeturn20search19

Preconditions and initiating changes should remain distinct. An initiating change is the transition-driving event or action; a precondition is a state that must already exist. An enabling condition may be neither—the CCPS LOPA usage describes an enabling condition as something required for scenario propagation concurrently with the initiating event. citeturn8search0turn8search23

### Time must be first-class, not an annotation added later

Each state and transition should be capable of representing:

`time-at-state`, `transition start`, `duration`, `rate`, `delay`, `deadline`, `residence time`, `accumulation integral`, `ordering constraint`, and `time-at-risk`.

This matters because hazards can arise from **too early, too late, out-of-order, too long or stopped too soon** control actions, a distinction made explicitly in STPA's unsafe-control-action framework. citeturn14search1turn14search3

For physical mechanisms, rate competition should be made semantically visible even when JSEA cannot perform the numerical calculation:

> generation rate **versus** removal rate  
> inflow **versus** outflow  
> heat release **versus** heat removal  
> vapor generation **versus** vent capacity  
> corrosion/damage growth **versus** inspection/intervention interval  
> hazardous propagation **versus** detection/isolation/evacuation response

The AI may identify that such a comparison is required; it should not fabricate the engineering result.

### Space must also be explicit

At minimum, spatial reasoning needs:

`source location → containment boundary → release direction → local geometry/confinement → transport medium → propagation region → receptor location`.

CSB's Texas City findings show why consequence cannot be inferred from process upset alone: the location of occupied trailers relative to the vent-release point materially affected who was harmed. citeturn21search1

For environmental scenarios, the corresponding pathway might be:

`process inventory → drain/sewer → wastewater system → receiving water → ecological receptor`

rather than an atmospheric plume. JSEA therefore needs a generalized **propagation medium** concept rather than a dispersion-only model.

### Enabling and disconfirming conditions

JSEA should use three-valued evidence status for conditions:

| Condition status | Interpretation |
|---|---|
| **Supported present** | Evidence supports the condition required by the mechanism. |
| **Supported absent** | Evidence supports a condition that blocks or contradicts the causal edge. |
| **Unknown / unresolved** | Evidence is insufficient; the edge remains conditional rather than being discarded. |

A **disconfirming condition** should be represented positively: for example, “spectacle blind verified installed between A and B” is stronger than merely having no evidence that the connecting valve is open.

This directly supports the user's existing fact/hypothesis/evidence-gap distinction. It prevents a particularly hazardous AI failure mode: silently transforming **“not established” into “not present.”**

### Safeguards should attach to causal edges

A generic list of safeguards is weaker than an edge-specific representation. A safeguard should say *what transition it changes*:

| Safeguard function | Causal attachment |
|---|---|
| Eliminate source | removes hazard-source node |
| Prevent initiating change | initiation edge |
| Prevent unsafe state | mechanism edge |
| Detect developing state | state-to-controller feedback edge |
| Interrupt escalation | transition from unsafe state toward loss |
| Limit source term | loss-of-containment/release edge |
| Interrupt propagation | source-to-target pathway |
| Reduce exposure | target/exposure edge |
| Mitigate harm | exposure-to-consequence edge |

This is consistent with CCPS's concept of an IPL as a device, system or action able to prevent a scenario from progressing to an undesired consequence, while preserving the crucial distinction that not every safeguard qualifies as an independent protection layer. citeturn8search19turn8search4

Every safeguard record should carry at least:

`intended function; causal edge; required capacity; response time; availability state; bypass state; test/maintenance evidence; common dependencies; independence claim; applicability conditions; failure/degradation modes; source of performance claim`.

This prevents statements such as “alarm present” from being treated as protection without examining detection, operator interpretation, available response time, action feasibility and final-element effectiveness. HSE describes process alarms as intended to notify operators that the process is leaving its normal envelope so that corrective action can be taken, and requires both controls engineering and human-factors considerations where alarms provide risk reduction. citeturn20search1

### Evidence and causal-confidence grammar

For each node and edge, JSEA should preserve an epistemic object:

```text
ASSERTION STATUS:
  fact_observed
  documented_design_basis
  engineering_model_result
  empirical_relationship
  expert_judgment
  inferred_hypothesis
  competing_hypothesis
  disconfirming_evidence
  evidence_gap
  not_applicable

EVIDENCE ATTRIBUTES:
  provenance
  date/version
  directness
  applicability_domain
  independence
  quality/authority
  contradictory_sources
  specialist_calculation_required
  confidence
```

“Confidence” should describe **support for the assertion**, never scenario frequency unless a validated risk method has separately calculated frequency.

Recommended qualitative confidence semantics are:

**High** — direct and applicable authoritative data, verified plant evidence, or multiple independent lines of strong evidence.

**Moderate** — credible inference supported by applicable engineering knowledge but with material unresolved assumptions.

**Low** — plausible hypothesis with important data/model/topology gaps.

**Indeterminate** — no defensible conclusion can yet be made.

No numeric percentages should be attached merely because an LLM can generate them.

## Limits of linear causality and comparison with established methods

### Why linear chains fail in some accident classes

A linear event sequence works well when the central analytical problem is predominantly physical:

> valve opens → pressurized liquid escapes → flashes → vapor cloud forms → ignition → fire/explosion → exposure

It becomes less satisfactory when future system behavior depends on feedback, beliefs, controllers, interactions and repeating cycles.

**Feedback control is circular.** A sensor measures the process, a controller forms an internal representation, issues a control action, the process changes, and new feedback returns. MIT's CAST/STPA material explicitly describes this as a circular feedback-control loop rather than merely a succession of events. citeturn14search17

**The same action can be safe or unsafe depending on context and timing.** STPA distinguishes failure to provide a needed control action, provision of an unsafe action, incorrect timing/order, and actions continued too long or stopped too soon. citeturn14search1turn14search3

**Components can work as specified while the interaction is unsafe.** MIT's STPA material emphasizes that system accidents can arise from unsafe component interactions even where individual components have not necessarily failed. citeturn14search5turn14search7 This proposition is especially relevant to software-intensive systems where “failure” of a hardware component may be absent.

**Feedback can be technically functioning yet misleading or incomplete.** At BP Texas City, failed alarms and false instrument readings influenced the operator's understanding while the tower continued to overfill. citeturn21search5 The physical chain “feed → accumulation → tower flood” remains essential, but it does not explain why control did not correct the state unless information and decision loops are added.

**Dependencies defeat apparently independent lines of defense.** Common utilities, maintenance processes, sensors, software, environmental conditions, communications or human actions can defeat multiple safeguards simultaneously. HSE therefore calls for appropriate redundancy of utilities where loss would prevent continued safe operation or safe shutdown. citeturn20search7

**Human action cannot be reduced to a generic random initiator.** HSE recommends examining task design, workload, time pressure, competence, interfaces, communication and other performance-influencing factors, and explicitly warns against stopping incident investigation at “operator error.” citeturn20search15turn20search17

**Organizations issue control actions too.** Decisions about staffing, maintenance deferral, alarm policy, allowable modes, budgets, design standards and change authorization can modify plant-level constraints. STAMP/STPA's hierarchy makes those decisions analyzable as part of the control system rather than as remote “root causes.” citeturn14search5turn14search7

### Comparative role of major methods

| Method | Primary representation | What it is strong at | Important limitation for JSEA | Recommended JSEA role |
|---|---|---|---|---|
| **HAZOP** | Nodes, design intent, parameters/guide words, deviations, causes, consequences, safeguards | Structured discovery of deviations and operability/process hazards; strong interdisciplinary review mechanism. IEC 61882 standardizes guidance on application, procedure and documentation. citeturn4search3 | Conventional HAZOP does not by itself quantify likelihood or loss; results depend on scope, design information and team expertise. HSE explicitly notes this. citeturn20search0 | Keep as a scenario-discovery and challenge view; map deviations into ontology states/changes. |
| **What-if / checklist** | Questions about deviations, failures and abnormal conditions | Flexible; valuable for nonroutine activities, early design and situations not well represented by fixed guide words. CCPS recognizes it among standard hazard-evaluation methods. citeturn2search25 | Completeness depends strongly on questions, facilitator and knowledge; weak formal coverage guarantee. | Use generated What-if prompts from ontology gaps and topology/state changes, subject to human review. |
| **Bowtie** | Hazard/threats → top event → consequences with prevention and mitigation barriers | Excellent communication of pathway/barrier relationships and degradation factors. AIChE describes threats leading toward loss of control and consequences; IChemE uses Bowtie for barrier-based risk management. citeturn8search5turn17search27 | Bowtie does not intrinsically discover all hazards or capture detailed dynamics/feedback; IChemE literature notes that hazard analysis must provide the initiating hazard/scenario basis. citeturn8search2 | Generate a Bowtie projection from the richer mechanism graph; never make Bowtie the sole ontology. |
| **Fault Tree** | Deductive logical combinations leading to a top event | Strong for combinations of equipment/function failures, redundancy and explicit logical structure. CCPS includes FTA among recognized hazard/risk methods. citeturn2search25 | Static Boolean structure can obscure dynamics, sequence, feedback and changing state unless extensively extended. | Derive failure-combination views for selected top events, especially barrier dependencies. |
| **Event Tree** | Inductive branching from an initiating event through subsequent successes/failures | Clear representation of alternative post-initiator outcomes and barrier success/failure sequences. CCPS recognizes ETA as a hazard/risk-analysis method. citeturn2search25 | Branch explosion, dependencies, continuous state and feedback can be awkward; starting initiator must already be defined. | Use as scenario-outcome projection, not master causal representation. |
| **LOPA** | One scenario, initiating-event frequency, conditional factors, IPLs, consequence/frequency comparison | Disciplined simplified/order-of-magnitude analysis of whether identified protection layers provide adequate risk reduction. CCPS and IChemE characterize LOPA this way. citeturn8search12turn17search5 | Not principally a scenario-discovery or first-principles physical model; results depend on correct scenario definition, valid frequencies, enabling conditions and genuine IPL independence. | JSEA may prepare a structured candidate LOPA scenario and challenge IPL relevance/dependency; competent practitioners retain calculations/acceptance. |
| **STAMP/STPA** | Losses, system hazards, safety constraints, hierarchical control structure, unsafe control actions, causal scenarios | Captures software, humans, organization, feedback, timing, unsafe interactions and process-model flaws. citeturn14search5turn14search7 | Not a thermodynamic, reaction, release, dispersion or quantitative-risk model; method quality still depends on competent system definition and analysis. | Add as a control/constraint layer over the mechanism graph; do not replace chemical/process PHA. |

### Important disagreements among the frameworks

**Event causality versus control theory.** STAMP critiques treating all accidents as chains of failed components, particularly in complex software/human systems. Conventional process-safety methods remain highly effective for identifying material/energy deviations and physical release scenarios. The appropriate conclusion is not “one is correct and the other obsolete”; it is that they resolve different classes of causal question. citeturn14search5turn20search0  
**Researcher conclusion:** JSEA should preserve both representations. **Confidence: high.**

**Meaning of “hazard.”** In chemical-process practice, a hazard often refers to intrinsic material/energy potential or a hazardous situation. STPA defines system-level hazards relative to unacceptable losses and system state/constraints. These concepts overlap but are not synonymous. JSEA should therefore use distinct terms: **hazard source**, **system hazard/unsafe state**, and **loss**. citeturn14search5turn19view1  
**Confidence: high** that terminological separation will reduce ambiguity.

**“Safeguard,” “barrier,” and “IPL.”** A safeguard recorded in HAZOP can be relevant without meeting LOPA's stricter IPL independence/performance requirements. JSEA must not upgrade a listed safeguard to an IPL merely because its name sounds protective. citeturn8search19turn8search4  
**Confidence: high.**

**Qualitative discovery versus quantitative risk.** HAZOP is fundamentally a structured hazard-identification method; LOPA adds simplified quantitative/order-of-magnitude risk reasoning; STPA primarily identifies unsafe control and causal scenarios rather than producing accident frequencies. HSE explicitly distinguishes hazard identification from subsequent likelihood/risk analysis. citeturn20search0turn17search5  
**Confidence: high.**

**Inherent safety versus passive protection.** “Passive” is not automatically “inherent.” A dike or blast wall may require no actuation but still manages a hazard that remains present, whereas reducing hazardous inventory changes the hazard source itself. The CCPS ISD checklist includes passive/design choices within a broader design review, so JSEA should preserve both dimensions rather than equating them. citeturn5view3  
**Confidence: high** as a conceptual distinction.

**Ordering of ISD principles.** Literature and guidance do not always list minimize and substitute in the same order; IChemE material also shows variants such as “eliminate” in the terminology. citeturn17search0 The four terms should therefore be treated as **design lenses, not a rigid priority algorithm**. Eliminating a hazardous chemistry entirely may clearly dominate inventory reduction of the same chemistry, but real alternatives often trade toxicity, flammability, pressure, complexity, waste and lifecycle exposure against one another. **Researcher inference, confidence: high.**

### Conclusion on linear causality

JSEA should **retain the causal chain as its mechanism core, but never constrain the underlying representation to a chain**.

The master representation should be a **directed, typed, cyclic multigraph** capable of containing:

- repeated state/mechanism sequences;
- feedback loops;
- multiple simultaneous initiating conditions;
- common-cause links;
- dependent barriers;
- control and feedback links;
- temporal ordering and delays;
- spatial propagation;
- competing hypotheses;
- alternative scenario branches.

A “chain” can then be rendered for human review as one path through that graph.

## Recommended hybrid architecture for JSEA

### The architecture

The recommended JSEA Safety-by-Design architecture contains five logically separate layers.

| Layer | Purpose | Principal objects | Why separate it |
|---|---|---|---|
| **Physical and chemical mechanism layer** | Establish whether a hazardous transition has a credible material/energy basis. | inventory, state, phase, reaction, energy, transport, geometry, topology, accumulation, release, propagation | Prevents high-level safety language from bypassing physics. |
| **Barrier and dependency layer** | Show exactly where safeguards intervene and what they depend on. | preventive/mitigative barriers, detection, isolation, relief, passive features, active systems, procedural actions, dependencies | Supports Bowtie/LOPA-style challenge without falsely granting IPL status. |
| **Safety-constraint and control layer** | Explain unsafe behavior arising from control, feedback, timing, software, humans and organization. | controllers, control actions, feedback, process models, constraints, UCAs, organizational controllers | Covers accident mechanisms that linear component-failure chains miss. |
| **Evidence and model-validity layer** | Make every inference auditable. | source, fact, hypothesis, counterevidence, model, assumptions, applicability, gap, confidence | Prevents unsupported certainty and enables targeted engineering follow-up. |
| **Lifecycle and design-comparison layer** | Compare alternatives and identify risk transfer across operating states and locations. | ISD principle, hazard-specific change, inventory/energy, dependencies, lifecycle stages, new hazards, risk transfers | Prevents “safer” from becoming a single-score or one-stage assertion. |

Governance and approval authority should cut across all five layers as a **non-bypassable boundary condition**, not as a sixth engineering-analysis layer.

### Safety constraints JSEA should enforce on its own reasoning

The following are not plant design requirements; they are proposed constraints on JSEA's analysis behavior.

**No consequence without a pathway.** A consequence claim must identify source, relevant state, propagation/exposure mechanism and target, or be explicitly labelled a hypothesis requiring calculation.

**No safeguard credit without edge relevance.** JSEA should identify the specific causal transition a safeguard acts upon.

**No independence by naming.** Two protections are not independent merely because they have different equipment tags or technologies.

**No absence from absence of evidence.** Unknown conditions remain unknown.

**No model without applicability metadata.** Any correlation, property model, failure-rate source or consequence model should retain its valid domain.

**No steady-state inheritance across a transient without justification.** Startup, shutdown, maintenance and other transient modes must inherit only those assumptions shown to remain valid.

**No generic “operator error” terminal cause.** Human actions should be linked to task, feedback, interface, timing and performance-influencing conditions where relevant. HSE strongly supports this approach. citeturn20search15turn20search17

**No legal universalization.** A requirement from COMAH, OSHA/EPA, API adoption, a corporate standard, or another authority must retain its jurisdiction/contractual status. COMAH's requirements, for example, are UK-specific even where the underlying engineering ideas are broadly useful. citeturn20search19

**No automatic engineering acceptance from AI analysis.** Relief design, SIL assignment, materials qualification, dispersion/consequence calculations, structural adequacy and similar determinations remain specialist engineering activities.

### Proposed workflow

JSEA's analysis cycle should conceptually be:

`establish scope → reconstruct actual state → identify hazardous sources → generate state-changing deviations → construct mechanisms → test conditions → map loss/exposure pathways → identify constraints → map barriers → analyze dependencies/control loops → identify evidence gaps → compare alternatives → route unresolved engineering questions to competent reviewers`

This should be **iterative**, not one pass.

For example, discovering that a candidate barrier depends on instrument air may add a new scenario involving utility loss; discovering a reaction instability may create a requirement to examine relief design; discovering a temporary hose may change the topology and therefore invalidate a previous isolation conclusion.

### Recommended “engineering calculation required” boundary

JSEA should recognize, formulate and route specialist questions such as:

- What is the credible heat-generation rate and adiabatic temperature/pressure trajectory?
- Is the proposed relief system adequate for the applicable single- or two-phase scenario?
- What is the credible release source term?
- What are the dispersion, fire, explosion or toxic-exposure consequences?
- Is a structural/mechanical component fit for the specified loading and degradation?
- Is the proposed safety instrumented function adequate and what SIL, if any, is required?
- Are two candidate protection layers sufficiently independent?
- What is the material compatibility/corrosion rate for the actual contaminants and conditions?

DIERS's body of work illustrates why reactive relief cannot responsibly be reduced to a linguistic AI inference: reactive relief design can require explicit modeling of heat release, noncondensable gas generation, two-phase flow and effluent handling. citeturn18search2turn18search6turn18search10

### JSEA-specific AI governance

MIT's 2024 experiment using ChatGPT for STPA is directly relevant as a warning, though not as a universal benchmark. In that experiment, expert review required repeated corrections; the authors found plausible-looking errors, difficulty detecting some mistakes, and potential unsafe control actions in which a facilitator accepts incorrect or incomplete AI output. They explicitly describe the tested model as simplified and incomplete and caution against assuming that human supervision automatically removes AI weaknesses. citeturn15view1

JSEA should therefore treat the human reviewer not merely as a final **“approve” button**, but as a controller who needs usable feedback. The interface should expose:

`what JSEA concluded; why; which evidence supports it; what evidence opposes it; what assumptions are necessary; which calculation it did not perform; what would falsify the scenario; what changed since the last review`.

That design is a **researcher inference** from STPA principles and the MIT LLM study. **Confidence: high** that transparency is preferable to opaque recommendation; **moderate** on the optimum interface until human-factors testing is performed.

## Multi-dimensional inherently safer design comparison and lifecycle risk transfer

### ISD should answer a hazard-specific question

The foundational question is not:

> “Which alternative has the highest safety score?”

It is:

> **“For each relevant hazard and lifecycle stage, how does Alternative B change the hazardous source, state, mechanism, pathway, target exposure and dependence on protective functions relative to Alternative A?”**

The CCPS ISD alternatives checklist supports a broad view. It asks designers to consider substituting less hazardous materials, reducing raw-material/in-process/product inventories, using milder temperature/pressure/concentration conditions, simplifying piping and connections, avoiding cross-connections and common-cause vulnerabilities, improving human interfaces, and considering siting and transportation. citeturn5view3  
**Source:** CCPS/AIChE industry guidance. **Applicability:** design-review prompts, not a quantitative acceptance method. **Confidence: high.**

### The four ISD lenses

| Lens | Core question | Strongest claim JSEA may make | What must be checked |
|---|---|---|---|
| **Minimize** | Can the quantity of hazardous material or accessible energy be reduced? | “This alternative lowers maximum or typical hazardous inventory for hazard X under conditions Y.” | increased throughput frequency, smaller equipment at harsher conditions, faster kinetics, more connections, transport/storage shifts, control sensitivity |
| **Substitute** | Can the hazardous material, chemistry, equipment/material choice or process route be replaced by one with less severe relevant hazards? | “Hazard X is eliminated/reduced by substituting A with B.” | hazards introduced by B: flammability, toxicity, reactivity, corrosion, pressure, waste, supply-chain exposure, decomposition products |
| **Moderate** | Can hazardous conditions or physical form be made less severe? | “The consequence-driving condition is reduced from state A to state B.” | refrigeration/heating dependencies, phase changes after loss of control, energy efficiency, material compatibility, new operating margins |
| **Simplify** | Can equipment, topology, tasks or operating logic be made easier to understand and harder to misconfigure? | “The alternative removes specified connections/actions/dependencies that enable scenario X.” | loss of flexibility, recovery capability, maintainability, diagnostic information, hidden complexity moved into software |

A design should not receive an ISD label merely because it uses one of these words. The claim must specify the **hazard changed** and the **mechanism of improvement**.

### Proposed multidimensional comparison dossier

Each pair of alternatives should receive a side-by-side dossier rather than an aggregate score.

| Comparison dimension | Required question | Preferred evidence/output |
|---|---|---|
| **Hazard identity** | Which exact hazard is being reduced—acute toxicity, runaway, flammability, pressure, corrosion, environmental persistence, confined-space exposure, etc.? | named hazard + causal mechanism |
| **Hazard elimination status** | Is the source eliminated, reduced, moderated, or merely better controlled? | categorical classification with justification |
| **Maximum hazardous inventory** | What maximum credible quantity can participate in the scenario? | verified/design inventory; specialist balance where needed |
| **Typical hazardous inventory** | Does normal holdup materially differ even if maximum remains similar? | inventory comparison |
| **Accessible energy** | Does stored pressure, reaction energy, thermal or mechanical energy change? | physical basis; engineering calculation where necessary |
| **Severity of process conditions** | Do T, P, concentration, phase or oxygen/oxidizer conditions become more or less severe? | state comparison |
| **Reaction stability** | Do kinetics, heat removal, mixing sensitivity or runaway potential change? | calorimetry/kinetics/model evidence |
| **Containment robustness** | Does the design remove or reduce a credible degradation/failure mechanism? | materials/design/inspection evidence |
| **Equipment/topology complexity** | Are equipment count, interconnections, cross-connections, dead legs, valves, flanges, temporary connections or alignment opportunities reduced? | topology comparison |
| **Control complexity** | Are control modes, software states, interlocks, bypasses and operator actions simplified or made more complex? | control narrative/control structure |
| **Passive dependency** | What protection is provided without detection, power or action? | barrier-function mapping |
| **Active dependency** | What sensors, logic, actuators, utilities or proof tests are newly required? | dependency model |
| **Procedural dependency** | What safety-critical manual actions, procedures or administrative controls are required? | task analysis |
| **PPE dependency** | Does residual exposure become increasingly dependent on personal protection? | exposure/task assessment |
| **Common-cause vulnerability** | Do apparently separate protections share utility, sensor, software, maintenance, location or organization? | dependency graph |
| **Operability** | Does the design reduce or increase abnormal states, narrow operating windows and need for intervention? | operating-mode analysis |
| **Maintainability** | Does maintenance require more opening, breaking containment, confined-space entry or complex isolation? | maintenance task review |
| **Detectability/recoverability** | Does simplification remove useful feedback or diagnostic capability? | HMI/control analysis |
| **Startup/shutdown** | Are new transient hazards or temporary configurations introduced? | transient scenario analysis |
| **Cleaning/decontamination** | Are more hazardous chemicals, temperatures, pressure or entries required? | lifecycle task comparison |
| **Transport** | Is risk moved to/from road, rail, marine, pipeline or onsite transfer? | quantity/form/route/frequency analysis |
| **Storage** | Is onsite inventory reduced but supplier/offsite/warehouse inventory increased? | system-boundary inventory |
| **Waste/emissions** | Does substitution or moderation change hazardous waste, effluent, flare/vent loads or persistent pollutants? | material/environmental balance |
| **Occupational exposure** | Does routine or maintenance exposure change? | task/exposure pathways |
| **Off-site exposure** | Does source term, siting or propagation toward public receptors change? | site/consequence assessment |
| **Emergency response burden** | Does the alternative require more difficult firefighting, neutralization, evacuation or rescue? | emergency scenario review |
| **Decommissioning** | Does end-of-life create residues, contaminated equipment or disposal hazards? | decommissioning plan |
| **New hazards** | What did the alternative introduce that was absent before? | new causal scenarios |
| **Risk transfer** | Which hazard/person/location/lifecycle stage receives increased exposure as another decreases? | explicit transfer statement |
| **Evidence maturity** | Is the alternative mature and characterized, or dependent on extrapolation/pilot data? | evidence-quality rating |
| **Uncertainty** | Which material conclusions remain model/data sensitive? | uncertainty register |
| **Governance constraints** | Are there jurisdictional, standard or corporate requirements relevant to either option? | jurisdiction-tagged requirement set |

### No single score

A weighted index can conceal precisely the information Safety by Design is meant to expose. For example:

- lower toxicity can accompany higher flammability;
- lower inventory can accompany higher delivery frequency;
- lower pressure can require refrigeration whose failure changes phase behavior;
- fewer manual valves can mean greater software/control dependence;
- process intensification can lower holdup while increasing reaction and transfer rates;
- substitution can reduce worker hazard but increase persistent environmental waste.

IChemE notes both inherent-safety benefits from process intensification through reduced inventory and the need to assess wider implications of major process changes. citeturn17search4

The recommended decision representation is therefore:

**Dominance:** Alternative B is demonstrably no worse on all material safety dimensions and better on at least one.

**Tradeoff:** Alternative B improves specified dimensions while worsening others; competent decision makers must resolve the tradeoff.

**Indeterminate:** available evidence cannot reliably establish which alternative is safer.

**Constraint failure:** an alternative violates a non-negotiable engineering, legal or organizational requirement and cannot be selected without redesign.

This is a **researcher-proposed decision framework**, not a CCPS scoring system. **Confidence: moderate-high**; it should be tested against real design-change cases.

### Lifecycle risk-transfer checklist

A credible ISD assessment should run each proposed change through the following lifecycle matrix.

| Lifecycle stage | Risk-transfer questions |
|---|---|
| **Raw-material production and supply** | Did substitution move acute or environmental hazard upstream? Is the alternative more unstable, scarce, contaminated or difficult to quality-control? |
| **Transportation and receipt** | Did smaller onsite inventory require more deliveries? Did physical form, pressure or route change? Are unloading connections/tasks more hazardous? |
| **Onsite storage** | Did process minimization simply move inventory into storage? Did segregation, temperature control or incompatibility requirements change? |
| **Normal operation** | What source hazards, process states, energies and dependencies changed? |
| **Startup and commissioning** | Are control modes, inventories, bypasses, vent paths or manual actions different before steady state? BP Texas City demonstrates the importance of startup-specific analysis. citeturn21search1turn21search5 |
| **Shutdown and emergency shutdown** | Can the alternative reach a stable safe state following loss of power, cooling, instrument air or feed isolation? HSE specifically ties utility reliability to safe continuation/shutdown. citeturn20search7 |
| **Cleaning and decontamination** | Are hazardous cleaning chemicals, steam, oxidants, confined spaces, residues or reaction incompatibilities introduced? |
| **Inspection and maintenance** | Does the design require more line breaking, bypassing, temporary connections, lifting, entry or intrusive inspection? |
| **Troubleshooting/nonroutine operation** | What topologies exist only during abnormal work? CSB's DuPont findings demonstrate how a nonroutine valve configuration can create an overlooked release pathway. citeturn21search3 |
| **Waste treatment** | Does substitution create hazardous aqueous, gaseous or solid wastes that were previously absent? |
| **Emission control and relief disposal** | Does the alternative change flare, scrubber, relief-header or containment loads? |
| **Emergency response** | Is fire, toxic release, runaway or spill response more difficult even if incident likelihood is reduced? |
| **Off-site/community interface** | Has inventory, source term, siting, transport route or receptor proximity changed? CCPS's checklist expressly considers siting and transportation. citeturn5view3 |
| **Decommissioning/demolition** | What trapped inventories, contamination, reactive residues, insulation, catalysts or waste streams remain at end of life? |
| **Post-closure/environment** | Are persistent contamination or long-duration environmental liabilities introduced or reduced? |

### Worked conceptual comparison without calculation

Consider replacing a large batch of a highly hazardous intermediate with continuous generation-and-consumption of a much smaller holdup.

A poor assessment says: **“Alternative B is inherently safer because inventory is 90% lower.”**

A proper JSEA comparison would instead conclude conditionally:

> Alternative B strongly supports the **minimize** principle for the specified intermediate because its in-process holdup is reduced. This can reduce the maximum quantity available for selected loss-of-containment scenarios. However, the overall Safety-by-Design conclusion remains conditional on whether the continuous process introduces higher pressure/temperature, faster reaction dynamics, narrower control margins, more complex automation, additional feed connections, startup/shutdown states, or increased upstream storage and delivery. CCPS recognizes inventory minimization as an ISD strategy, while IChemE notes that process intensification can improve inherent safety through minimized inventory but requires assessment of wider implications. citeturn5view3turn17search4

That is the level of claim JSEA should make: **specific, directional, evidence-qualified, and hazard bounded.**

## Open research questions and project recommendations

### Open questions and unresolved research gaps

**Ontology granularity.** The proposed ontology is sufficient for first-principles scenario construction, but Phase 2 must determine how fine-grained its classes should be. A valve can be represented simply as a topology state or richly as a controller/actuator/containment element with failure modes. Excessive granularity will make authoring and validation impractical; insufficient granularity will hide causal mechanisms. **Research gap; confidence: high that empirical prototyping is necessary.**

**Formal distinction between physical causality and evidential causality.** “A caused B” and “document X supports the proposition that A caused B” need separate graph semantics. Otherwise citations can accidentally become causal nodes. This is primarily an ontology-engineering problem rather than one settled by process-safety standards.

**Dynamic state representation.** Chemical processes are continuous-variable systems, whereas most safety-analysis artifacts are discrete. Phase 2 must decide how JSEA represents transitions such as “temperature is increasing” without pretending to be a dynamic simulator. A promising solution is qualitative state predicates plus explicit requirements for specialist calculation where threshold crossing depends quantitatively on rates. **Researcher proposal.**

**Mixture and reaction uncertainty.** Property databases provide high-quality information where compounds/models exist, but real streams contain mixtures, contaminants and unknown side reactions. NIST itself bounds its databases by available data and models; DIERS practice demonstrates that reactive systems often require experimental characterization. citeturn18search0turn18search2 **Confidence: high** that missing chemistry data must be a first-class gap.

**Formal treatment of dependency.** LOPA's requirement for IPL independence is clear conceptually, but practical dependencies can be partial, conditional and organizational. JSEA needs a representation that can flag shared dependencies without attempting unsupported numerical common-cause quantification. citeturn8search19turn20search7

**Integration of STPA with HAZOP without duplication.** Both can generate large sets of scenarios. Research is needed to determine which HAZOP deviations should automatically trigger control-structure analysis and which STPA UCAs need physical mechanism expansion. The objective should be complementary coverage, not duplicate worksheets.

**Environmental ontology.** Acute process-safety models tend to emphasize loss of containment, fire/explosion and acute toxic exposure. Environmental consequences may involve drainage networks, soil transport, water bodies, persistence, bioaccumulation or delayed harm and require an extended propagation/receptor ontology. COMAH's equal concern for major-accident harm to people and environment supports retaining environmental receptors explicitly, but does not solve the modeling problem. citeturn20search19

**Chronic occupational exposure.** A JSEA system centered on major accident scenarios could underrepresent repeated low-level exposure. Source, pathway, target and cumulative dose concepts need extension if occupational hygiene is in scope.

**Human/organizational evidence quality.** STPA and HSE both support richer analysis of control and human conditions, but causal assertions about motives, mental models or organizational culture can easily exceed evidence. citeturn14search17turn20search15 JSEA should prefer observable control actions, communications, resource conditions and documented decisions before attributing psychological states.

**Automatic scenario-generation completeness.** There is no evidence that an AI can prove that all credible process scenarios have been generated. JSEA should therefore report coverage relative to ontology dimensions and source documents—not “100% hazard completeness.”

**Confidence calibration for AI reasoning.** Language-model verbal confidence is not an engineering uncertainty model. MIT's 2024 STPA/LLM study raises a concrete concern about confidently presented incorrect output. citeturn15view1 Phase 2 should test whether evidence-structured confidence categories correlate with specialist review outcomes.

**Versioned applicability.** Process states, drawings, procedures, standards and legal requirements change. JSEA needs temporal provenance so an inference based on an old P&ID cannot silently survive a later modification. CCPS Process Knowledge Management and HSE management-of-change practices support maintaining accurate process knowledge and reassessing changes. citeturn2search12turn20search0

### Recommendations for the JSEA project

**Adopt the ontology before expanding the hazard library.** Scenario labels such as “toxic release,” “runaway” or “fire” should be outputs/classifications of causal reasoning, not substitutes for it.

**Represent the master safety model as a typed graph.** Human-readable chains, Bowties, STPA control structures and LOPA candidate worksheets should be **views generated from the same underlying scenario/evidence objects**, not independent truth stores.

**Make process state explicit.** Every scenario should identify operating mode, material state, topology, time basis and boundary conditions. A scenario without them should automatically be marked underspecified.

**Make topology executable as reasoning, not calculation.** JSEA should be able to infer that two inventories are connected through a stated route, identify unknown isolation states, and challenge assumptions, without calculating hydraulic flow.

**Separate “mechanism plausible” from “magnitude adequate.”** JSEA can infer that pressure differential through an open path can cause release; determining the source term can require a specialist calculation.

**Separate safeguards from IPLs.** Default to “candidate safeguard.” Granting IPL treatment belongs to the applicable risk method and requires documented capability, independence, availability/testing and scenario-specific applicability. citeturn8search19turn8search4

**Add STPA selectively.** Trigger control-structure analysis where safety depends materially on automation, operator action, software state, feedback, sequencing, communication, organizational authorization or interacting safeguards. There is no need to construct a full STPA model for every simple mechanical hazard.

**Require an explicit disconfirmation pass.** After constructing a scenario, JSEA should ask: *What verified facts would break each causal edge? Are any of those facts available?* This counteracts confirmation bias and distinguishes evidence gaps from supporting evidence.

**Require a common-cause pass.** For each cluster of safeguards, JSEA should inspect shared sensing, utility, logic, actuator, location, maintenance, testing, human response and organizational dependencies.

**Treat transients as separate configurations.** Startup, shutdown, cleaning, maintenance and decommissioning should instantiate their own process-state/topology snapshots whenever those differ materially from normal operation. HSE explicitly identifies these operating modes in procedure requirements. citeturn20search9

**Use incident cases for ontology validation, not for universal statistics.** T2, BP Texas City, Chevron Richmond and DuPont La Porte cover different missing dimensions—reaction/runaway, accumulation/feedback/exposure, material degradation/ISD and nonroutine topology. citeturn9search0turn21search1turn21search6turn21search3 They should serve as regression cases for whether the ontology can reconstruct known causal features, not as sources of universal incident ratios.

**Do not build a universal ISD score.** Build an alternative-comparison matrix and allow Pareto dominance, tradeoff and indeterminate outcomes.

**Preserve engineering authority in the data model itself.** Each analysis should contain fields such as `requires specialist calculation`, `requires field verification`, `requires competent-person decision`, and `jurisdictional determination required`. Those should not be dismissible by a generated narrative.

**Validate JSEA prospectively against expert teams.** Retrospective incident reconstruction demonstrates representational capability, not prospective hazard-identification performance. Phase 2/3 testing should compare JSEA-assisted and expert-only analyses for scenario discovery, false positives, omitted dependencies, evidence quality, reviewer workload and susceptibility to automation bias. MIT's LLM/STPA experience makes this particularly important. citeturn15view1

## Phase 2 Handoff Package

### Accepted first principles

The recommended Phase 1 baseline for Phase 2 is:

1. **Mass and energy must be accounted for.**
2. **Hazard is state-dependent; material name alone is insufficient.**
3. **A credible transfer/release mechanism requires a driving force and pathway.**
4. **Rates, duration, sequence and accumulation are safety variables.**
5. **Reaction kinetics, heat transfer, mass transfer and phase behavior can form reinforcing feedback.**
6. **Equipment geometry, containment condition and connectivity/topology are causal properties.**
7. **A consequence requires a credible source-to-target pathway.**
8. **Transient and lifecycle states must be represented when they differ from normal operation.**
9. **Safety should be expressed partly as system constraints, not only failure events.**
10. **Safeguards are meaningful only relative to specific causal transitions and required timing/capability.**
11. **Protection-layer independence and common dependencies must be explicitly examined.**
12. **Unknown evidence remains unknown and must not be interpreted as safe.**
13. **ISD claims must identify the hazard reduced and check lifecycle/risk transfer.**
14. **JSEA's analysis is advisory; engineering acceptance and authorization remain human/governance functions.**

These principles are a synthesis of physical science, CCPS/DIERS process-safety practice, HSE/IEC functional-safety principles, CSB accident evidence and STAMP/STPA systems theory. citeturn18search0turn18search6turn20search1turn14search5turn21search1 The precise formulation is **researcher-proposed**, even where its foundations are authoritative.

### Ontology definitions to freeze for Phase 2

The following terms should be treated as controlled vocabulary:

| Term | Phase 2 canonical meaning |
|---|---|
| **Hazard source** | Material, energy or condition possessing potential to cause harm. |
| **Process state** | Relevant values of composition, inventory, T/P, phase, equipment/control state and operating mode at a specified time. |
| **Precondition** | State that must already be present for a causal mechanism to proceed. |
| **Enabling condition** | Concurrent/contextual condition necessary for scenario propagation but not itself the initiating change. |
| **Initiating change** | State-changing event/action/disturbance that begins or advances the scenario. |
| **Mechanism** | Physical, chemical, mechanical or control process linking states. |
| **Unsafe state** | State violating or threatening an identified safety constraint. |
| **Loss of control** | Inability of intended controls to keep the system within required safety constraints. |
| **Loss of containment** | Breach/open pathway through which material escapes its intended boundary. |
| **Source term** | Characterization of material/energy released into the propagation environment. |
| **Propagation pathway** | Physical/spatial route from source to target. |
| **Target/receptor** | Person, population, asset, environment or function capable of loss. |
| **Exposure** | Interaction between hazardous agent/energy and target. |
| **Consequence** | Physical outcome of the scenario. |
| **Loss** | Stakeholder-defined unacceptable outcome; broader than physical consequence if necessary. |
| **Safeguard** | Candidate preventive or mitigative measure acting on a specific causal transition. |
| **IPL** | Safeguard that meets the applicable LOPA methodology's criteria for an independent protection layer; never assigned merely by name. citeturn8search19 |
| **Safety constraint** | Condition/action restriction that must be maintained to prevent a defined hazard/loss. |
| **Controller** | Human, automated, software or organizational agent issuing control actions. |
| **Control action** | Observable action/non-action through which a controller affects a controlled process. |
| **Feedback** | Information supplied to a controller about process/system state. |
| **Process model** | Controller's internal representation of controlled-process state relevant to its decision. |
| **Dependency** | Shared condition through which behavior/failure of one function is not independent of another. |
| **Evidence gap** | Information required to resolve a causal/model/applicability question but not presently established. |
| **Disconfirming evidence** | Evidence supporting the absence of a required condition or contradicting a causal assertion. |
| **Applicability domain** | Conditions under which evidence/model/rule may legitimately be used. |

### Causal grammar to freeze for prototyping

The Phase 2 master representation should be:

```text
HazardSource
    + InitialState
    + [Preconditions]
    + [EnablingConditions]
    + InitiatingChange
    -> MechanismTransition
    -> StateChange
    -> [Further MechanismTransitions / feedback]
    -> UnsafeState
    -> [LossOfControl and/or LossOfContainment]
    -> [SourceTerm]
    -> [PropagationPath]
    -> [Exposure]
    -> [Consequence / Loss]
```

Every transition must support:

```text
time
rate
duration
accumulation
spatial scope
required topology
required state
enablers
inhibitors/disconfirmers
barriers
dependencies
model required
evidence
counterevidence
uncertainty
applicability
confidence
```

Every scenario may branch and loop. A linear rendering is only a selected path through the graph.

### Proposed Phase 2 safety constraints

The JSEA reasoning engine should be tested against these constraints:

| ID | Proposed constraint |
|---|---|
| **SC-PHY** | Do not assert a physical transition without an identified mechanism and required state/conditions. |
| **SC-ME** | Do not implicitly create or destroy required mass/energy. |
| **SC-STATE** | Do not transfer conclusions between materially different process states without an applicability justification. |
| **SC-TIME** | Do not declare a protection relevant where its response/action time has not been shown compatible with the hazardous transition time. |
| **SC-PATH** | Do not assert exposure/consequence without a source-to-target pathway or label it as unresolved/model-dependent. |
| **SC-BAR** | Do not treat a safeguard as generic scenario credit; attach it to the causal edge it controls. |
| **SC-IPL** | Do not describe a safeguard as an IPL unless applicable method-specific independence and performance evidence is supplied. |
| **SC-DEP** | Search explicitly for common sensing, utilities, actuation, software, maintenance, location and human/organizational dependencies. |
| **SC-EVID** | Absence of evidence shall remain unknown rather than being converted to absence of hazard. |
| **SC-DISC** | Seek and display evidence capable of disproving each material causal edge. |
| **SC-MODE** | Treat startup, shutdown, cleaning, maintenance, abnormal and decommissioning configurations independently where state/topology differs. |
| **SC-HUM** | Do not terminate causal analysis at generic “operator error”; analyze available action, feedback, context and performance conditions where material. citeturn20search15 |
| **SC-AUTO** | For safety-critical automation, examine unsafe control action, timing/order, feedback and process-model adequacy. citeturn14search3turn14search5 |
| **SC-ISD** | Do not call an alternative “safer” without naming the improved hazard dimension and checking introduced/transferred hazards. |
| **SC-JUR** | Preserve jurisdiction and effective scope on every regulatory assertion. |
| **SC-AUTH** | JSEA shall not issue permits, certify engineering adequacy, assign acceptance, or replace competent engineering calculations. |

### ISD comparison dimensions to freeze

Phase 2 should retain, at minimum:

`hazard eliminated/reduced; hazardous inventory; accessible energy; T/P/concentration/phase severity; reaction stability; material compatibility/degradation; containment robustness; physical topology complexity; control/software complexity; passive dependency; active dependency; procedural dependency; PPE dependency; common cause; operability; maintainability; startup/shutdown; cleaning; maintenance/isolation; transport; storage; waste/emissions; occupational exposure; environmental exposure; off-site impact; emergency response; decommissioning; newly introduced hazards; risk transfer; evidence maturity; uncertainty`.

These dimensions should remain independent. No default aggregate weighting should be introduced.

### Unresolved assumptions to carry into Phase 2

**The proposed ontology is “minimum sufficient,” not proven minimal.** Validation may show that some classes can be combined or that additional classes—electrostatic state, ignition-source ontology, structural integrity, biological processes, chronic exposure—need explicit representation.

**Qualitative state reasoning may be sufficient for scenario discovery but not scenario dismissal.** This needs validation.

**A single generic mechanism grammar may not capture every specialty.** Dust explosions, electrochemistry, polymerization, high-energy systems, cryogenics and biological processes may require specialized extensions.

**Barrier-edge mapping may become many-to-many.** A relief system, for example, can affect pressure, containment failure and release disposition simultaneously.

**The boundary between “precondition” and “enabling condition” will require strict examples.** LOPA terminology should not be imported into all analyses without preserving its method-specific meaning. citeturn8search0

**STPA depth should be risk- and complexity-proportionate.** Full control structures for every routine task could overwhelm the benefit.

**Confidence labels require calibration.** “High/moderate/low” should initially represent evidence support, not calibrated probabilities, and should later be compared with specialist judgments.

**Human approval does not by itself guarantee safety.** Human-review interfaces and workload must be designed so that evidence gaps and AI uncertainty are salient; MIT's LLM/STPA study provides a reason to treat superficial human review as a potential unsafe control condition rather than a sufficient safeguard. citeturn15view1

### Terms requiring consistent use in Phase 2

The following distinctions should be enforced rigorously:

**Hazard source ≠ initiating event.** A toxic inventory is a hazard source; an opened valve may be an initiating change.

**Precondition ≠ cause ≠ enabling condition.** They play different logical roles.

**Deviation ≠ hazard ≠ consequence.** “High pressure” may be a deviation or unsafe state; rupture may be loss of containment; injury is consequence.

**Loss of control ≠ loss of containment.** The first may precede the second or occur without it.

**Safeguard ≠ barrier ≠ IPL.** “IPL” is the narrowest, method-qualified term. citeturn8search19

**Safety constraint ≠ operating target.** A target is desirable; violation of a safety constraint can create a system hazard.

**Control action ≠ controller failure.** An unsafe control action can occur even without a component being conventionally failed. citeturn14search3turn14search7

**Feedback ≠ alarm.** An alarm is one feedback mechanism; process indication, field observation, communication and analytical measurement can also provide feedback.

**Process model ≠ engineering process model.** In STPA usage, the controller's process model means its internal representation of system state; this must be distinguished from a thermodynamic or dynamic engineering model.

**Evidence gap ≠ negative evidence.** Unknown does not mean absent.

**Confidence ≠ probability.** JSEA confidence describes epistemic support unless a formally identified risk calculation provides frequency/probability.

**Inherently safer ≠ passively protected.** A passive barrier can mitigate an existing hazard; an inherent change modifies or removes the hazard source/conditions.

**Hazard reduction ≠ total-risk reduction.** A change can reduce one hazard while transferring risk elsewhere.

**Guidance ≠ standard ≠ regulation.** Their authority, applicability and jurisdiction differ.

**Engineering recommendation ≠ engineering approval.** JSEA may formulate the former; competent authorized humans retain the latter.

The resulting Phase 2 design target is therefore a JSEA system that can reconstruct **what hazardous material or energy exists, in what state, where it can go, what can change, by what mechanism, how fast, under what conditions, through which equipment and controls, toward which targets, with which safeguards and dependencies, and with what evidence**—while remaining explicit about what it does not know and what requires engineering calculation or human authority. This direction is consistent with CCPS's emphasis on understanding hazards and risk, HSE's integration of hazard identification with control/function lifecycle management, DIERS's mechanism-specific engineering, CSB's evidence from real process accidents, and STPA's treatment of safety constraints, feedback and unsafe interactions. citeturn2search13turn20search1turn18search6turn21search1turn14search5 **Overall confidence in the Phase 1 architecture: high for the foundational concepts and hybrid direction; moderate-high for the proposed ontology/grammar details pending Phase 2 validation against real JSEA cases.**