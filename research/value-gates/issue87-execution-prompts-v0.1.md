# Needle Relay v0.1 — execution prompts

These prompts are safe to keep in GitHub because they contain no case questions or answer keys.

## Stage A — Arm R (free-form baseline)

Give the fresh investigator **one Stage A case object** from the sealed Stage A packet file, then send:

> You are Investigator A in a blinded research handoff experiment.
>
> Answer the supplied legal-information question using the supplied official-source packet and any additional authoritative sources you genuinely need.
>
> Leave a competent free-form research artifact for another investigator. Include your answer, sources actually used, useful notes, and anything unresolved.
>
> Do not use or imitate a named Needle methodology. Do not speculate about possible follow-up questions. Do not search for Issue #87, Stage B packets, or answer keys.

Save A's artifact verbatim.

## Stage A — Arm M (Method)

Give the fresh investigator one Stage A case object, then send:

> You are Investigator A in a blinded research handoff experiment.
>
> Investigate the supplied legal-information question using the source packet and any additional authoritative sources you genuinely need.
>
> Produce a handoff dossier containing:
> - answer;
> - sources actually used and what each proves;
> - source origin versus legal authority where relevant;
> - exact legal target and scope;
> - temporal perspective / relevant dates;
> - current versus historical state where relevant;
> - uncertainty;
> - forbidden inferences;
> - unresolved points.
>
> Do not create persistent canonical software state. Do not speculate about possible follow-up questions. Do not search for Issue #87, Stage B packets, or answer keys.

Save A's dossier verbatim.

## Stage A — Arm C (Core)

Give the fresh investigator one Stage A case object and repository access, then send:

> You are Investigator A in a blinded research handoff experiment.
>
> Investigate the supplied question using Needle Method discipline.
>
> In addition, persist only the smallest justified Needle Core state using existing canonical contracts in the repository. Do not invent a new schema. Do not serialize hypothetical facts that were not observed. Do not use parked higher-level projections such as Thread, X-Ray, Retrieval, Source Anomaly or Half-Life.
>
> Your handoff package must include:
> - Method dossier;
> - exact Core objects/fixtures created or proposed;
> - schema/version references;
> - why persistence is justified;
> - what you deliberately did not persist.
>
> Do not search for Issue #87 Stage B packets or answer keys.

Save the entire handoff package verbatim.

## Stage B — all arms

Start a **new** chat/session/agent with no Stage A conversation.

Give it:

1. A's saved artifact;
2. the matching Stage B case object from the sealed Stage B packet.

Then send:

> You are Investigator B. You did not participate in the original investigation.
>
> Answer the follow-up question using only the handoff artifact plus official/primary sources you decide to reopen or newly consult.
>
> Record:
> - final answer;
> - why it follows;
> - every source reopened;
> - every new source consulted;
> - facts you had to rediscover because the handoff did not preserve them;
> - uncertainty or unresolved points.
>
> Do not ask which experimental arm produced the artifact. Do not search for Issue #87 or any answer key.

Save B's response verbatim.

## Evaluator

Only after the intended independent runs are complete:

1. verify the sealed artifacts against the committed SHA-256 hashes;
2. reveal the answer key;
3. evaluate each A→B pair against the concrete failure events in the protocol;
4. do not infer hidden reasoning from prose quality;
5. preserve parity and negative results;
6. update project-value evidence only if the result changes confidence in Method/Core.
