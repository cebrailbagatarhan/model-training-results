# Bigg 50M — V4.1-Flash-inspired

- Status: pending controlled benchmark
- JEPA / EMA teacher: removed
- Design direction: causal encoder–decoder, compressed global KV, Engram-style n-gram memory, sparse MoE, gated residual mixing
- First planned seed: 42
- First planned budget: 600 s
- Baseline to beat: Bigg 50M JEPA-off test NLL 5.607873 / PPL 272.563981

This is a Bigg-scale experimental adaptation inspired by modern CED/efficient-memory ideas. It is not presented as an exact reproduction of another model's full production stack.

Experiment: [`../../../../experiments/bigg-50m-v41-flash/`](../../../../experiments/bigg-50m-v41-flash/)
