"""Regenerate the FST reference and Mermaid diagrams from the executable model.

Run from resumeLeans: python -m scripts.document_transducers
"""
from collections import defaultdict
from pathlib import Path

from src.normalization.transducers import TRANSFORMACIONES, construir_transducer


def main():
    destination = Path(__file__).resolve().parents[1] / "docs" / "Transducers"
    aliases = defaultdict(dict)
    for alias, token in TRANSFORMACIONES.items():
        aliases[token][alias] = token
    lines = [
        "# Executable finite-state transducer specification", "",
        "Generated with `python -m scripts.document_transducers`. Do not edit the generated tables.", "",
        "The program uses one nondeterministic FST. Each alias contributes a separate character route, "
        "sharing only the start state and accepting state. Multiple routes may accept the same input "
        "but produce the same canonical token. There are no epsilon-input transitions.", "",
        "Each section below shows the part of the FST that produces one output token. "
        "To combine these parts into the complete FST, rename every internal state with its token "
        "prefix, then merge the shared q0 and q_aceptacion states. State numbers within each section "
        "are local. No transitions between internal states of different sections exist.", "",
        "For each section M = (Q, Sigma, Gamma, delta, omega, q0, F). The table defines delta "
        "and omega jointly: a row (p, a, q, w) means an edge p --a/w--> q. "
        "Absent edges reject. Output epsilon means the empty word, not an input transition. "
        "Letters accept both ASCII cases. An alias space accepts one or more spaces/tabs through "
        "a consuming self-loop. Only the last character emits the complete canonical token.", "",
        "Unknown terms have no accepting path. The wrapper removes duplicate output tokens and "
        "sorts them; profile-specific ordering happens later. JAVA, MYSQL and MONGODB are retained "
        "as skills but do not change any profile's acceptance requirements.", "",
        "The PNGs under GRAPHICS show an earlier version. "
        "Use the Mermaid diagrams below for the current model.", "",
    ]
    for token, mapping in sorted(aliases.items()):
        fst = construir_transducer(mapping)
        grouped = defaultdict(list)
        for (source, symbol), destinations in fst.transitions.items():
            for target, output in destinations:
                grouped[(str(source), str(target), "".join(output))].append(symbol)
        lines += [f"## {token}", "", "Aliases: " + ", ".join(f"`{a}`" for a in mapping), "",
                  "- Q = {" + ", ".join(sorted(fst.states)) + "}",
                  "- Sigma = {" + ", ".join(repr(x) for x in sorted(fst.input_symbols)) + "}",
                  "- Gamma = {" + ", ".join(sorted(fst.output_symbols)) + "}",
                  "- Initial state: q0", "- F = {q_aceptacion}", "",
                  "| Source | Input alternatives | Destination | Output word |",
                  "|---|---|---|---|"]
        diagram = ["```mermaid", "stateDiagram-v2", "    [*] --> q0", "    q_aceptacion --> [*]"]
        for (source, target, output), symbols in sorted(grouped.items()):
            label = ", ".join("SPACE" if s == " " else "TAB" if s == "\t" else s for s in sorted(set(symbols)))
            word = output or "epsilon"
            lines.append(f"| {source} | `{label}` | {target} | {word} |")
            diagram.append(f"    {source} --> {target}: {label} / {word}")
        lines += [""] + diagram + ["```", ""]
    (destination / "Definiciones formales transducers.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
