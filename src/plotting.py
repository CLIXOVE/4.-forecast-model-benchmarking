import matplotlib.pyplot as plt

def scatter_accuracy_vs_stability(df, x="wape", y="avg_rolling_wape", label_col="model", outpath=None):
    plt.figure(figsize=(9,5))
    plt.scatter(df[x], df[y])
    for _, r in df.iterrows():
        plt.text(r[x], r[y], str(r[label_col]))
    plt.xlabel("Overall WAPE (accuracy)")
    plt.ylabel("Average Rolling WAPE (stability)")
    plt.title("Accuracy vs Stability Trade-off")
    plt.tight_layout()
    if outpath is not None:
        plt.savefig(outpath, dpi=200, bbox_inches="tight")
