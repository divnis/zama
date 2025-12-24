# Confidential Space Reputation – Zama FHE Concept

## Overview
This project explores how on-chain reputation and reward systems
for X (Twitter) Spaces can be built using Zama’s Fully Homomorphic
Encryption (FHE) to preserve user privacy while remaining verifiable
on-chain.

Traditional Space reward systems expose user scores, rankings,
and engagement metrics publicly. This project proposes a
confidential alternative where sensitive data remains encrypted
throughout computation and storage.

## Problem
Current Space reward systems suffer from:
- Public exposure of user scores and rankings
- Easy leaderboard farming and bot exploitation
- Lack of privacy for real participants
- Off-chain trust assumptions

## Solution: Zama FHE
Using Zama FHEVM, this project proposes:
- Encrypted reputation points per wallet
- On-chain storage of encrypted scores
- Confidential score updates after Space participation
- Optional user-controlled decryption

The smart contract never sees plaintext values —
only encrypted handles.

## Conceptual Flow
1. User joins an X Space via a shared link
2. Participation proof is verified (off-chain or oracle-based)
3. Reputation points are encrypted client-side
4. Encrypted values are sent to the FHEVM contract
5. Contract updates encrypted reputation on-chain
6. Only the user (or approved entities) can decrypt

## Why FHE Matters Here
Without FHE:
- Scores must be public
- Ranking logic leaks user behavior
- Bots can reverse-engineer incentives

With Zama FHE:
- Scores remain private
- Logic executes on encrypted data
- Fairness without surveillance

## Repository Structure
- `app.py` – Prototype backend / demo service
- `templates/` – Demo UI
- `docs/` – Space reward & privacy design
- `README.md` – Project overview and Zama motivation

## Status
This repository focuses on:
- Architectural design
- Confidential computation model
- Zama FHEVM suitability analysis

Full production deployment (relayers, oracles, and SDK wiring)
is considered future work.

## Built For
Zama FHEVM Bounty Program
