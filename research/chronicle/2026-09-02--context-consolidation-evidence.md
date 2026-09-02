# Chronicle — context, memory, model and evidence decision boundary

Recorded: 2026-09-02

\`\`\`yaml
harness_ref: e80097fe8eb88c9e9340732683710ba1dc2ae008
manifest: harness-adoption.yaml
task_id: DIDEROT-CONTEXT-CONSOLIDATION-20260902
base_commit: 12a6282a08fd7538183df28c88832f8443d87715
authoritative_sources:
  - https://github.com/jbecirovski/jetson-llm-maxperf
  - https://mistral.ai/news/forge/
  - https://www.figure.ai/news/helix
  - https://www.figure.ai/news/helix-02
  - https://arxiv.org/abs/2005.11401
current_gates:
  - draft research synthesis; no new scientific result is claimed
  - benchmark quantities remain bounded to their published configurations
  - vendor robot descriptions are self-reported, not independent reliability evidence
  - MMALS context-to-consolidation boundary remains a hypothesis and experimental programme
intended_action: preserve the full reasoning chain and prevent future lossy summaries
\`\`\`

## Decision history preserved

1. The initial energy discussion suggested reducing history/context on an embedded LLM.
2. The architecture question was widened from “which LLM?” to “what is the smallest sufficient inference capability?”
3. The user corrected the assumption that continual learning had to occur on the edge: local experience may be uploaded and consolidated offline.
4. The analogy between mobile robotics and an LLM agent was challenged as unjustified.
5. The author's likely belief was reconstructed narrowly as conditional embedded-systems optimisation, not replacement of SLAM/planning/control by a language model.
6. Humanoid examples were examined to identify what is actually deployed: multi-rate semantic, visuomotor and motor-control layers learned from Internet data, teleoperation, human motion, simulation and robot experience.
7. The question became a general threshold among context, RAG, memory, learned state, adapter, fine-tuning, distillation and specialist model.
8. Mistral Forge was retained as an industrial example of institutional knowledge consolidation, but not as evidence for the threshold itself.
9. The governing principle was formulated as a distinct evidence base and model base: a model may encode knowledge without becoming the authority for it.

## Prohibited future compression

A later summary must not erase:

- the distinction \(C_t \neq M_t \neq b_t/z_t \neq \theta_t\);
- the user's correction that CL can be offline after reconnection;
- the rejected “robot = LLM agent” shortcut;
- the charitable reconstruction of the source author's belief;
- the conditional-estimand distinction \(P(Y\mid A)\) versus \(P(A\mid G)\);
- the multi-rate humanoid architecture and the difference between training data and deployed weights;
- full lifecycle cost including evidence, evaluation, non-regression, qualification and provenance;
- volatile facts as poor candidates for parametric memorisation;
- the fact that finite regression suites do not prove global non-regression;
- the research status of the proposed decision boundary.

## Produced artifacts

- \`research/2026-09-02--context-memory-model-evidence-decision-boundary.md\`
- \`research/sources/2026/2026-09-02--jetson-llm-maxperf.md\`
- this append-only chronicle record

## Exact next admissible action

Independently review the source transcriptions and scientific boundaries, then design a preregistered experiment that budget-matches long-context/RAG and consolidation treatments. Only after that review should the synthesis be promoted from draft or decomposed into stable pedagogical concept pages.
