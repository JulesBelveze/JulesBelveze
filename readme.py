from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🙂 [link=https://www.linkedin.com/in/jules-belveze/]Jules Belveze", guide_style="bold bright_black")

python_tree = tree.add("📦 Open Source", guide_style="bright_black")
python_tree.add("[bold link=https://github.com/JulesBelveze/time-series-autoencoder/]tsa[/]       - [bright_black]Dual-attention autoencoder")
python_tree.add("[bold link=https://github.com/JulesBelveze/bert-squeeze/]bert-squeeze[/]    - [bright_black]Shrink down transformers")
python_tree.add("[bold link=https://github.com/JulesBelveze/nlptest/]nlptest[/] - [bright_black]Behavioral testing")
python_tree.add("[bold link=https://github.com/JulesBelveze/time-series-dataset/]time-series-dataset[/]   - [bright_black]Dataset utilities")
python_tree.add("[bold link=https://huggingface.co/datasets/JulesBelveze/tldr_news/]tldr_news[/]    - [bright_black]Summarization dataset")

contrib_tree = tree.add("👍 Contributions", guide_style="bright_black")
contrib_tree.add("[bold link=https://koaning.github.io/bulk]bulk[/]      - [bright_black]contributed the color feature")
contrib_tree.add("[bold link=https://github.com/BitVoyage/FastBERT]FastBERT[/]      - [bright_black]contributed the batching inference")

talk_tree = tree.add("📄 Blogs & Papers", guide_style="bright_black")
talk_tree.add("[bold link=https://ieeexplore.ieee.org/document/9564190]Atlastic Reputation AI[/]")
talk_tree.add("[bold link=https://neptune.ai/blog/mlops-examples-model-development-in-hypefactors]Real-World MLOps Examples: Model Development in Hypefactors[/]")
talk_tree.add("[bold link=https://cloudblogs.microsoft.com/opensource/2022/04/19/scaling-up-pytorch-inference-serving-billions-of-daily-nlp-inferences-with-onnx-runtime/]Scaling-up PyTorch inference: Serving billions of daily NLP inferences with ONNX Runtime[/]")

console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)