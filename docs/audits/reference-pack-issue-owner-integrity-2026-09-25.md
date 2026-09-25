# Issue #306 — Reference Pack issue-owner integrity

Date: 2026-09-25  
Disposition: **ADOPT_DOC_ONLY**

## Question

Can issue-backed evidence navigation in Needle Reference Pack v0.1 be made
drift-detectable or release-verifiable without copying GitHub issue history into a
second legal-truth store?

## Measured exposure

The frozen Reference Pack contains 81 cases and 54 unique GitHub issue owners.

Current evidence-map analysis:

- **45/81 cases (55.6%) are issue-only**: their pack evidence refs contain no
  commit-pinned repository `path:` owner;
- 36/81 cases have at least one commit-pinned repository path;
- **32/54 unique issue owners** serve only issue-only cases;
- 22/54 issue owners are attached only to cases that also have a Git-backed path;
- there are no mixed issue owners in the current pack.

This makes issue mutability a material release-integrity limitation rather than an
edge case. It does **not** make the 45 cases invalid; it limits what the frozen pack
can claim to preserve about their underlying issue evidence.

## GitHub mutability facts

Authoritative GitHub documentation confirms:

- issue titles and descriptions are editable;
- issue/comment content exposes edit-history metadata;
- comment edit history can have revision content removed;
- GitHub retains at most 100 edits per content item;
- issue comments themselves are editable and can be added after an issue is closed.

References:

- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/editing-an-issue
- https://docs.github.com/en/communities/moderating-comments-and-conversations/tracking-changes-in-a-comment
- https://docs.github.com/en/graphql/reference/issues
- https://docs.github.com/en/rest/issues/comments
- https://docs.github.com/en/rest/issues/issues

The repository demonstrates the distinction directly:

- Issue #61 is currently an issue-body-only owner with zero comments.
- Issue #88 is a multi-comment evaluation owner whose issue remained navigable after
  closure while later comments were added. Its URL/identity stayed stable while the
  evidence-bearing conversation evolved.

A stable issue number, database ID or GraphQL node ID identifies the mutable GitHub
object. It does not freeze that object's body or comments.

## Guarantees matrix

| Approach | Stable identity | Detect content drift | Recover prior content | Offline pack rebuild | Duplicates evidence/truth | Assessment |
| --- | --- | --- | --- | --- | --- | --- |
| Existing issue URL | Yes, practically navigable | No | No | Yes | No | Correct navigation, not archival fixation |
| Add database/node ID | Stronger object identity | No | No | Yes | No | Does not solve the actual problem |
| Add `updated_at` | Object-change signal only | Weak/noisy | No | Requires captured metadata | No | False precision; not content integrity |
| Hash issue body + comments | Yes | Yes, for captured canonicalization | **No** | No, unless a snapshot/input is also preserved | No content copy, but adds network/release state | Detects loss after the point when recovery is already impossible |
| Rely on GitHub edit history | N/A | Partial | Partial/non-durable | No | No | History may be redacted and is capped; not an archival contract |
| Copy Git-backed issue snapshot | Yes | Yes | Yes | Yes | **Yes** unless ownership is redesigned | Solves archival recovery by paying the complexity the pack deliberately avoids |

## Adversarial analysis of fingerprint attestation

A content fingerprint is the strongest superficially attractive middle option.

A deterministic digest over:

- issue number / immutable object ID;
- issue body;
- top-level comment IDs;
- comment bodies;
- comment ordering;

would answer one useful question:

> Does the live GitHub issue conversation still have exactly the bytes/state that were
> attested at release time?

But it does **not** answer the more important archival question:

> What did the evidence owner contain when the Reference Pack was frozen?

Once the live content differs, the hash proves drift but cannot reconstruct the prior
state. Recovery would still depend on GitHub's edit history or another snapshot. GitHub
explicitly allows edit-history revision content to be removed and caps retained edits, so
that history cannot be promoted into Needle's frozen evidence substrate.

Fingerprinting also damages one of Reference Pack v0.1's strongest properties: the pack
currently rebuilds offline from the canonical Git corpus index. Exact issue-content
fingerprints require GitHub/network/repository access at release time, or a separately
preserved issue snapshot. The former creates a second non-Git input to release
reproducibility; the latter is effectively the snapshot approach under a different name.

Therefore a fingerprint would add integrity theatre unless a real consumer first needs
drift detection without historical recovery.

## What the frozen pack actually guarantees

Reference Pack v0.1 reproducibility applies to:

- the frozen corpus membership/classification source;
- the generated pack bytes;
- commit-pinned repository-path owners;
- exposure/reuse metadata and navigation structure.

It does **not** freeze the historical bytes of live GitHub issue bodies/comments.

For `issue:` evidence refs, the pack guarantees a navigation pointer to the project
evidence owner, subject to repository access and the owner's later mutation.

That distinction should be explicit in project/release governance.

## Durable rule

For future frozen/released artifacts:

> A GitHub issue number, URL, database ID, node ID, timestamp or content hash does not by
> itself make issue evidence historically recoverable. If a reproducibility/archival claim
> requires the exact issue content as-of release, preserve that content in a Git-backed
> artifact with a clear ownership role, or explicitly state that the issue ref is mutable
> navigation only.

Do not backfill the current 45 issue-only cases merely to make the metric prettier. A
backfill is justified only if a concrete archival/reuse job requires historical recovery
of those issue owners.

## Disposition

**ADOPT_DOC_ONLY**

Reason:

- the gap is real and affects 55.6% of current cases;
- object IDs/timestamps do not freeze content;
- fingerprints detect drift but cannot recover evidence and compromise the simple offline
  release model;
- Git-backed snapshots would recover evidence but create duplicated ownership/maintenance
  without a demonstrated need;
- the strongest boring solution is to state the exact guarantee honestly and preserve the
  current pack architecture.

Reference Pack v0.1 remains frozen and unchanged.

## Next implication

Future release/review work must distinguish:

- **commit-pinned evidence owner** — frozen/recoverable from Git;
- **mutable issue navigation owner** — stable reference to a live project record, not
  frozen evidence bytes.

A future real archival consumer can earn a snapshot/attestation mechanism. #306 does not.
