# LLM Inference and Model-Behavior Research

Use this reference for LLM training, inference, serving, abliteration, model behavior, MoE, distillation, and evaluation.

## Foundations

Build from linear algebra, probability, optimization, neural networks, backpropagation, attention, tokenization, embeddings, parameters, data quality, generalization, bias/variance, overfitting, cross-validation, and evaluation. Add supervised, unsupervised, semi-supervised, SFT, preference/RL-style methods, distillation, mixture-of-experts, and multimodal/diffusion concepts as outcomes require.

## Inference and serving

Cover batching, dynamic batching, KV cache, memory hierarchy, quantization, precision, parallelism, scheduling, throughput/latency/cost, streaming, cancellation, admission control, observability, capacity, failure recovery, and secure deployment. Current model, GPU, driver, framework, and API details are volatile.

## Model-behavior research

Frame abliteration and behavior modification as controlled research: state the hypothesis, identify measurements, choose interventions, preserve an untouched baseline, run regression and safety tests, record provenance, and define rollback. Do not promise that an intervention removes a behavior reliably or preserves unrelated capabilities. Redirect harmful evasion or unsafe operationalization toward interpretability, robustness, safety evaluation, or benign alignment research.

## Training scale

A one-billion-parameter-from-scratch goal requires data, tokenizer, architecture, optimizer, compute, memory, network, checkpoint, evaluation, safety, cost, and governance estimates. Build staged evidence from small models before larger training; never infer feasibility from parameter count alone.
